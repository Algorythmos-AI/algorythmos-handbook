# Model and effort policy for agents

How every AI agent working for Algorythmos picks a model and an effort level, and how it keeps
threads and subagents lean. Binding for agents through [`AGENTS.md`](../AGENTS.md) §2 (decision D-028).

Facts and prices are as of **2026-11-09**, from Anthropic's model guide ("Which Claude model should
you build with?") and the Claude API price list. This field changes every few months: the monthly
review below keeps this page current. When a price here disagrees with Anthropic's pricing page,
the pricing page wins and this page gets a fix.

## The four rules

1. **Start on Opus 5.5 at `medium`.** It is the session default and the right answer when unsure.
2. **Go down when the task is well scoped or high volume.** Sonnet 5.5 for a fix or feature against a
   clear spec; Haiku 5.5 for searching, reading logs, summarising and extraction.
3. **Go up only after the cheaper steps fail,** in this order:
   1. Give the model a way to check its own work (a test, a build, `make check`, a script).
   2. Raise effort one level.
   3. Move to the next model up, starting at a *lower* effort than you used on the smaller one.
4. **Keep the expensive model's context for decisions.** Verbose reading goes to a cheaper subagent
   that returns a short conclusion.

Past `high`, one more effort level can cost as much as the next model up. On Opus 5.5, `xhigh` costs
about 2.5× `high` for about 1.4 points on SWE-bench Pro, so `xhigh` and `max` need a stated reason.

## Which model for which work

| Work | Model | Effort | Why |
|---|---|---|---|
| Coordinator (project chat), planning a thread, routing work | Opus 5.5 | `medium` | Judgment across the org; context kept short |
| Code change in one repo, debugging | Opus 5.5 | `medium`, then `high` | Everyday engineering default |
| Fix or feature against a written spec, catalog edits, CI config, dependency bumps | Sonnet 5.5 | `medium` | Well scoped; half Opus's price |
| Explorer subagents: find files, grep across repos, read CI or deploy logs, summarise a web page | Haiku 5.5 | `low`–`medium` | A wrong answer is cheap to spot |
| Routine PR review | Sonnet 5.5 | `medium` | Repeated agent task |
| Review of high-stakes changes: auth, payments, secrets, scripture text (`sggs-*`), trading, anything touching production | Opus 5.5 | `high` | Mistakes are expensive; reviewer reads the code, not the author's conclusion |
| Handbook, README and runbook writing | Sonnet 5.5 | `medium` | Everyday documents |
| Decisions, strategy and architecture write-ups | Opus 5.5 | `high` | Judgment, not prose |
| Multi-repo refactors and migrations (for example the trading split, D-026, or going private), architecture planning, leading many subagents, long unattended runs | Fable 5.2 | `medium`, then `high` | Hardest work; or when Opus 5.5 at `high` still falls short |
| Product features that call the Claude API (classification, routing, extraction) | Haiku 5.5 | default | High volume; measure before moving up |
| Product features that call the Claude API (summaries, drafting, chat) | Sonnet 5.5 | `medium` | Fast, mid-price; measure against Opus on real samples |

Scripture repos: a small model may *find* files, but any check of Gurmukhi text, Ang citations or
the editorial ledger stays on the main model (AGENTS.md §2).

## Running threads and subagents lean

- **One thread, one goal.** Unrelated work goes to a new thread so neither context grows.
- **Spawn a subagent only for** independent work that can run in parallel, a broad sweep whose file
  dumps you don't need, or a review that must not be anchored on your own reading. A lookup you
  could do in two tool calls stays inline.
- **Brief subagents narrowly:** goal, files to read, what is already ruled out, the shape of the
  answer, and the org rules that apply (AGENTS.md §2 attribution rule, §4). Ask for the conclusion,
  not the contents.
- **Set the subagent's model explicitly.** In repos with a `.claude/agents/` folder, the `Explore`
  agent runs on Haiku (see [`.claude/agents/explore.md`](../.claude/agents/explore.md)); copy it into
  any repo where agents explore a lot. `CLAUDE_CODE_SUBAGENT_MODEL` sets the default for subagents
  that name no model.
- **No multi-agent workflows or deep research unless the owner asks.** Orchestration pays off only
  for bulk, independent work; for one chain of dependent steps it costs more than it saves.
- **Don't re-read, don't re-run.** Use what the conversation already established. After a test
  failure, re-run only the failing tests until they pass, then the full suite once.
- **Batch checkable work cheaply:** when an outcome can be checked automatically, run everything at
  `low` and re-run only the failures at `high` (about 97% pass at 60% of the all-`high` cost in
  Anthropic's test).
- **Switching models mid-session:** the prompt cache belongs to the model that wrote it. Run
  `/compact` first, or start a fresh session from a short written plan.
- **Price the long tail.** A few hard tasks carry most of the spend (two of twenty problems took 43%
  in one benchmark). Stop and report after repeated failed attempts rather than escalating effort
  indefinitely.

## Price card (Claude API list prices, per million tokens, 2026-11-09)

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 | Fable 5.2 |
|---|---|---|---|---|
| Input / output | $0.10 / $0.50 (prompt ≤100K); $0.50 / $2.50 (>100K) | $2 / $10 | $4 / $20 | $8 / $40 |
| Cache reads | $0.01 (≤100K); $0.05 (>100K) | $0.10 | $0.20 | $0.20 |
| Default effort (API / Claude Code) | `medium` | `high` / `medium` | `medium` | `high` / `medium` |

All four have a 1M-token context window and 128K max output. Opus 5.5 and Fable 5.2 always think and
offer a fast mode at premium prices, used only when the owner asks for
speed.

## Approval gates

- Changing a project's default model, effort level or environment settings needs the owner's
  approval in chat.
- A Fable 5.2 run, a multi-agent workflow, or a long unattended run is announced to the owner with
  its purpose before it starts.
- Changing the model a *product* calls in production is a normal code change: PR, CI, and the
  repo's own promotion rules.

## Review cadence

| When | What | Output |
|---|---|---|
| Monthly (first Monday) | Check Anthropic's news, model pages and pricing for new models, price changes, effort or default changes, and deprecations | A PR updating this page and the D-028 entry if anything changed; otherwise a one-line "no change" note |
| Quarterly | Measure on our own work: pick five recent real tasks with a checkable outcome, run two candidate models at two effort levels, compare cost (`/usage`) against outcome | Keep or change the routing table above |
| On any new model release | Read the release notes and migration checklist before switching anything | Same as monthly |
