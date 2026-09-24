# Algorythmos-AI/.github-private

Members-only. GitHub shows [`profile/README.md`](profile/README.md) as the org homepage to members.
The public face is [`Algorythmos-AI/.github`](https://github.com/Algorythmos-AI/.github).

| Path | What it is |
|---|---|
| `profile/README.md` | Member homepage. The repo map section is generated; don't edit it by hand |
| `catalog.yaml` | The single source of truth for every Algorythmos repo |
| `AGENTS.md` | Rules for AI agents across all Algorythmos repos |
| `docs/naming.md` · `docs/ownership.md` · `docs/onboarding.md` | Standards, owners, first-day guide |
| `scripts/catalog.py` | `validate` · `render` · `check-public` |
| `.github/workflows/catalog.yml` | CI: schema + render check on every push, live drift + public-leak check weekly |

```bash
make validate   # schema + live GitHub check (needs gh auth)
make render     # regenerate the member homepage map from catalog.yaml
make check      # everything CI runs, offline
```
