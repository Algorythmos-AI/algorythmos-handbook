# Repository map

Every Algorythmos repo: what it is, where it ships and its visibility. The block below is generated
from [`catalog.yaml`](../catalog.yaml) by `make render`; edit the catalog, not this file. CI fails
when the two disagree.

<!-- catalog:start -->
_Generated from [`catalog.yaml`](https://github.com/Algorythmos-AI/algorythmos-handbook/blob/main/catalog.yaml) (updated 2026-11-17). Edit the catalog, not this block._

### In this org

#### Gurbani Soul

Sri Guru Granth Sahib Ji, verbatim and offline, cited by Ang — iPhone, iPad and web.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`gurbani-soul-ios`](https://github.com/Algorythmos-AI/gurbani-soul-ios) | app | active | — | **public** → private | `main` | testflight, app-store | Consumes sggs-data by commit + sha256 (dataset.lock.json). If sggs-data goes private, CI needs a read token. |
| [`sggs-platform`](https://github.com/Algorythmos-AI/sggs-platform) | monorepo | active | [gurbanisoul.com/search](https://gurbanisoul.com/search) | **public** → private | `integration` | render-api, vercel-web | Formerly sggs-knowledge-base (GitHub redirects). Temporarily public; NOTICE.md says intended private. |
| [`sggs-data`](https://github.com/Algorythmos-AI/sggs-data) | data | active | — | **public** → private | `main` | — | Temporarily public for Actions compute. Translation layer is licence-restricted — see NOTICE.md. |
| [`sggs-source`](https://github.com/Algorythmos-AI/sggs-source) | data | active | — | private | `main` | github-releases | Non-redistributable source PDF and translation files. Release assets are never replaced. |
| [`gurbani-soul-device-evidence`](https://github.com/Algorythmos-AI/gurbani-soul-device-evidence) | data | active | — | private | `main` | — | Created 2026-10-27; catalogued 2026-11-09. Raw physical-device test evidence for gurbani-soul-ios releases: each run is a GitHub Release with .xcresult bundles, RUN-NOTES.md and SHA256SUMS. Private because the bundles carry device identifiers, screen recordings and host paths. The reviewed record lives in gurbani-soul-ios ios/device-runs/. |

#### AlgoMinutes

AI meeting recorder — transcripts with speaker labels, structured minutes and action items.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`algominutes`](https://github.com/Algorythmos-AI/algominutes) | monorepo | active | — | **public** → private | `integration` | gcp-cloud-run, firebase | Proprietary licence. Temporarily public for Actions compute (uses macOS runners). |
| [`algominutes-test-history`](https://github.com/Algorythmos-AI/algominutes-test-history) | data | active | — | private | `main` | — | Created 2026-10-28; catalogued 2026-11-09. Every AlgoMinutes test run (iPhone and CI) kept as data for queries and backtesting (tools/query.py). Never named or linked from a public repository. |

#### WASSUP

AI for the clinic front desk — Secretary (phone receptionist), Wassup Doc (meeting notes), call analytics. Older generations kept for history; see docs/wassup-product-map.md.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`wassup-secretary`](https://github.com/Algorythmos-AI/wassup-secretary) | monorepo | active | — | **public** → private | `integration` | railway | Multi-clinic AI phone receptionist (voice gateway, core API, ops worker). Proprietary; temporarily public for CI compute. Created 2026-09-24. Staging (`integration`) is deployed to Railway by exact commit with scripts/deploy-railway.sh; production runs only `v*` tags on `main` (docs/runbooks/release.md in the repo). |
| [`wassup-web`](https://github.com/Algorythmos-AI/wassup-web) | web | dormant | — | private | `main` | — | Formerly frontend (renamed 2026-09-25). README only, no code. Created by abhishekyadav01 (not an org member). |
| [`wassup-patient-api`](https://github.com/Algorythmos-AI/wassup-patient-api) | service | dormant | — | private | `main` | — | Formerly patient-api (renamed 2026-09-25). README only (design notes), no code. Authored by abhishekyadav01. |
| [`wassup-authorize-api`](https://github.com/Algorythmos-AI/wassup-authorize-api) | service | dormant | — | private | `main` | — | Formerly authorize-api (renamed 2026-09-25). Auth0 token verification. Authored by abhishekyadav01. |
| [`wassup-encounters-api`](https://github.com/Algorythmos-AI/wassup-encounters-api) | service | dormant | — | private | `main` | — | Formerly encounters-api (renamed 2026-09-25). README only; never started. |
| [`wassup-scheduling-api`](https://github.com/Algorythmos-AI/wassup-scheduling-api) | service | dormant | — | private | `main` | — | Formerly scheduling-api (renamed 2026-09-25). main created 2026-09-25 from integration/scheduling-foundation (kept). |
| [`wassup-transcription-api`](https://github.com/Algorythmos-AI/wassup-transcription-api) | service | dormant | — | private | `main` | — | Formerly transcription-api (renamed 2026-09-25). Skeleton. |
| [`wassup-workflow-api`](https://github.com/Algorythmos-AI/wassup-workflow-api) | service | dormant | — | private | `main` | — | Formerly workflow-api (renamed 2026-09-25). Skeleton. |
| [`wassup-notification-api`](https://github.com/Algorythmos-AI/wassup-notification-api) | service | dormant | — | private | `main` | — | Formerly notification-api (renamed 2026-09-25). Skeleton. |
| [`wassup-messaging-api`](https://github.com/Algorythmos-AI/wassup-messaging-api) | service | dormant | — | private | `main` | — | Formerly messaging-api (renamed 2026-09-25). Skeleton. |
| [`wassup-documents-api`](https://github.com/Algorythmos-AI/wassup-documents-api) | service | dormant | — | private | `main` | — | Formerly documents-api (renamed 2026-09-25). Skeleton. |
| [`wassup-audit-api`](https://github.com/Algorythmos-AI/wassup-audit-api) | service | dormant | — | private | `main` | — | Formerly audit-api (renamed 2026-09-25). Append-only audit trail skeleton. |
| [`wassup-media-api`](https://github.com/Algorythmos-AI/wassup-media-api) | service | dormant | — | private | `main` | — | Formerly media-api (renamed 2026-09-25). Skeleton. |
| [`wassup-monolith`](https://github.com/Algorythmos-AI/wassup-monolith) | monorepo | dormant | — | private | `main` | — | Moved from personal account 2026-09-24. WASSUP modular monolith. |
| [`wassup-genesis`](https://github.com/Algorythmos-AI/wassup-genesis) | web | dormant | — | private | `main` | firebase | Moved from personal account 2026-09-24. |
| [`wassup-genesis-backend`](https://github.com/Algorythmos-AI/wassup-genesis-backend) | service | dormant | — | private | `main` | gcp-cloud-run | Moved from personal account 2026-09-24. Python engine + FastAPI on Cloud Run + Vertex AI Gemini. |
| [`wassup-genesis-platform`](https://github.com/Algorythmos-AI/wassup-genesis-platform) | docs | dormant | [clinical-data-platform.vercel.app](https://clinical-data-platform.vercel.app) | private | `main` | vercel | Vercel project `clinical-data-platform`. Moved from personal account 2026-09-24. Clinical briefing and investor materials. |
| [`wassup-dashboard`](https://github.com/Algorythmos-AI/wassup-dashboard) | web | dormant | — | private | `main` | — | Moved from personal account 2026-09-24. |
| [`wassup-meeting`](https://github.com/Algorythmos-AI/wassup-meeting) | app | active | [wassup-meeting.web.app](https://wassup-meeting.web.app) | private | `integration` | gcp-cloud-run, firebase | Moved from personal account 2026-09-24. Product name: Wassup Doc. |
| [`wassup-call-dashboard`](https://github.com/Algorythmos-AI/wassup-call-dashboard) | web | active | [wassup-secretary-app.web.app](https://wassup-secretary-app.web.app) | private | `main` | firebase-hosting, railway | Moved from personal account 2026-09-24. Hosted at wassup-secretary-app.web.app (historical Firebase site name; not the Secretary product). Backend on Railway since 2026-05-31. Git history contains a credential: never make this repository public. |

#### Agentic Armor

In development.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| _agentic-armor_ (no repo yet) | app | planned | — | private | — | — | Planned; no repository yet. |

#### Algorythmos company platform

Company website, document-processing API and its dashboard, docs and console.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`algorythmos-website`](https://github.com/Algorythmos-AI/algorythmos-website) | web | active | [algorythmos.com](https://algorythmos.com) | **public** → private | `master` | vercel | Public since 2026-09-25 (owner, D-009). algorythmos.com (Astro 7, EN/FR). Vercel project algorythmos-astro. Moved from personal account 2026-09-24. |
| [`algorythmos-api`](https://github.com/Algorythmos-AI/algorythmos-api) | service | active | [api.algorythmos.fr/docs](https://api.algorythmos.fr/docs) | private | `main` | vercel | 404 incident 2026-09-25 fixed by PR #17; Neon Postgres connected with migrations on production deploys (PR #19). Own ignoreCommand in vercel.json. api.algorythmos.fr live since 2026-09-25 (DNS added); pooled-connection fix PR #20. CI (the ci workflow) is green on main as of 2026-11-09; there is no Python Tests workflow any more. Open: about 120 tests are marked xfail, and the security workflow cannot start while Actions billing for private repos is failing. Moved from personal account 2026-09-24. Multi-tenant document-processing API (FastAPI). |
| [`algorythmos-docs`](https://github.com/Algorythmos-AI/algorythmos-docs) | docs | dormant | [docs-algorythmos.vercel.app](https://docs-algorythmos.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`algorythmos-ui`](https://github.com/Algorythmos-AI/algorythmos-ui) | web | dormant | [app.algorythmos.com](https://app.algorythmos.com) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`algorythmos-console`](https://github.com/Algorythmos-AI/algorythmos-console) | web | dormant | — | private | `main` | vercel | Moved from personal account 2026-09-24. Console for the document-processing API. |

#### Client: ICHR

International Coalition for Human Rights — trilingual (EN/AR/FR) newsroom.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`ichr-website`](https://github.com/Algorythmos-AI/ichr-website) | web | active | [www.ichr-international.org](https://www.ichr-international.org) | **public** → private | `integration` | vercel | ichr-international.org — the repo credits Algorythmos publicly. |
| [`ichr-ops`](https://github.com/Algorythmos-AI/ichr-ops) | ops | active | — | private | `main` | — | Security operations notes and pre-migration history. Never copy into the public repo. |

#### Client: Integrant

Integrant Pty Ltd internal document portal.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`integrant-portal`](https://github.com/Algorythmos-AI/integrant-portal) | web | dormant | — | private | `main` | — | Formerly data-room-portal (renamed 2026-09-25). Integrant's internal document portal, authored under an integrant.bio identity. Transferred 2026-09-24; ownership subject to the commercial agreement. |

#### Client websites

Marketing sites built for small-business and community clients.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`mazcina-website`](https://github.com/Algorythmos-AI/mazcina-website) | web | active | [mazcina.vercel.app](https://mazcina.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`mazcina-book`](https://github.com/Algorythmos-AI/mazcina-book) | web | active | — | private | `main` | vercel | Created 2026-10-12; catalogued 2026-11-09. Private back office for Mazcina Resto - Bar (recipe costing, menus; gift cards and inventory later), live at kitchen.mazcinarestobar.com.au. Next.js, Neon Postgres, Vercel (Sydney). No LICENSE file yet. |
| [`pdto-website`](https://github.com/Algorythmos-AI/pdto-website) | web | active | [www.pdto.org](https://www.pdto.org) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`src-website`](https://github.com/Algorythmos-AI/src-website) | web | active | [www.src-rural.org](https://www.src-rural.org) | private | `main` | vercel | Moved from personal account skalaliya/src and renamed 2026-09-27. integration → main. |
| [`regenu-website`](https://github.com/Algorythmos-AI/regenu-website) | web | active | [regenu-website.vercel.app](https://regenu-website.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`renovations-australia-website`](https://github.com/Algorythmos-AI/renovations-australia-website) | web | active | [renovations-australia.vercel.app](https://renovations-australia.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`acjr-website`](https://github.com/Algorythmos-AI/acjr-website) | web | active | [www.acjr.org](https://www.acjr.org) | public | `main` | vercel | Moved from personal account 2026-10-23. Trilingual FR/EN/AR (Astro). |
| [`cabinets-and-wardrobes-website`](https://github.com/Algorythmos-AI/cabinets-and-wardrobes-website) | web | active | [cabinetsandwardrobes.vercel.app](https://cabinetsandwardrobes.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`australians-care-website`](https://github.com/Algorythmos-AI/australians-care-website) | web | dormant | [www.australianscare.com.au](https://www.australianscare.com.au) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`pure-sydney-cleaning-website`](https://github.com/Algorythmos-AI/pure-sydney-cleaning-website) | web | dormant | [www.puresydneycleaning.com.au](https://www.puresydneycleaning.com.au) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`margaret-property-services-website`](https://github.com/Algorythmos-AI/margaret-property-services-website) | web | dormant | [margaret-property-services.vercel.app](https://margaret-property-services.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`elizabeth-cleaners-website`](https://github.com/Algorythmos-AI/elizabeth-cleaners-website) | web | dormant | [www.cleaningelizabeth.com.au](https://www.cleaningelizabeth.com.au) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`marigold-website`](https://github.com/Algorythmos-AI/marigold-website) | web | dormant | [marigold-international-society.vercel.app](https://marigold-international-society.vercel.app) | private | `main` | vercel | Moved from personal account 2026-09-24. |
| [`empowerwell-website`](https://github.com/Algorythmos-AI/empowerwell-website) | web | active | [empowerwellsupport.com.au](https://empowerwellsupport.com.au) | private | `main` | vercel | Moved from personal account 2026-11-07. Registered NDIS provider site (Astro 7, static). Live on empowerwellsupport.com.au (Vercel project empowerwell-website; DNS on Cloudflare, DNS only; www and the vercel.app domain 308 to the apex). |

#### Vision On Care

Archived March 2026 prototype of an operations platform for NDIS-style disability-support providers. Algorythmos IP, imported from the visiononcare org on 2026-09-25 and archived (read-only).

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`visiononcare-web`](https://github.com/Algorythmos-AI/visiononcare-web) | web | archived | [vison-on-care-frontend.vercel.app](https://vison-on-care-frontend.vercel.app) | private | `main` | vercel | Formerly visiononcare/frontend. The only substantial Vision On Care code: React + Vite front end with mock-backed workflows. Vercel project vison-on-care-frontend (spelling as created) still serves the last build. Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-worker-mobile`](https://github.com/Algorythmos-AI/visiononcare-worker-mobile) | app | archived | — | private | `main` | — | Formerly visiononcare/worker-mobile. Created empty; never started. Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-api-gateway`](https://github.com/Algorythmos-AI/visiononcare-api-gateway) | service | archived | — | private | `main` | — | Formerly visiononcare/api-gateway. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-tenant-service`](https://github.com/Algorythmos-AI/visiononcare-tenant-service) | service | archived | — | private | `main` | — | Formerly visiononcare/tenant-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-participant-service`](https://github.com/Algorythmos-AI/visiononcare-participant-service) | service | archived | — | private | `main` | — | Formerly visiononcare/participant-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-worker-service`](https://github.com/Algorythmos-AI/visiononcare-worker-service) | service | archived | — | private | `main` | — | Formerly visiononcare/worker-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-roster-service`](https://github.com/Algorythmos-AI/visiononcare-roster-service) | service | archived | — | private | `main` | — | Formerly visiononcare/roster-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-notes-service`](https://github.com/Algorythmos-AI/visiononcare-notes-service) | service | archived | — | private | `main` | — | Formerly visiononcare/notes-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-funding-service`](https://github.com/Algorythmos-AI/visiononcare-funding-service) | service | archived | — | private | `main` | — | Formerly visiononcare/funding-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-pricing-service`](https://github.com/Algorythmos-AI/visiononcare-pricing-service) | service | archived | — | private | `main` | — | Formerly visiononcare/pricing-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-invoice-service`](https://github.com/Algorythmos-AI/visiononcare-invoice-service) | service | archived | — | private | `main` | — | Formerly visiononcare/invoice-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-document-service`](https://github.com/Algorythmos-AI/visiononcare-document-service) | service | archived | — | private | `main` | — | Formerly visiononcare/document-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-reporting-service`](https://github.com/Algorythmos-AI/visiononcare-reporting-service) | service | archived | — | private | `main` | — | Formerly visiononcare/reporting-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-audit-service`](https://github.com/Algorythmos-AI/visiononcare-audit-service) | service | archived | — | private | `main` | — | Formerly visiononcare/audit-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |
| [`visiononcare-notification-service`](https://github.com/Algorythmos-AI/visiononcare-notification-service) | service | archived | — | private | `main` | — | Formerly visiononcare/notification-service. FastAPI scaffold only (identical across the 13 service repos, no business logic). Imported and archived 2026-09-25 (D-013). |

#### Trading Lab

Stocks and options paper-trading research — the stocks desk, the options workstation and the status dashboard, plus the original knowledge-base pipeline. Becomes Options Lab when its repo is renamed (D-026); see docs/trading-platforms.md.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`trading-lab`](https://github.com/Algorythmos-AI/trading-lab) | monorepo | active | — | private | `main` | — | Code-only history split from skalaliya/trading 2026-09-28 (source PDFs, extracts and local paths filtered out). Paper trading only; runs locally. Private on GitHub as found 2026-10-05 (the catalog said public). |
| [`trading-lab-source`](https://github.com/Algorythmos-AI/trading-lab-source) | data | active | — | private | `main` | — | Moved from personal account skalaliya/trading and renamed 2026-09-28. Non-redistributable KB source for trading-lab (KB_SOURCE_ROOT); see NOTICE.md. |
| [`trading-lab-research`](https://github.com/Algorythmos-AI/trading-lab-research) | monorepo | active | — | private | `integration` | vercel, gcp | Created 2026-09-28. Research engine (wt package), strategy registry, and two paper desks: stocks (Alpaca paper account) and crypto (Kraken public data on the lab's own simulator, live 2026-10-04). Jobs run on a GCP VM since 2026-10-01. The status dashboard (dashboard/, lab.algorythmos.com) deploys to Vercel project trading-lab-dashboard as prebuilt output from GitHub Actions (no Git integration, so Vercel never clones the repo); Vercel Authentication on all deployments; it publishes sanitized snapshots only, never restricted content (its ADR 0001). D-026 (2026-10-10): this becomes the stocks and options platform; the crypto desk moves to crypto-lab, after which the owner renames this repo options-lab. Until then the status dashboard here keeps showing every desk. |
| [`trading-lab-kraken-bot`](https://github.com/Algorythmos-AI/trading-lab-kraken-bot) | service | archived | — | private | `main` | — | Formerly skalaliya/kraken. The original Kraken spot paper-trading bot (TypeScript, Apr 2026); never held live keys. Rebuilt as the crypto desk in trading-lab-research. Transferred, renamed and archived 2026-10-05 (D-025). |
| [`trading-lab-docs`](https://github.com/Algorythmos-AI/trading-lab-docs) | docs | active | — | private | `main` | vercel | Created 2026-10-12. One documentation site for the trading platforms (stocks and options, crypto, forex HFT) and the shared knowledge base: what is built, how it runs, where each stands and the roadmap, with design records and runbooks copied from each repository at a recorded commit. Served at docs.algorythmos.com (sign-in required, so no url here) from Vercel project trading-lab-docs through the Git integration, with Vercel Authentication on all deployments. Runs no Actions: pnpm check and a pre-push hook are the gate. Holds no specification text, research prose or knowledge-base text. algorythmos-docs (the document-processing product's docs) is a separate repository. |
| [`trading-focus-card-ledger`](https://github.com/Algorythmos-AI/trading-focus-card-ledger) | data | active | — | **public** → private | `main` | — | Created 2026-10-28; catalogued 2026-11-09. Renamed from focus-card-ledger on 2026-11-16 to carry the trading prefix (GitHub redirects the old name). Pre-registered Top 4 Focus Card predictions committed before the open, scored after the close against broker bars; sends the Card record page of the trading-lab-research dashboard. Research only: places and suggests no orders. Holds market data, so never public. |

#### HFT Lab

High-frequency paper trading for the currency (forex) market — records its own tick data, trades on a broker paper account and retrains its models every week.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`hft-lab`](https://github.com/Algorythmos-AI/hft-lab) | monorepo | active | — | private | `main` | — | Created 2026-10-10 (D-026). High-frequency paper trading for the currency market on a broker paper account. The code of every planned phase is in the repository and tested against a deterministic fake broker and synthetic data: the paper-only lock, the broker adapter and capability probe, the tick recorder and replay, a shadow venue with an explicit cost model, the risk gate, the order manager with a write-ahead outbox, reconciliation, the trader with staged rollout, the control, Directional Change and ML sleeves, ridge and gradient-boosted models, the weekly learning loop with promotion and rollback, reports, a deploy gate, backups, and the status snapshot contract the dashboard vendors. Nothing is installed on a host, nothing has been recorded from the real feed and nothing has traded: every phase gate past the foundation is open and needs days on the host. The capability probe reached the real paper gateway on 2026-10-11 (weekend, no quotes yet). Paper only: the adapter cannot reach a live account. Will run on the shared GCP VM under its own user and unit prefix. Branch rule since 2026-10-11: main takes only pull requests with test and leakcheck green. |

#### Crypto Lab

Crypto paper-trading desk on public market data and the lab's own simulator, with its learning loop. Closed on 2026-10-24 (trading-lab-research DEC-0036) and never cut over; archived.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`crypto-lab`](https://github.com/Algorythmos-AI/crypto-lab) | monorepo | archived | — | private | `main` | — | Created 2026-10-11 (D-026) by a repeatable scripted extraction from trading-lab-research. Never cut over: the crypto desk was closed on 2026-10-24 by trading-lab-research DEC-0036 (every registered rule failed gate C1), its jobs removed from the host the same day, and this repository archived as the extraction of 2026-10-11. |

#### Trading Knowledge Base

Shared, licence-restricted knowledge base for the three trading platforms — sources, extracts and verified claim cards, one collection per platform.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`trading-kb`](https://github.com/Algorythmos-AI/trading-kb) | data | active | — | private | `main` | — | Created 2026-10-10 (D-026); runs no Actions. One knowledge base shared by the three trading platforms: sources, page extracts, verified claim cards and syntheses, one collection per platform, plus its own tooling. First collection: the owner's HFT study folder. trading-lab-source stays the stocks course-material store until it is folded in as a collection. |

#### PDF Algo Pro

Native PDF reader, editor and scanner for iPhone, iPad and Mac with private, on-device document intelligence.

| Repo | Kind | Status | Live at | Visibility | Default branch | Ships to | Notes |
|---|---|---|---|---|---|---|---|
| [`pdf-algo-pro`](https://github.com/Algorythmos-AI/pdf-algo-pro) | app | planned | — | **public** → private | `integration` | testflight, app-store | Renamed from PDF-Algo-Pro 2026-09-28. Planning phase: no app code until its readiness gate clears. integration -> main branch model is a recorded exception for an app (D-023). Business documents live in pdf-algo-pro-private. |
| [`pdf-algo-pro-private`](https://github.com/Algorythmos-AI/pdf-algo-pro-private) | docs | planned | — | private | `main` | — | Created 2026-09-28. Confidential editions of the business documents whose redacted editions are in pdf-algo-pro (naming shape <name>-private, D-024). |
| [`pdf-algo-pro-test-history`](https://github.com/Algorythmos-AI/pdf-algo-pro-test-history) | data | active | — | private | `main` | — | Created 2026-10-28; catalogued 2026-11-09. Every PDF Algo Pro test run (CI and iPhone) kept as data for queries and backtesting (tools/query.py). The public app repository never links it. |

### Rename backlog (in-org)

Generic names that collide across products. Rename only with explicit approval; GitHub keeps a redirect as long as the old name is never reused.

| Current | Proposed |
|---|---|
| [`trading-lab-research`](https://github.com/Algorythmos-AI/trading-lab-research) | `options-lab` |

### Temporarily public

Public today for free Actions compute; intended private. Don't link these from public pages. If a README or `NOTICE.md` here says "keep this repository private", that is the intended end state (D-002), not a mistake.

- [`gurbani-soul-ios`](https://github.com/Algorythmos-AI/gurbani-soul-ios) — public data
- [`sggs-platform`](https://github.com/Algorythmos-AI/sggs-platform) — restricted data
- [`sggs-data`](https://github.com/Algorythmos-AI/sggs-data) — restricted data
- [`algominutes`](https://github.com/Algorythmos-AI/algominutes) — confidential data
- [`wassup-secretary`](https://github.com/Algorythmos-AI/wassup-secretary) — confidential data
- [`trading-focus-card-ledger`](https://github.com/Algorythmos-AI/trading-focus-card-ledger) — confidential data. Public on GitHub as found 2026-11-16, the day of the rename; private before. The catalog said never public because it holds market data, so the owner decides whether it stays public until go-private.
- [`pdf-algo-pro`](https://github.com/Algorythmos-AI/pdf-algo-pro) — internal data. Temporarily public for Actions compute (D-002); back to private per go-private.md
- [`algorythmos-website`](https://github.com/Algorythmos-AI/algorythmos-website) — internal data. Public on purpose since 2026-09-25 (D-009); the owner decides at go-private time whether it stays public
- [`ichr-website`](https://github.com/Algorythmos-AI/ichr-website) — public data
<!-- catalog:end -->
