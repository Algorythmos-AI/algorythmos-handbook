# WASSUP product map

WASSUP is one brand with four generations of code. Nothing in an older generation is used by a
newer one; each was a fresh start. If you're new: **only the first table is live.** The rest is kept
for history (owner decision 25 Sep 2026: label, don't archive).

Commit counts and dates are as at 25 Sep 2026, before that week's housekeeping commits
(licences, README headers).

## Live / active

| Repo | What it is | Status | Runs at | Commits | Last real commit |
|---|---|---|---|---|---|
| `wassup-secretary` | Multi-clinic AI phone receptionist: voice gateway, core API, ops worker, shared `wassup_core` lib, Alembic migrations | **Active** (created 24 Sep 2026; temporarily public) | not deployed yet | 36 | Sep 2026 |
| `wassup-meeting` (product: **Wassup Doc**) | Clinical meeting recorder + AI summariser: iOS app + web; Google STT v2; Vertex Gemini | **Live** (clinical alpha) | wassup-meeting.web.app · Cloud Run | 100+ | 2026-09-07 |
| `wassup-call-dashboard` | Call analytics for Retell AI voice agents; Firebase Hosting + Auth front end, Railway API + Postgres | **Live** | wassup-secretary-app.web.app | 100+ | 2026-07-13 |

## Monolith (March 2026)

| Repo | What it is | Status | Commits | Last real commit |
|---|---|---|---|---|
| `wassup-monolith` | Modular-monolith orthopaedic practice platform: React/Vite staff shell + patient portal, Fastify API, AI orchestration ("Phase 4 / 5B") | Dormant, not deployed | 15 | 2026-03-10 |

## Genesis prototypes (May 2026, built for Integrant)

| Repo | What it is | Status | Commits | Last real commit |
|---|---|---|---|---|
| `wassup-genesis-backend` | Translational-medicine decision engine: FastAPI on Cloud Run, Vertex Gemini | Dormant | 28 | 2026-05-25 |
| `wassup-genesis` | Demo web app for the above (AI Studio scaffold, Firebase) | Dormant | 19 | 2026-05-24 |
| `wassup-genesis-platform` | Static briefing deck + one-pager + architecture document | Dormant; still served at clinical-data-platform.vercel.app | 4 | 2026-05-25 |

## Integrant-era service skeletons (March–April 2026)

Created as placeholders for a microservice split that never proceeded. Three were written by an
external contributor (`abhishekyadav01`) and have a `pending` licence decision.

| Repo | What it is | Status | Commits | Last real commit |
|---|---|---|---|---|
| `wassup-web` | Web front-end placeholder (README says "frontend") | Skeleton | 1 | 2026-03-10 |
| `wassup-patient-api` | Patient enrolment API; early RAG experiment | Skeleton | 1 | 2026-03-10 |
| `wassup-authorize-api` | Auth0 token verification, roles → permissions | Skeleton with working code | 1 | 2026-03-20 |
| `wassup-scheduling-api` | FastAPI scheduling foundation (contracts only) | Skeleton | 3 | 2026-03-27 |
| `wassup-transcription-api` | Placeholder | Skeleton | 4 | 2026-03-26 |
| `wassup-workflow-api` | Placeholder | Skeleton | 4 | 2026-03-26 |
| `wassup-notification-api` | Placeholder | Skeleton | 6 | 2026-03-26 |
| `wassup-messaging-api` | Placeholder | Skeleton | 5 | 2026-03-26 |
| `wassup-documents-api` | Placeholder | Skeleton | 4 | 2026-03-26 |
| `wassup-audit-api` | Placeholder | Skeleton | 5 | 2026-03-26 |
| `wassup-media-api` | Placeholder | Skeleton | 4 | 2026-03-26 |
| `wassup-encounters-api` | Empty repository | Never started | 0 | — |
| `wassup-dashboard` | AI Studio scaffold | Prototype, never developed | 3 | 2026-03-12 |

## Related but not WASSUP code

- `integrant-portal` — Integrant's internal document portal (feeds "Wassup AI"); a client system, catalogued under Integrant.
- The `wassup-pm` org — a previous project (Plane self-host, gateway, inventory service). Not needed; backed up 25 Sep 2026 and scheduled for deletion by the owner.

## Commercial note

Algorythmos's position is that it owns the WASSUP platform and IP while WASSUP remains the customer-
facing brand; a subscription-licence arrangement with Integrant was proposed and not yet agreed as at
25 Sep 2026. See [`ownership.md`](ownership.md) and [`decisions.md`](decisions.md).
