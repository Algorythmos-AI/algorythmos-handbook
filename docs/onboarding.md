# Onboarding

## Your first 30 minutes

1. **[Glossary](glossary.md)** — 5 minutes. SGGS, Ang, WASSUP, Wassup Doc, Genesis, ICHR, PDTO,
   Integrant, Vision On Care: every term you'll see in a repo name.
2. **[Architecture](architecture.md)** — 10 minutes. One diagram per product showing which repo feeds
   which, and where each one runs.
3. **[Repository map](../profile/README.md#repository-map)** on the member homepage — find your repo.
   The map is generated from [`catalog.yaml`](../catalog.yaml); status, visibility, branch, deploy
   target and live URL are all there. For WASSUP read the
   [product map](wassup-product-map.md) first: only three of twenty repos are live.
4. **Open the repo.** Its README starts with a standard header: what it is, **Status**, **Owner**,
   **Runs at**, **Run locally**. The six flagship repos (`gurbani-soul-ios`, `sggs-platform`, `sggs-data`,
   `algominutes`, `wassup-secretary`, `ichr-website`) keep their own, longer README format; the catalog
   entry is authoritative for all of them.
5. **[Decision log](decisions.md)** — why things are the way they are (public for now, `sggs-*` names,
   dormant WASSUP repos labelled not archived, Vision On Care archived, …). Check it before proposing a
   structural change.
6. If you are an AI agent: **[`AGENTS.md`](../AGENTS.md)** is binding.

## Access

- Org membership requires **two-factor authentication** (enforced at org level).
- Install the GitHub CLI and sign in: `gh auth login`. Most runbooks here use `gh`.
- Deploy platforms are connected at org level: the **Vercel**, **Render** and **Claude** GitHub
  apps are installed for all repos. Ask the owner for access to the matching dashboards.

## Branches and gates

| Model | Repos | Flow |
|---|---|---|
| `integration` → `main` | deployed web platforms (`sggs-platform`, `ichr-website`, `algominutes`, `wassup-secretary`, `wassup-meeting`) | Feature branch → PR into `integration` (staging) → release PR into `main` (production). |
| `main` only | everything else (apps, data, client sites, dormant repos) | Feature branch → PR into `main`. Tags cut releases where relevant. |

Rulesets protect the trunk branches and release tags. CI must be green to merge. Each repo's
`CONTRIBUTING.md` lists its exact gates and `make` targets; read it before your first PR.

**Baseline protection on every repo.** The org ruleset `protect-default-branches` blocks force-push
and deletion of every default branch, with no bypass actors, so neither a mistyped command nor an
agent's token can lose history. For a deliberate history rewrite: Org Settings → Repository →
Rulesets → `protect-default-branches` → set enforcement to *Disabled*, do the rewrite, set it back
to *Active* immediately, and record why in [`decisions.md`](decisions.md).

## Finding repos

The repo list can be filtered by custom property, e.g. `props.product:wassup`,
`props.lifecycle:dormant` or `props.kind:service`. Values come from `catalog.yaml` via
`make properties`. Don't edit them in the UI.

## Labels, security workflow and CODEOWNERS

- **Labels:** the shared set lives in `Algorythmos-AI/.github/labels.json`. Run
  `scripts/sync-labels.sh` there after adding a repo. It adds and updates labels and never deletes any.
- **Security CI:** new repos call the reusable workflow in `Algorythmos-AI/.github` (see its README).
  Existing repos keep their own `security.yml` until switched one at a time, since switching renames the
  required check.
- **CODEOWNERS:** use `* @Algorythmos-AI/maintainers`. The team has `maintain` on every repo.
  While there is one maintainer, **don't** turn on "require review from code owners" in a ruleset,
  because you can't approve your own pull request.

## New repositories

- Public repos get secret scanning and push protection automatically from the org's default code
  security configuration ("GitHub recommended", applied to new **public** repos only; on private repos
  those features are paid). `make validate` fails if any public repo lacks them.
- Add the repo to `catalog.yaml`, then `make render` and `make properties APPLY=--apply`. Run
  `scripts/sync-labels.sh <repo>` in `.github` and grant `maintainers` `maintain`. The weekly check
  flags any repo missing from the catalog.

## Secrets

Secrets never go in git. Push protection is on for every public repo and will block a push that
contains one. If it does, **remove the secret and rotate it**. Don't bypass unless it is a
confirmed false positive, and say why in the bypass reason.

| Kind | Lives in |
|---|---|
| CI credentials | GitHub → repo → Settings → Secrets and variables → Actions |
| Runtime config | Vercel / Render / GCP project environment settings |
| Company records (ASIC, banking, client files) | Git-ignored folders on the owner's machine, never on GitHub. Ask the owner. |

## Moving a repo into the org

For each repo, one at a time:

1. **Pre-check:** open PRs from forks, GitHub Pages (Pages URLs do *not* redirect), Actions
   secrets, webhooks, deploy keys. Take a mirror backup: `git clone --mirror <url>`.
2. **Transfer:** `gh api -X POST repos/<owner>/<repo>/transfer -f new_owner=Algorythmos-AI`.
   Git and web URLs redirect as long as the old name is never reused.
3. **Verify:** refs match the backup (`git ls-remote`), secrets, webhooks and deploy keys are still
   attached, and the Vercel/Render project still shows the Git connection (reconnect it if not).
   Then run one deploy.
4. **Record:** update `catalog.yaml` (`repo`, `location: org`), `make render`, open a PR. After merge,
   `make properties APPLY=--apply`, sync labels (`scripts/sync-labels.sh <repo>` in `.github`) and
   grant the `maintainers` team `maintain` on the repo.
5. Update local remotes: `git remote set-url origin https://github.com/Algorythmos-AI/<repo>.git`.
