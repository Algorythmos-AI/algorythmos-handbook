# Trading platforms: three repos and a shared knowledge base

**Owner decision D-026 (10 Oct 2026).** Trading work is three separate platforms, each in its own repository,
sharing one knowledge base. The aim is that nobody, and no code, confuses one platform with another.

## The map

| Platform | Repo | Trades | Status |
|---|---|---|---|
| HFT Lab | `hft-lab` | Currencies (forex), many trades a day held for seconds to minutes, on a broker paper account | planned |
| Crypto Lab | `crypto-lab` | Crypto on 15-minute to 4-hour bars, on the lab's own simulator | being extracted from `trading-lab-research` |
| Options Lab | `trading-lab-research`, to be renamed `options-lab` | US stocks and options | live |
| Trading Knowledge Base | `trading-kb` | nothing: sources, extracts, claim cards | planned |

Related repos: `trading-lab-source` keeps the stocks course material until it is folded into `trading-kb` as a
collection. `trading-lab` is the original gap-and-go pipeline. `trading-lab-kraken-bot` is the archived crypto
prototype.

All of it is **paper trading only**. No repo here holds a way to reach a real-money account.

## The separation contract

1. One platform is one repo, one catalog product, one research registry, one CI and one set of deploy units.
2. No imports or submodules across platforms. A pull request touches one platform repo.
3. Each platform owns its config, kill switch, state directory, journal, alert-key prefix, snapshot schema id,
   host user or unit prefix, secrets file and runbooks. Nothing reads another platform's state.
4. Platforms share in two ways only:
   - a tagged `trading-kb` release, pinned in the platform's `kb.lock.json`;
   - a published, versioned data contract (a snapshot schema) that the consumer vendors with a hash check.
5. Research ids never collide.
   - `hft-lab` records start `HFT-`; new `crypto-lab` records start `CRY-`.
   - Records that moved with the crypto desk keep their old numbers. Those numbers are never reused.
   - A reference to another repo's record is written `repo:ID`.
6. In `trading-kb` a pull request touches one collection. Cards carry a `platforms` tag so one search can be
   filtered by platform.
7. There is no shared code library. Each platform keeps its own trimmed copy of the generic pieces it needs,
   with the origin commit noted. Revisit once all three run stably.
8. An agent session works in its own clone or worktree of one repo.

## What stays shared, on purpose, for now

| Shared | Why | What ends it |
|---|---|---|
| The status site (`lab.algorythmos.com`) lives in the stocks and options repo and shows every desk. Since 2026-10-11 its desks are a registry and it has an HFT page; a desk in another repo is shown through that repo's own snapshot contract, vendored with a hash lock | Moving it would break that repo's deploy guard and collide with work in flight | A repo of its own |
| One ingest key signs every desk's snapshot | A second key would be filed where nothing reads it | Per-desk key scope in the ingest route |
| One cloud server | Owner's choice. Platforms are isolated by user, unit prefix and resource caps | A measured limit |

## Order of the change

1. `trading-kb` and `hft-lab` are created; the knowledge base is built from the owner's HFT study folder.
2. `crypto-lab` is built and proven to behave identically to the desk inside `trading-lab-research`.
3. The owner cuts the crypto jobs over on the host. State is moved, never copied.
4. After a clean day, the crypto code leaves `trading-lab-research`.
5. With the owner's go-ahead, `trading-lab-research` is renamed `options-lab`
   ([`naming.md`](naming.md) has the rename steps).

Each new repo joins [`catalog.yaml`](../catalog.yaml) as `planned` first and becomes `active` when it exists.
