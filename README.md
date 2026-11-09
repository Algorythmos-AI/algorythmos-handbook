# Algorythmos-AI/algorythmos-handbook

Members-only. The org's source of truth: the repository catalog, agent rules, decisions and
standards. Moved here from `.github-private` on 2026-11-09 (D-027) so that people and agents can
read it like any other repository.

`.github-private` now holds only `profile/README.md`, the member homepage GitHub shows at
github.com/Algorythmos-AI. The public face is [`Algorythmos-AI/.github`](https://github.com/Algorythmos-AI/.github).

| Path | What it is |
|---|---|
| `catalog.yaml` | The single source of truth for every Algorythmos repo |
| `docs/repository-map.md` | The repo map, generated from the catalog; don't edit it by hand |
| `AGENTS.md` | Rules for AI agents across all Algorythmos repos |
| `docs/decisions.md` | Why things are the way they are (D-001 onwards) |
| `docs/naming.md` · `docs/ownership.md` · `docs/onboarding.md` | Standards, owners, first-day guide |
| `docs/architecture.md` · `docs/glossary.md` · `docs/wassup-product-map.md` | How the repos connect, terms, which WASSUP repo is live |
| `docs/go-private.md` | Runbook for making every repo private |
| `docs/trading-platforms.md` | The three trading platforms, their shared knowledge base and the rules that keep them apart |
| `docs/model-policy.md` | Which model and effort level agents use for which work, how they stay lean, and the review cadence |
| `scripts/catalog.py` | `validate` · `render` · `properties` · `check-public` |
| `.github/workflows/catalog.yml` | CI: schema + render check on every push, live drift + public-leak check weekly |

```bash
make validate   # schema + live GitHub check (needs gh auth)
make render     # regenerate docs/repository-map.md from catalog.yaml
make check      # everything CI runs, offline
make properties # dry-run: org custom properties vs catalog (APPLY=--apply to write)
```
