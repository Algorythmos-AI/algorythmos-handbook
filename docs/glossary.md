# Glossary

Terms you will meet in repo names, READMEs and CI logs. Product and repo names are in `code`.

## Company

| Term | Meaning |
|---|---|
| **Algorythmos** | Algorythmos Pty Ltd, Sydney (ACN 701 006 626). Owns this GitHub org and every repo in it. One director/owner: Sameer Raj Kalaliya, [@skalaliya](https://github.com/skalaliya) — "Sam" in some READMEs. |
| **Agentic Armor** | A planned Algorythmos product. No repository yet. |
| **BitePerk** | BitePerk Pty Ltd, a **separate company** with its own GitHub org (`biteperk`). Never share code, secrets or Apple IDs with it. |
| **Document-intelligence platform** | Algorythmos's own document-processing product: `algorythmos-api` (FastAPI; live at api.algorythmos.fr, maintained — fixes in Sep 2026), `algorythmos-ui` (dashboard at app.algorythmos.com), `algorythmos-docs`, `algorythmos-console`. The UI, docs and console are dormant since Feb 2026. |
| **Data class** | The most sensitive data a repo holds, set per repo in the catalog: **public** (fine to publish), **internal** (company code, nothing personal), **confidential** (client or business data, commercial terms), **restricted** (licence-restricted content, e.g. the scripture translation layer, or personal data; tightest handling). Shown on the member homepage as "… data". |
| **Flagship repos** | The six actively developed repos with their own README format and stricter rulesets: `gurbani-soul-ios`, `sggs-platform`, `sggs-data`, `algominutes`, `wassup-secretary`, `ichr-website`. Every other repo opens with the standard header. |
| **Plan v5** | The 25 Sep 2026 org clean-up plan (phases A–F) that produced this structure. Decisions it made are marked "Agent (plan v5)" in the [decision log](decisions.md). Its last step, making repos private, waits for the owner ([`go-private.md`](go-private.md)). |
| **Catalog** | [`catalog.yaml`](../catalog.yaml) in this repo: the single source of truth for what each repo is. The member homepage's repo map is generated from it. |
| **Custom properties** | GitHub repo metadata (`product`, `kind`, `lifecycle`, `client`, …) set from the catalog. Filter the repo list with `props.product:wassup`. |
| **`maintainers`** | The org team that owns every repo and is the `CODEOWNERS` target. Currently one person. |
| **Temporarily public** | A repo that is public today only for free GitHub Actions compute and is intended to become private. Listed at the bottom of the member homepage. Never link one from a public page. |

## Gurbani Soul (scripture product)

| Term | Meaning |
|---|---|
| **Gurbani Soul** | The consumer product: Sri Guru Granth Sahib Ji on iPhone/iPad (`gurbani-soul-ios`) and the web (gurbanisoul.com, served from `sggs-platform`). |
| **SGGS** | **S**ri **G**uru **G**ranth **S**ahib, the central scripture of Sikhism. The `sggs-*` repos are the data platform behind Gurbani Soul; they keep the short name because two lock files pin `Algorythmos-AI/sggs-data` by name. |
| **Gurbani** | The scripture's text ("the Guru's word"). In this org it is always verbatim, never edited or "corrected". |
| **Ang** | A page of the Granth (1,430 Angs). Every line the apps show is cited by Ang. |
| **Nitnem** | The daily prayers; the iOS app has a Nitnem reader with reminders. |
| **Hukam** | A randomly opened passage read as guidance; a feature of the app. |
| **Raag** | The musical mode a composition is set in; the app has a "raag clock". |
| **Corpus / dataset** | `corpus/sggs.jsonl` (the text) and `db/sggs.sqlite` (the searchable database) in `sggs-data`. |
| **Dataset pin** | `dataset.lock.json` in a consuming repo: the exact `sggs-data` commit plus the database's sha256. Consumers refuse a database that doesn't match. |
| **Editorial ledger** | `audit/editorial-ledger.jsonl` in `sggs-data`: the only sanctioned way scripture text ever changes, with review. CI rejects any other change. |
| **Golden contract** | `contract/` in `sggs-platform`: fixed request/response pairs that the API and the iOS search core must both satisfy byte for byte (`make parity`). |
| **`sggs-source`** | Private archive of the source PDF and licence-restricted translation files, as GitHub Releases. Never public. |

## AlgoMinutes

| Term | Meaning |
|---|---|
| **AlgoMinutes** | AI meeting recorder: native iOS/Android capture, web review; transcripts with speaker labels, structured minutes, action items. Monorepo `algominutes`. |

## WASSUP (clinic products)

| Term | Meaning |
|---|---|
| **WASSUP** | The brand for Algorythmos's clinic-facing AI products. Algorythmos holds the platform and IP; see [`ownership.md`](ownership.md) for the commercial status with Integrant. |
| **WASSUP Secretary** | Multi-clinic AI phone receptionist: a voice agent answers calls; staff handle calls, messages and callbacks in a dashboard. Repo `wassup-secretary`. Active development. |
| **Wassup Doc** | Product name of `wassup-meeting`: records clinical meetings (iOS or web), transcribes (Google STT), summarises and extracts actions (Vertex Gemini). Live at wassup-meeting.web.app. |
| **WASSUP call dashboard** | `wassup-call-dashboard`: analytics for calls handled by Retell AI; Firebase Hosting front end, Railway API + Postgres. Live at wassup-secretary-app.web.app (a historical Firebase site name; it is *not* the Secretary product). |
| **WASSUP Genesis** | A May 2026 prototype family for Integrant: a translational-medicine decision engine (`wassup-genesis-backend`), a demo web app (`wassup-genesis`) and a briefing deck (`wassup-genesis-platform`). Not developed since. |
| **WASSUP monolith** | `wassup-monolith`: a March 2026 modular-monolith orthopaedic practice platform (React web + Fastify API). Not developed since. |
| **Service skeletons** | `wassup-*-api` repos created Mar–Apr 2026 as placeholders for a microservice split (audit, documents, media, messaging, notification, transcription, workflow, scheduling, encounters). Most contain only a README, `LICENSE` and `.gitignore`; none has a running service. See [`wassup-product-map.md`](wassup-product-map.md). |
| **Retell AI** | Third-party voice-agent platform. The voice agents answering clinic calls today are configured in Retell itself (no repo holds them); their call webhooks feed `wassup-call-dashboard`. `wassup-secretary` is Algorythmos's own receptionist, in staging. |

## Clients and sister orgs

| Term | Meaning |
|---|---|
| **ICHR** | International Coalition for Human Rights, a Geneva-based NGO. Algorythmos builds and operates its trilingual newsroom site (`ichr-website`, public) and keeps ops notes in `ichr-ops` (private). |
| **Integrant** | Integrant Pty Ltd, a biotech client. Its GitHub org `integrant-biotechnology` keeps three repos; `integrant-portal` (its internal document portal) and the WASSUP repos it hosted moved here on 24 Sep 2026. |
| **PDTO** | Organization for Peace and Democratic Transition; client website `pdto-website` (pdto.org). |
| **SRC** | Sudanese Rural Community, a Paris-based nonprofit working in Sudan; client website `src-website` (src-rural.org). |
| **Vision On Care** | A March 2026 prototype of an operations platform for NDIS-style disability-support providers. Algorythmos IP. Imported on 25 Sep 2026 as the 15 `visiononcare-*` repos and **archived** (read-only): `visiononcare-web` is the only substantial code; the 13 `*-service` repos are identical FastAPI scaffolds. |
| **`wassup-pm`** | A previous, unneeded project org (Plane self-host, gateway, inventory service). Not catalogued. Backed up 25 Sep 2026; the owner deletes it (D-014). |
| **Client websites** | Marketing sites built for small businesses and community groups (`*-website` repos). Algorythmos owns the code. |

## Infrastructure

| Term | Meaning |
|---|---|
| **Vercel** | Hosts the company website, the Gurbani Soul web app and its production API functions, the document-intelligence apps and all client websites. Team `skalaliya's projects` (Pro). |
| **Render** | Runs the Gurbani Soul single-process API `sggs-knowledge-base.onrender.com`, kept as the **rollback**. Production search runs as Vercel functions inside the gurbanisoul.com web project. |
| **Firebase Hosting / Auth** | Hosts Wassup Doc and the call dashboard front ends. |
| **Cloud Run / Vertex AI** | Google Cloud: backend containers and Gemini models used by AlgoMinutes and Wassup Doc. |
| **Railway** | Hosts the call dashboard's API and Postgres (since 31 May 2026) and `wassup-secretary` staging. |
| **`integration` → `main`** | Branch model for deployed web platforms: `integration` is staging, `main` is production; releases are PRs from one to the other. Apps and data repos use `main` only. |
| **Archived** | A read-only repo (GitHub's archive flag): kept for history, never changed. Catalog `lifecycle: archived`; `make validate` checks the flag matches. To change one: unarchive, change, re-archive, with owner approval. Today only the `visiononcare-*` repos are archived; dormant WASSUP repos are deliberately *not* (D-011). |
| **Ruleset** | GitHub branch protection. Flagship repos have their own; an org ruleset blocks force-push and deletion on every default branch. |
