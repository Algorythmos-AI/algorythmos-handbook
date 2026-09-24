# AGENTS.md — rules for AI agents working across Algorythmos repositories

Read this before acting in any `Algorythmos-AI` repo. It applies to Claude, Codex, Copilot and any
other automated contributor.

## 1. Orient

1. **Read [`catalog.yaml`](catalog.yaml) first.** It is the only source of truth for what a repo is,
   who owns it, its visibility (now and intended), its data class, default branch and deploy targets.
   Do not infer any of these from memory, repo names or old conversations.
2. **Then read the target repo's own `CLAUDE.md` / `AGENTS.md` / `CONTRIBUTING.md`.** A repo's own rules
   override anything here except section 3.
3. If the catalog and GitHub disagree, trust GitHub, say so, and propose a catalog fix. Don't work
   around it silently.

## 2. Work

- Branch from the repo's default branch, open a PR, and let CI gate it. Never push straight to `main`
  or `integration`.
- Deployed web platforms promote `integration` → `main`. Apps and data repos use `main` only.
- A change that adds, renames, transfers, archives or re-scopes a repo must update `catalog.yaml`
  and re-render the member homepage (`make render`) in the same PR here.
- Scripture repos (`sggs-*`, `gurbani-soul-*`): text is verbatim and cited by Ang. Never edit,
  normalise or "correct" Gurmukhi. Follow each repo's editorial-ledger rules.

## 3. Never, without explicit human approval in chat

These actions are possible with the owner's `gh` token. Being possible is not being allowed.

- Change a repo's **visibility**, **rename**, **transfer**, **archive** or **delete** a repo.
- Change org settings, rulesets, branch protection, required checks or security settings.
- Force-push, rewrite history, or delete branches/tags you did not create.
- Publish anything outward-facing: releases, the public profile, deployments to production.

## 4. Never, under any circumstances

- Copy content from a private repo, or from the company-records folders (`asic/`,
  `business-bank-account/`, `Clients/`, `Bustle-studios/` in the website repo) into a public repo,
  issue, PR body, commit message or log.
- Write secrets into any file: tokens, keys, passwords, tax file numbers, bank or card numbers.
  They live in GitHub Actions secrets, Vercel/Render/GCP environment settings, or the git-ignored
  company records — never in git.
- Publish a street address, officeholder date of birth or home address, or any French entity claim.
- Link a **temporarily public** repo (see the catalog) from a public page.

## 5. Facts you may state publicly

Algorythmos Pty Ltd · ACN 701 006 626 · ABN 22 701 006 626 · Sydney, Australia ·
info@algorythmos.com.au · careers@algorythmos.com · https://algorythmos.com.
It is a single-person company: do not write copy implying a team, board or multiple founders.
