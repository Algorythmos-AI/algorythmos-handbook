#!/usr/bin/env python3
"""Validate, render and guard the Algorythmos repository catalog.

    catalog.py validate [--offline] [--expect-missing OWNER/REPO ...]
        Schema + enum checks. Online (default) also checks every entry against live GitHub via `gh`:
        the repo exists, visibility and default branch match, and every Algorythmos-AI repo is
        catalogued. Exit 1 on any error; stale-lifecycle findings are warnings only.

    catalog.py render [--check]
        Rewrite the generated block of profile/README.md from catalog.yaml.
        --check exits 1 if the file is out of date instead of writing it.

    catalog.py properties [--apply]
        Sync org custom properties (schema + per-repo values) from catalog.yaml. Dry-run by default:
        prints what would change. --apply writes, then reads back. `validate` (online) fails when
        live property values drift from the catalog.

    catalog.py check-public PATH
        Scan a checkout of the PUBLIC Algorythmos-AI/.github repo for anything that must never be
        published: private/personal repo names, street-address forms, bank-number shapes, personal
        email, relative links in the profile. The forbidden list is derived from this private catalog,
        which is why this check lives here and not in the public repo.

Requires PyYAML: `uv run --with pyyaml==6.0.2 python scripts/catalog.py ...`
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.yaml"
README = ROOT / "profile" / "README.md"
ORG = "Algorythmos-AI"
PERSONAL = "skalaliya"
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"

ENUMS = {
    "kind": {"app", "service", "web", "data", "monorepo", "library", "infra", "docs", "ops", "config"},
    "lifecycle": {"active", "dormant", "deprecated", "archived", "planned"},
    "visibility": {"public", "private"},
    "intended_visibility": {"public", "private"},
    "data_class": {"public", "internal", "confidential", "restricted"},
    "location": {"org", "personal"},
}
REQUIRED = ["repo", "product", "kind", "location", "lifecycle", "visibility",
            "intended_visibility", "data_class", "default_branch", "deploys_to"]
OPTIONAL = {"depends_on", "client", "target_name", "notes"}
ACTIVE_DAYS = 120
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def load() -> dict:
    return yaml.safe_load(CATALOG.read_text())


# ── validate ──────────────────────────────────────────────────────────────────
def schema_errors(cat: dict) -> list[str]:
    errs: list[str] = []
    products = cat.get("products") or {}
    seen: set[str] = set()
    for i, e in enumerate(cat.get("repos") or []):
        where = e.get("repo") or f"repos[{i}] ({e.get('target_name')})"
        for k in REQUIRED:
            if k not in e:
                errs.append(f"{where}: missing '{k}'")
        for k in e:
            if k not in REQUIRED and k not in OPTIONAL:
                errs.append(f"{where}: unknown key '{k}'")
        for k, allowed in ENUMS.items():
            if k in e and e[k] not in allowed:
                errs.append(f"{where}: {k}={e[k]!r} not in {sorted(allowed)}")
        if e.get("product") not in products:
            errs.append(f"{where}: product {e.get('product')!r} not defined under products")
        repo = e.get("repo")
        if repo is None:
            if e.get("lifecycle") != "planned":
                errs.append(f"{where}: repo may be null only when lifecycle is 'planned'")
            continue
        if repo in seen:
            errs.append(f"{repo}: duplicate entry")
        seen.add(repo)
        owner = repo.split("/")[0]
        expected_owner = ORG if e.get("location") == "org" else PERSONAL
        if owner != expected_owner:
            errs.append(f"{repo}: location={e.get('location')} but owner is {owner}")
        if e.get("location") == "personal" and not NAME_RE.match(e.get("target_name") or repo.split("/")[1]):
            errs.append(f"{repo}: personal repo whose name breaks the standard needs a valid target_name")
        if e.get("target_name") and not NAME_RE.match(e["target_name"]):
            errs.append(f"{where}: target_name {e['target_name']!r} is not lowercase kebab-case")
        if e.get("visibility") == "public" and e.get("data_class") in {"confidential", "restricted"} \
                and e.get("intended_visibility") != "private":
            errs.append(f"{repo}: public + {e['data_class']} data must have intended_visibility: private")
    return errs


def gh_json(args: list[str]):
    out = subprocess.run(["gh", *args], capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)}: {out.stderr.strip()}")
    return json.loads(out.stdout)


def live_repos() -> dict[str, dict]:
    fields = "nameWithOwner,visibility,defaultBranchRef,pushedAt,isArchived"
    live: dict[str, dict] = {}
    for owner in (ORG, PERSONAL):
        for r in gh_json(["repo", "list", owner, "--limit", "1000", "--json", fields]):
            live[r["nameWithOwner"]] = r
    return live


def live_errors(cat: dict, expect_missing: set[str]) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    live = live_repos()
    today = dt.date.today()
    catalogued = {e["repo"] for e in cat["repos"] if e.get("repo")}
    for e in cat["repos"]:
        repo = e.get("repo")
        if not repo:
            continue
        r = live.get(repo)
        if r is None:
            if repo not in expect_missing:
                errs.append(f"{repo}: not found on GitHub (renamed, transferred or deleted?)")
            continue
        if r["visibility"].lower() != e["visibility"]:
            errs.append(f"{repo}: catalog says {e['visibility']}, GitHub says {r['visibility'].lower()}")
        branch = (r.get("defaultBranchRef") or {}).get("name")
        if branch and branch != e["default_branch"]:
            errs.append(f"{repo}: default_branch {e['default_branch']!r}, GitHub says {branch!r}")
        if r["isArchived"] != (e["lifecycle"] == "archived"):
            errs.append(f"{repo}: archived={r['isArchived']} but lifecycle={e['lifecycle']}")
        pushed = dt.date.fromisoformat(r["pushedAt"][:10])
        stale = (today - pushed).days > ACTIVE_DAYS
        if e["lifecycle"] == "active" and stale:
            warns.append(f"{repo}: lifecycle active but last push {pushed} — consider dormant")
        if e["lifecycle"] == "dormant" and not stale:
            warns.append(f"{repo}: lifecycle dormant but pushed {pushed} — consider active")
    for name in sorted(n for n in live if n.startswith(ORG + "/")):
        if name not in catalogued:
            errs.append(f"{name}: exists in the org but is not in catalog.yaml")
    if gh_json(["api", f"orgs/{ORG}/properties/schema"]):  # only once properties are set up
        for repo, want in desired_values(cat).items():
            if repo in expect_missing or repo not in live:
                continue
            have = live_values(repo)
            for k, v in want.items():
                if have.get(k) != v:
                    errs.append(f"{repo}: property {k}={have.get(k)!r}, catalog says {v!r} — run `catalog.py properties --apply`")
    # Secret scanning + push protection are free on public repos and the public profile promises them.
    # New repos get them from the org's default code security configuration; this catches any gap.
    for name, r in sorted(live.items()):
        if name.startswith(ORG + "/") and r["visibility"].lower() == "public" and name not in expect_missing:
            sa = gh_json(["api", f"repos/{name}", "--jq", ".security_and_analysis"]) or {}
            for feature in ("secret_scanning", "secret_scanning_push_protection"):
                if (sa.get(feature) or {}).get("status") != "enabled":
                    errs.append(f"{name}: public repo without {feature} — enable it (free on public repos)")
    for name in sorted(expect_missing):
        if name in live:
            errs.append(f"{name}: passed --expect-missing but it exists — drop the flag")
    return errs, warns


def cmd_validate(a) -> int:
    cat = load()
    errs = schema_errors(cat)
    warns: list[str] = []
    if not a.offline and not errs:
        e2, warns = live_errors(cat, set(a.expect_missing or []))
        errs += e2
    for w in warns:
        print(f"warning: {w}")
    for e in errs:
        print(f"error: {e}")
    n = sum(1 for e in cat["repos"] if e.get("repo"))
    print(f"{'FAIL' if errs else 'OK'}: {n} repos, {len(errs)} errors, {len(warns)} warnings"
          f"{' (offline)' if a.offline else ''}")
    return 1 if errs else 0


# ── render ────────────────────────────────────────────────────────────────────
def link(repo: str) -> str:
    return f"[`{repo.split('/')[1]}`](https://github.com/{repo})"


def vis(e: dict) -> str:
    v = e["visibility"]
    return v if v == e["intended_visibility"] else f"**{v}** → {e['intended_visibility']}"


def esc(s) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def render_block(cat: dict) -> str:
    repos = cat["repos"]
    out = [
        f"_Generated from [`catalog.yaml`](https://github.com/{ORG}/.github-private/blob/main/catalog.yaml)"
        f" (updated {cat['updated']}). Edit the catalog, not this block._",
        "",
    ]
    org_entries = [e for e in repos if e["location"] == "org" and e["kind"] != "config"]
    out += ["### In this org", ""]
    for slug, p in cat["products"].items():
        group = [e for e in org_entries if e["product"] == slug]
        if not group:
            continue
        out += [f"#### {p['name']}", "", esc(p["summary"]), "",
                "| Repo | Kind | Visibility | Default branch | Ships to | Status | Notes |",
                "|---|---|---|---|---|---|---|"]
        for e in group:
            name = link(e["repo"]) if e["repo"] else f"_{e.get('target_name')}_ (no repo yet)"
            ships = ", ".join(e["deploys_to"]) or "—"
            branch = f"`{e['default_branch']}`" if e["default_branch"] else "—"
            out.append(f"| {name} | {e['kind']} | {vis(e)} | {branch} | {ships} | {e['lifecycle']} "
                       f"| {esc(e.get('notes'))} |")
        out.append("")
    personal = [e for e in repos if e["location"] == "personal"]
    if personal:
        out += ["### Lives elsewhere — to migrate into this org", "",
                "Algorythmos IP still in the personal account. Transfer one at a time (see "
                f"[`docs/onboarding.md`](https://github.com/{ORG}/.github-private/blob/main/docs/onboarding.md#moving-a-repo-into-the-org)).",
                "", "| Repo | Product | Proposed name | Ships to | Status | Notes |", "|---|---|---|---|---|---|"]
        for e in personal:
            p = cat["products"][e["product"]]["name"]
            tgt = f"`{e['target_name']}`" if e.get("target_name") else "_(keep)_"
            client = f"{e['client']}. " if e.get("client") else ""
            out.append(f"| {link(e['repo'])} | {esc(p)} | {tgt} | {', '.join(e['deploys_to']) or '—'} "
                       f"| {e['lifecycle']} | {esc(client + (e.get('notes') or ''))} |")
        out.append("")
    renames = [e for e in org_entries if e.get("repo") and e.get("target_name")]
    if renames:
        out += ["### Rename backlog (in-org)", "",
                "Generic names that collide across products. Rename only with explicit approval; GitHub keeps a "
                "redirect as long as the old name is never reused.", "",
                "| Current | Proposed |", "|---|---|"]
        out += [f"| {link(e['repo'])} | `{e['target_name']}` |" for e in renames]
        out.append("")
    temp = [e for e in repos if e.get("repo") and e["visibility"] == "public" and e["intended_visibility"] == "private"]
    if temp:
        out += ["### Temporarily public", "",
                "Public today for free Actions compute; intended private. Don't link these from public pages.", ""]
        out += [f"- {link(e['repo'])} — {e['data_class']} data" for e in temp]
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def cmd_render(a) -> int:
    text = README.read_text()
    if START not in text or END not in text:
        print(f"error: {README} is missing the {START} / {END} markers")
        return 1
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{render_block(load())}{END}{tail}"
    if a.check:
        if new != text:
            print("error: profile/README.md is out of date — run `make render` and commit")
            return 1
        print("OK: profile/README.md matches catalog.yaml")
        return 0
    README.write_text(new)
    print(f"rendered {README.relative_to(ROOT)}")
    return 0


# ── properties ───────────────────────────────────────────────────────────────
# catalog field -> org custom property. Personal-account repos can't carry org properties.
PROPERTY_FIELDS = {
    "product": "product",
    "kind": "kind",
    "lifecycle": "lifecycle",
    "data-class": "data_class",
    "intended-visibility": "intended_visibility",
    "client": "client",
}
PROPERTY_HELP = {
    "product": "Product this repository belongs to (see .github-private/catalog.yaml)",
    "kind": "What the repository is: app, service, web, data, monorepo, library, infra, docs, ops, config",
    "lifecycle": "active = pushed within 120 days; dormant; deprecated; archived; planned",
    "data-class": "Most sensitive data the repository holds",
    "intended-visibility": "Target visibility. Differs from actual visibility for temporarily-public repos",
    "client": "Client organisation, for client work only",
}


def desired_schema(cat: dict) -> dict[str, dict]:
    schema = {}
    for prop, field in PROPERTY_FIELDS.items():
        body = {"value_type": "single_select", "required": False, "description": PROPERTY_HELP[prop],
                "values_editable_by": "org_actors"}
        if prop == "product":
            body["allowed_values"] = sorted(cat["products"])
        elif prop == "client":
            body = {"value_type": "string", "required": False, "description": PROPERTY_HELP[prop],
                    "values_editable_by": "org_actors"}
        else:
            body["allowed_values"] = sorted(ENUMS[field])
        schema[prop] = body
    return schema


# Property values on a public repo are readable by anyone via the API, unauthenticated. These would
# advertise which public repos hold sensitive data or are about to go private, so they are unset on
# public repos and live only in the private catalog.
PRIVATE_ONLY_PROPERTIES = {"data-class", "intended-visibility"}


def desired_values(cat: dict) -> dict[str, dict[str, str | None]]:
    out = {}
    for e in cat["repos"]:
        if e.get("repo") and e["location"] == "org":
            vals = {prop: e.get(field) for prop, field in PROPERTY_FIELDS.items()}
            if e["visibility"] == "public":
                vals.update({p: None for p in PRIVATE_ONLY_PROPERTIES})
            out[e["repo"]] = vals
    return out


def live_values(repo: str) -> dict[str, str | None]:
    return {p["property_name"]: p["value"] for p in gh_json(["api", f"repos/{repo}/properties/values"])}


def gh_write(method: str, path: str, body: dict) -> None:
    out = subprocess.run(["gh", "api", "-X", method, path, "--input", "-"],
                         input=json.dumps(body), capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(f"{method} {path}: {out.stderr.strip()}")


def cmd_properties(a) -> int:
    cat = load()
    if errs := schema_errors(cat):
        print("error: fix catalog schema errors first (catalog.py validate --offline)")
        return 1
    mode = "APPLY" if a.apply else "DRY-RUN"
    live_schema = {p["property_name"]: p for p in gh_json(["api", f"orgs/{ORG}/properties/schema"])}
    changes = 0
    for prop, want in desired_schema(cat).items():
        have = live_schema.get(prop)
        same = bool(have) and all(have.get(k) == want[k] for k in ("value_type", "required", "description")) \
            and sorted(have.get("allowed_values") or []) == sorted(want.get("allowed_values") or [])
        if not same:
            changes += 1
            print(f"[{mode}] schema {prop}: {'create' if not have else 'update'} "
                  f"{want['value_type']} {want.get('allowed_values', '')}")
            if a.apply:
                gh_write("PUT", f"orgs/{ORG}/properties/schema/{prop}", want)
    live = {r["nameWithOwner"] for r in gh_json(["repo", "list", ORG, "--limit", "1000", "--json", "nameWithOwner"])}
    for repo, want in desired_values(cat).items():
        if repo not in live:
            print(f"[{mode}] skip {repo}: not on GitHub")
            continue
        have = live_values(repo) if live_schema else {}
        diff = {k: v for k, v in want.items() if have.get(k) != v}
        if diff:
            changes += 1
            print(f"[{mode}] values {repo}: " + ", ".join(f"{k}={v}" for k, v in diff.items()))
            if a.apply:
                gh_write("PATCH", f"orgs/{ORG}/properties/values", {
                    "repository_names": [repo.split("/")[1]],
                    "properties": [{"property_name": k, "value": v} for k, v in diff.items()]})
    if a.apply and changes:
        drift = []
        for r, want in desired_values(cat).items():
            if r in live:
                have = live_values(r)
                drift += [f"{r}: {k}" for k, v in want.items() if have.get(k) != v]
        print(f"read-back: {'OK' if not drift else 'MISMATCH ' + '; '.join(drift)}")
        return 1 if drift else 0
    print(f"{mode}: {changes} change(s)")
    return 0


# ── check-public ─────────────────────────────────────────────────────────────
FIXED_PATTERNS = {
    "street address": r"Elizabeth\s+St|Surry\s+Hills|\bLevel\s+1\b|\bUnit\s+1\b|\b2010\b",
    "BSB-shaped number": r"\b\d{3}-\d{3}\b",
    "personal email": r"[\w.+-]+@gmail\.com",
    "French registration": r"\bSIRET\b|\bSIREN\b",
    "tax file number": r"\bTFN\b",
    "local path": r"/Users/|scratchpad",
}


def cmd_check_public(a) -> int:
    cat = load()
    base = Path(a.path)
    public_words = {w.lower() for w in cat.get("public_words", [])}
    forbidden: dict[str, str] = {}
    for e in cat["repos"]:
        repo = e.get("repo")
        if not repo or e["visibility"] == "public" and e["location"] == "org":
            continue
        forbidden[f"private repo {repo}"] = re.escape(repo)
        name = repo.split("/")[1]
        if name.lower() not in public_words:
            forbidden[f"private repo name {name}"] = rf"(?<![\w.-]){re.escape(name)}(?![\w-])"
        if e.get("client") and not cat["products"][e["product"]]["public"]:
            forbidden[f"unannounced client {e['client']}"] = re.escape(e["client"])
    forbidden.update(FIXED_PATTERNS)
    hits = 0
    files = [p for p in base.rglob("*") if p.is_file() and ".git" not in p.parts]
    for p in files:
        text = p.read_text(errors="replace")
        for label, pat in forbidden.items():
            for m in re.finditer(pat, text, flags=re.IGNORECASE):
                line = text.count("\n", 0, m.start()) + 1
                print(f"LEAK {p.relative_to(base)}:{line}: {label}: {m.group(0)!r}")
                hits += 1
        if p.suffix == ".md":
            # Org-default files are displayed inside other repos, so relative links break there too.
            for m in re.finditer(r"\]\((?!https://|mailto:|#)([^)]+)\)", text):
                print(f"LINK {p.relative_to(base)}: relative link {m.group(1)!r} breaks outside this repo")
                hits += 1
            for m in re.finditer(r"http://", text):
                print(f"LINK {p.relative_to(base)}: insecure http:// link")
                hits += 1
    print(f"{'FAIL' if hits else 'OK'}: scanned {len(files)} files, {len(forbidden)} rules, {hits} hits")
    return 1 if hits else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("--offline", action="store_true")
    v.add_argument("--expect-missing", action="append", metavar="OWNER/REPO")
    r = sub.add_parser("render")
    r.add_argument("--check", action="store_true")
    p = sub.add_parser("properties")
    p.add_argument("--apply", action="store_true")
    c = sub.add_parser("check-public")
    c.add_argument("path")
    a = ap.parse_args()
    return {"validate": cmd_validate, "render": cmd_render, "properties": cmd_properties,
            "check-public": cmd_check_public}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
