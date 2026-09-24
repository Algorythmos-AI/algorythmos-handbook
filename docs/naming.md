# Repository naming standard

Modelled on how `anthropics/*` and `openai/*` name repos: short, lowercase, product first, and
predictable enough that you can guess a repo's name before you search for it.

## Rules

1. **lowercase kebab-case only**: `[a-z0-9]` words joined by single hyphens. No capitals, underscores,
   dots, spaces, dates, version numbers (`v2`), or filler (`new`, `final`, `test`, `my-`).
2. **Product first.**
   | Shape | Use for | Examples |
   |---|---|---|
   | `<product>` | a monorepo that is the whole product | `algominutes` |
   | `<product>-<surface>` | one client surface of a product | `gurbani-soul-ios`, `wassup-web` |
   | `<product>-<component>` | a service or pipeline | `wassup-scheduling-api`, `sggs-data` |
   | `<product>-sdk-<lang>` | a published SDK | `algominutes-sdk-python` |
   | `<client>-<component>` | client work (set the `client` field in the catalog) | `ichr-website` |
   | `<name>-ops` | private runbooks and ops notes that pair with a public repo | `ichr-ops` |
   | `<name>-source` | non-redistributable inputs kept out of a public repo | `sggs-source` |
3. **No generic names in a multi-product org.** `frontend`, `api`, `backend` or `patient-api` on their
   own collide across products. Prefix them with the product.
4. **Families are documented, not renamed.** `sggs-*` is the scripture data platform; `gurbani-soul-*`
   is the consumer app brand. Both belong to the Gurbani Soul product.
5. **Every repo has** a one-line description, a README, and either a licence or an explicit
   "Proprietary" notice. Public repos also get topics.
6. **Retire by archiving, never deleting.** Never reuse a retired name: reusing it breaks the redirect
   GitHub keeps for the old URL.

## Renaming an existing repo

Renames need explicit approval (see [`AGENTS.md`](../AGENTS.md) §3). The backlog lives in
`catalog.yaml` as `target_name` and appears on the member homepage. When you rename:

1. Rename on GitHub. Web and git URLs redirect automatically.
2. Update `catalog.yaml` (`repo`, drop `target_name`), `make render`, commit.
3. Search for hard-coded URLs in other repos (`dataset.lock.json`, `vendor.lock.json`, CI workflows,
   Vercel/Render project settings) and update them. Redirects cover git, not every integration.
4. Update local remotes: `git remote set-url origin https://github.com/Algorythmos-AI/<new>.git`.
