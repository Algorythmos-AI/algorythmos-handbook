# Architecture — how the repos fit together

One diagram per product. Boxes are repos; cylinders are where things run. Facts come from each
repo's workflows, `vercel.json`/`render.yaml` and lock files (re-read those files rather than
trusting memory). Live URLs are the ones that answered 200 on 25 Sep 2026.

## Gurbani Soul

```mermaid
flowchart LR
  src[("sggs-source<br/>private · source PDF + translation files<br/>GitHub Releases")]
  data[("sggs-data<br/>verbatim corpus + SQLite/FTS5 dataset<br/>editorial ledger · integrity proofs")]
  plat["sggs-platform<br/>search API + study web app<br/>golden contract"]
  ios["gurbani-soul-ios<br/>iPhone / iPad app (SwiftUI)"]
  api[("Render<br/>sggs-knowledge-base.onrender.com<br/>rollback API")]
  web[("Vercel<br/>gurbanisoul.com<br/>web app + production API functions")]
  store[("TestFlight / App Store")]
  src -- "rebuild only" --> data
  data -- "dataset.lock.json<br/>commit + sha256" --> plat
  data -- "dataset.lock.json<br/>+ vendor.lock.json: iOS DB builder" --> ios
  plat -- "vendor.lock.json<br/>golden contract" --> ios
  plat -. rollback .-> api
  plat --> web
  ios --> store
```

- **Trust chain:** `sggs-data` publishes one database per commit; consumers refuse a database whose
  sha256 doesn't match their pin. The iOS app's search core must match the API byte for byte
  (`make parity`). Scripture text changes only through the editorial ledger.
- **Branches:** `sggs-platform` uses `integration` → `main`; `sggs-data` and `gurbani-soul-ios` use
  `main` with release tags.
- **Cross-repo reads in CI** use `secrets.SGGS_READ_TOKEN || github.token`, so the data repos can go
  private later without code changes ([`go-private.md`](go-private.md)).

## WASSUP

```mermaid
flowchart TB
  subgraph live["Live / active (2026)"]
    sec["wassup-secretary<br/>voice-gateway · core-api · ops-worker<br/>multi-clinic AI phone receptionist"]
    doc["wassup-meeting = Wassup Doc<br/>iOS + web · Google STT · Vertex Gemini"]
    cd["wassup-call-dashboard<br/>Retell AI call analytics"]
    fbdoc[("Firebase Hosting<br/>wassup-meeting.web.app")]
    run[("Cloud Run · Vertex AI")]
    fbcd[("Firebase Hosting<br/>wassup-secretary-app.web.app")]
    rail[("Railway<br/>API + Postgres")]
    retell(("Retell AI<br/>webhooks"))
    doc --> fbdoc
    doc --> run
    cd --> fbcd
    cd --> rail
    retell --> rail
  end
  subgraph mono["Monolith (Mar 2026, dormant)"]
    m["wassup-monolith<br/>React web + Fastify API<br/>orthopaedic practice platform"]
  end
  subgraph gen["Genesis prototypes (May 2026, dormant)"]
    gb["wassup-genesis-backend<br/>FastAPI · Cloud Run · Vertex Gemini"]
    gw["wassup-genesis<br/>demo web app (AI Studio)"]
    gp["wassup-genesis-platform<br/>briefing deck · architecture doc"]
    gv[("Vercel<br/>clinical-data-platform.vercel.app")]
    gw --> gb
    gp --> gv
  end
  subgraph skel["Integrant-era service skeletons (Mar–Apr 2026, dormant)"]
    s1["wassup-web · wassup-patient-api · wassup-authorize-api"]
    s2["wassup-scheduling-api · wassup-transcription-api · wassup-workflow-api"]
    s3["wassup-notification-api · wassup-messaging-api · wassup-documents-api"]
    s4["wassup-audit-api · wassup-media-api · wassup-encounters-api (never started)"]
    dash["wassup-dashboard (AI Studio prototype)"]
  end
```

- There is **no dependency** between the four generations; each was a fresh start. Only the top group
  is deployed. The generation table with dates and commit counts is in
  [`wassup-product-map.md`](wassup-product-map.md).
- Naming trap: the call dashboard is hosted at `wassup-secretary-app.web.app` for historical reasons.
  It is not the Secretary product.
- `wassup-secretary` deploys by script, not by workflow: `integration` goes to Railway staging by exact commit
  (`scripts/deploy-railway.sh`); production runs only `v*` tags on `main` (its `docs/runbooks/release.md`).

## Algorythmos company platform

```mermaid
flowchart LR
  site["algorythmos-website<br/>Astro 7 · EN/FR"]
  api["algorythmos-api<br/>FastAPI document-processing API"]
  ui["algorythmos-ui<br/>Next.js dashboard"]
  docs["algorythmos-docs<br/>Next.js + Nextra"]
  con["algorythmos-console<br/>Next.js console (not deployed)"]
  v1[("Vercel algorythmos-astro<br/>algorythmos.com · .com.au · .fr")]
  v2[("Vercel api-algorythmos<br/>api.algorythmos.fr")]
  v3[("Vercel ui-algorythmos<br/>app.algorythmos.com")]
  v4[("Vercel docs-algorythmos<br/>docs-algorythmos.vercel.app")]
  site --> v1
  api --> v2
  ui --> v3
  docs --> v4
  ui -- "calls" --> api
  con -- "calls" --> api
```

- Working hosts (checked 25 Sep 2026): `api.algorythmos.fr` (DNS added 25 Sep) and `app.algorythmos.com`.
  `app.` and `docs.algorythmos.fr`, and `api.`/`docs.algorythmos.com`, have **no DNS records**; use
  `docs-algorythmos.vercel.app` for the docs. Every project also answers on its `*.vercel.app` URL.
