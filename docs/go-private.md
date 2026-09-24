# Runbook: making a temporarily-public repo private

`sggs-data`, `sggs-platform` and `algominutes` are public only for free Actions minutes (see
`intended_visibility: private` in `catalog.yaml`). This is the checklist for flipping them.
Visibility changes need explicit owner approval (`AGENTS.md` §3).

## Status (25 Sep 2026)

| Step | State |
|---|---|
| Consumers accept an optional read token | PRs open: `sggs-platform#162`, `gurbani-soul-ios#13` |
| Org Actions billing works | **Blocked** — private-repo jobs refused: "recent account payments have failed" |
| `SGGS_READ_TOKEN` org secret exists | Not yet (owner creates it) |

## Why the order matters

- **Billing.** Private-repo minutes bill to the org. If billing is failing, every job on a flipped
  repo is refused, including `sggs-platform`'s production deploy.
- **Cross-repo reads.** A workflow's `github.token` reads only its own repo. `sggs-platform` and
  `gurbani-soul-ios` fetch `sggs-data` (and `gurbani-soul-ios` vendors from `sggs-platform`), so a
  private `sggs-data` returns 404 to them unless they use a token that can read it.
- **Security features.** Secret scanning and push protection are free only on public repos. After the
  flip they switch off unless the org buys GitHub Secret Protection. The repos' own gitleaks CI stays.
- **Cost.** September 2026 usage priced at the private rate: `sggs-platform` ≈ $32/month Linux
  (its macOS jobs moved to `gurbani-soul-ios`), `algominutes` ≈ $26, `sggs-data` < $1. The Team plan's
  included minutes offset part of this. Check current rates on the billing page first.

## 1. Prerequisites (owner)

1. Fix billing: Algorythmos-AI → Settings → Billing & plans. Confirm with a manual run of any
   private-repo workflow (e.g. `.github-private` → Actions → Catalog → Run workflow).
2. Create the read token: a **fine-grained personal access token** (or a GitHub App installation)
   - Resource owner: `Algorythmos-AI`
   - Repository access: only `sggs-data` and `sggs-platform`
   - Permissions: Contents **read**, Metadata read. Nothing else.
   - Expiry: set one and diary the rotation.
3. Store it as an **org** secret available to selected repos only, typing the value at the hidden prompt:
   ```bash
   gh secret set SGGS_READ_TOKEN --org Algorythmos-AI --visibility selected --repos sggs-platform,gurbani-soul-ios
   ```
4. Merge the two consumer PRs. Then re-run one `scripture-integrity` and one `ci` run and confirm the
   dataset steps still pass. They now use the new token.

## 2. Flip, in this order

1. `algominutes`. Nothing depends on it.
2. `sggs-data` and `sggs-platform` together, only after step 1.4 is green.
3. `gurbani-soul-ios` stays public (`intended_visibility: public`).

```bash
gh repo edit Algorythmos-AI/<repo> --visibility private --accept-visibility-change-consequences
```

## 3. After each flip

1. `catalog.yaml`: set `visibility: private`, then `make render`, and commit.
2. `make properties APPLY=--apply`. The sensitive properties (`data-class`, `intended-visibility`)
   are set automatically once a repo is private.
3. `make validate`. It must be clean.
4. Watch the next CI run and production deploy on the flipped repo. Any 404 on a dataset step means the
   token is missing from that repo or lacks Contents: read.

## Rollback

`gh repo edit Algorythmos-AI/<repo> --visibility public --accept-visibility-change-consequences`,
then revert the catalog change. Stars and watchers are erased when a repo goes private. These repos had
none on 25 Sep 2026.
