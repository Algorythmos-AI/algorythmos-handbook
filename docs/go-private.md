# Final phase: making every repo private

**Owner decision (25 Sep 2026):** all work happens with repos public, on free Actions compute. The last
step of the org plan is to make **every** repo private. Until the owner says go, nothing here runs.
Visibility changes need explicit owner approval (`AGENTS.md` §3).

`catalog.yaml` records the end state: every entry has `intended_visibility: private`, except
`.github`, which stays public as the org homepage (owner decision, 25 Sep 2026). The member homepage lists what is still public under "Temporarily public".

> **Licence exposure while public (found 25 Sep 2026).** `sggs-data` tracks `db/sggs.sqlite` in Git LFS, and that
> database contains the full English translation layer (`MANIFEST.json`: `translations_en = 58039`). Its
> `NOTICE.md` says that layer is for personal, non-commercial use and must not be redistributed publicly. While
> the repo is public, the file is publicly downloadable. Flipping `sggs-data` (with its consumers) closes it;
> the owner decides when.

## Public today → private at the end

| Repo | Depends on / consumed by | Notes |
|---|---|---|
| `algominutes` | none | Proprietary licence. macOS CI job. |
| `wassup-secretary` | none | Proprietary; created 24 Sep 2026. |
| `ichr-website` | none | Client site; its README credits Algorythmos publicly. Vercel Pro deploys private repos fine. |
| `sggs-data` | read by `sggs-platform`, `gurbani-soul-ios` | Flip together with its consumers. |
| `sggs-platform` | reads `sggs-data`; read by `gurbani-soul-ios` | Production deploy fetches the dataset. |
| `gurbani-soul-ios` | reads `sggs-data`, `sggs-platform` | macOS CI jobs. |
| `trading-lab-research` | deploys the status dashboard to Vercel; a GCP VM pulls it over HTTPS | Public since 30 Sep 2026 for Actions compute (owner decision; risk acceptance in its `SECURITY.md`). Holds course-derived specifications, so it is first in line to flip. Before flipping: add the VM's deploy key, switch the VM's remote to SSH and keep `GH_TOKEN` set (its `docs/runbooks/gcp-host.md`). |
| `hft-lab` | none | Created public on 10 Oct 2026 for Actions compute (owner decision, D-026). Holds code and design records only; a leak check blocks papers, data and knowledge-base text. Nothing is deployed from it yet. |
| `crypto-lab` | none yet; after the cutover a GCP VM pulls it over HTTPS | Created public on 11 Oct 2026 for Actions compute (owner decision, D-026), as its code already was inside `trading-lab-research`. Holds the crypto desk's code and research records; no course-derived material (its history is checked for it on every extraction). Before flipping, once the host runs it: give the VM a deploy key and switch its remote to SSH. |
| `trading-focus-card-ledger` | written by the ledger's cloud routines over HTTPS | **Owner to confirm.** Found public on 16 Nov 2026, the day it was renamed from `focus-card-ledger`; it was private before and the catalog said never public, because it holds market data. |
| `algorythmos-api` | none | **Owner to confirm.** Found public on 5 Oct 2026 while the catalog said private (changed about 29 Sep 2026; no decision recorded). Data class confidential. Secret scanning shows no open alerts. |
| `algorythmos-website` | none | **Owner to decide.** Made public on purpose by the website programme (D-009), after D-002 was written; the catalog still says intended private. At go-private time either flip it with the rest or set `intended_visibility: public` in the catalog. |
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
   `algorythmos-handbook` → Actions → Catalog → Run workflow.
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