- `algorythmos-api` uses Neon Postgres and runs migrations on production deploys (its PR #19).
  See its catalog note for open items.

## Trading Lab

Paper-trading research: a knowledge base over trading literature plus a guarded gap-and-go
pipeline against an Alpaca **paper** account. Runs locally; nothing is deployed. Order submission
is frozen until its risk-control milestone lands (trading-lab ADR-0001).
The research engine (`trading-lab-research`) holds the `wt` package, the strategy registry
(hypotheses, experiments, decisions) and a paper runner scheduled by launchd. It tests
course-derived rules, so it is restricted and never public.

```mermaid
flowchart LR
  src["trading-lab-source (private, restricted)<br/>third-party PDFs · chunks · notes"] -- "KB_SOURCE_ROOT (local only)" --> kb["trading-lab<br/>ingest → SQLite FTS5 → search"]
  kb --> run["scheduled agent run<br/>scan → account → guard (dry-run) → log"]
  run --> alpaca["Alpaca paper API"]
  run --> dec["decisions/ run logs"]
  res["trading-lab-research (private, restricted)<br/>wt engine · registry · specs"] -- "paper runner + forward test (launchd)" --> alpaca
```

| Repo | Holds | Visibility |
|---|---|---|
| `trading-lab` | Code, prompts, run logs, `docs/` wiki and ADRs, backlog source | Public for now, intended private |
| `trading-lab-source` | The licence-restricted source publications and text extracted from them | Private, never public |
| `trading-lab-research` | Research engine (`wt`), strategy registry, specifications, paper runner | Private, never public |

## Client websites

| Repo | Client | Live | Stack | Vercel project |
|---|---|---|---|---|
| `ichr-website` (public) | International Coalition for Human Rights | www.ichr-international.org | Astro + Prisma/Neon, `integration` → `main` | `ichr` |
| `pdto-website` | PDTO | www.pdto.org | Vite + React | `pdto-org` |
| `src-website` | Sudanese Rural Community (SRC) | www.src-rural.org | Next.js + Payload CMS/Neon, `integration` → `main` | `src` |
| `australians-care-website` | Australians Care | www.australianscare.com.au | Vite + React | `australians-care` |
| `pure-sydney-cleaning-website` | Pure Sydney Cleaning | www.puresydneycleaning.com.au | React | `pure-sydney-cleaning` |
| `elizabeth-cleaners-website` | Elizabeth Cleaners | www.cleaningelizabeth.com.au | Vite + React | `elizabeth-cleaners` |
| `mazcina-website` | Mazcina | mazcina.vercel.app | Astro | `mazcina` |
| `renovations-australia-website` | Renovations Australia | renovations-australia.vercel.app (renovationsaustralia.com.au has no DNS) | Astro | `renovations-australia` |
| `cabinets-and-wardrobes-website` | Cabinets & Wardrobes | cabinetsandwardrobes.vercel.app | Astro | `cabinetsandwardrobes` |
| `regenu-website` | RegenU | regenu-website.vercel.app | static HTML | `regenu-website` |
| `margaret-property-services-website` | Margaret Property Services | margaret-property-services.vercel.app | Vite + React | `margaret-property-services` |
| `marigold-website` | Marigold International Society | marigold-international-society.vercel.app | Vite + React | `marigold-international-society` |
| `integrant-portal` | Integrant Pty Ltd | not deployed from this org | Next.js | — |

Every site auto-deploys production from its default branch. Docs-only commits (`README.md`,
`LICENSE`, `.github/CODEOWNERS`, `.github/dependabot.yml`) are skipped by each project's Ignored
Build Step (decision D-018):

```sh
if [ -n "$VERCEL_GIT_PREVIOUS_SHA" ] && git diff --quiet "$VERCEL_GIT_PREVIOUS_SHA" HEAD -- . ":(exclude)README.md" ":(exclude)LICENSE" ":(exclude).github/CODEOWNERS" ":(exclude).github/dependabot.yml" 2>/dev/null; then exit 0; else exit 1; fi
```

It must only ever exit 0 (skip) or 1 (build); Vercel fails the deployment on any other code. Anything
uncertain (first deploy, previous commit missing from the shallow clone, `.git` stripped by
`.vercelignore`) builds. A `vercel.json` `ignoreCommand` in a repo overrides the dashboard setting;
`algorythmos-api` has its own (`scripts/vercel_ignore.sh`).

## Vision On Care (archived)

A March 2026 prototype, imported and archived on 25 Sep 2026 (decision D-013). Nothing here is
developed; read it for history only.

- `visiononcare-web` — the only substantial code: React + Vite front end with mock-backed workflows
  (participants, workers, shifts, notes, funding, invoices). Vercel project `vison-on-care-frontend`
  (spelling as created) still serves the last build at vison-on-care-frontend.vercel.app.
- `visiononcare-api-gateway` and 12 `visiononcare-*-service` repos — identical FastAPI scaffolds
  (about 1 KB of code each, two commits); never implemented.
- `visiononcare-worker-mobile` — created empty; never started.

## Org plumbing

```mermaid
flowchart LR
  cat["catalog.yaml"] -- "make render" --> home["member homepage"]
  cat -- "make properties" --> props["repo custom properties"]
  cat -- "make validate (weekly CI)" --> gh["live GitHub state"]
  pub[".github (public)<br/>profile · CONTRIBUTING · SECURITY · templates"] --> strangers["anyone"]
  home --> members["org members + agents"]
```
