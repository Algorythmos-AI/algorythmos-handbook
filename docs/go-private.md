# Final phase: making every repo private

**Owner decision (25 Sep 2026):** all work happens with repos public, on free Actions compute. The last
step of the org plan is to make **every** repo private. Until the owner says go, nothing here runs.
Visibility changes need explicit owner approval (`AGENTS.md` §3).

`catalog.yaml` records the end state: every entry has `intended_visibility: private`, except
`.github`, which stays public as the org homepage (owner decision, 25 Sep 2026). The member homepage lists what is still public under "Temporarily public".

## Public today → private at the end

| Repo | Depends on / consumed by | Notes |
|---|---|---|
| `algominutes` | none | Proprietary licence. macOS CI job. |
| `wassup-secretary` | none | Proprietary; created 24 Sep 2026. |
| `ichr-website` | none | Client site; its README credits Algorythmos publicly. Vercel Pro deploys private repos fine. |
| `sggs-data` | read by `sggs-platform`, `gurbani-soul-ios` | Flip together with its consumers. |
| `sggs-platform` | reads `sggs-data`; read by `gurbani-soul-ios` | Production deploy fetches the dataset. |
| `gurbani-soul-ios` | reads `sggs-data`, `sggs-platform` | macOS CI jobs. |
| `.github` | none | **Stays public** (owner decision, 25 Sep 2026). It is the public org homepage. |

## What changes when they go private

- **Actions billing.** Private-repo minutes bill to the org. September 2026 usage at private rates:
  `sggs-platform` ≈ $32/month (Linux only; its macOS jobs moved out), `algominutes` ≈ $26,
  `gurbani-soul-ios` ≈ $21 (macOS), others under $5. The Team plan's included minutes offset part of
  this. **The org's billing must be working first**, or every job is refused ("recent account payments
  have failed", seen 24 Sep 2026).
- **Cross-repo reads.** A workflow's `github.token` reads only its own repo. `sggs-platform#162` and
  `gurbani-soul-ios#13` (merged) already read with `secrets.SGGS_READ_TOKEN || github.token`, so the
  only change needed is the secret.
- **Security features.** Secret scanning, push protection and private vulnerability reporting are
  free only on public repos. After the flip they switch off unless the org buys GitHub Secret
  Protection. The repos keep their own gitleaks CI.
- **Stars and watchers** are erased when a repo goes private (none recorded on 25 Sep 2026).
- **The public profile** (`.github/profile/README.md`) links to product websites, not repos, so it
  stays accurate. Its "How we build" line about public repositories becomes moot; edit it then.

## Steps (when the owner says go)

1. **Owner:** confirm org billing works. Manually run any private-repo workflow, e.g.
   `.github-private` → Actions → Catalog → Run workflow.
2. **Owner:** create a fine-grained token (resource owner `Algorythmos-AI`; repositories `sggs-data`
   and `sggs-platform`; Contents **read** + Metadata read; set an expiry). Store it by typing the value
   at the hidden prompt:
   ```bash
   gh secret set SGGS_READ_TOKEN --org Algorythmos-AI --visibility selected --repos sggs-platform,gurbani-soul-ios
   ```
   Then re-run one `scripture-integrity` (sggs-platform) and one `ci` (gurbani-soul-ios). Both must pass.
3. **Flip** the independent repos first: `algominutes`, `wassup-secretary`, `ichr-website`.
   Then flip `sggs-data`, `sggs-platform` and `gurbani-soul-ios` together.
   ```bash
   gh repo edit Algorythmos-AI/<repo> --visibility private --accept-visibility-change-consequences
   ```
4. **After each flip:** in `catalog.yaml` set `visibility: private`; then `make render`,
   `make properties APPLY=--apply` (sets the sensitive properties now that the repo is private) and
   `make validate`. Watch the next CI run and production deploy. A 404 on a dataset step means the token
   is missing from that repo or lacks Contents: read.
5. **Finally**, update `.github/profile/README.md` ("How we build") and this runbook's status.

## Rollback

`gh repo edit Algorythmos-AI/<repo> --visibility public --accept-visibility-change-consequences`,
then revert the catalog change.
