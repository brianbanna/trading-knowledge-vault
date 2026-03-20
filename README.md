# Trading Knowledge Vault

An open source, structured knowledge base for commodity and FX trading. Built as an [Obsidian](https://obsidian.md) vault with bidirectional links, domain tagging, and a visual knowledge graph.

Covers energy, metals, agriculture, softs, FX, rates, macro, and quantitative concepts. Every note links to prerequisites, related concepts, and concrete examples using real instruments and real market logic.

---

## What this is

A personal learning system turned public resource. Every concept encountered while studying commodity and FX markets gets a structured entry: definition, why it matters, step by step examples, formulas, prerequisites, and pointers to what to learn next.

The vault is designed so that each note's "Related concepts" section surfaces adjacent unknowns, concepts you need to learn next. The graph view in Obsidian visualizes how everything connects.

## How to use it

**Option 1: Browse on GitHub.** Every note is a standalone markdown file. Navigate the folders or use GitHub search.

**Option 2: Clone and open in Obsidian.**
```
git clone https://github.com/brianbanna/trading-knowledge-vault.git
```
Open the cloned folder as a vault in Obsidian. The `[[wiki links]]` become clickable, the graph view shows the full knowledge map, and the hub notes anchor each domain cluster.

## Structure

```
_hubs/                    → Domain hub notes (graph cluster anchors)
01-Concepts/              → Trading concepts, theories, frameworks
  macro/                    Central bank policy, inflation, real rates
  market-structure/         Liquidity, slippage, supply shocks, OPEC
  pricing-and-valuation/    Forward curve, contango, carry, basis
  quantitative/             Correlation, mean reversion, cointegration
  risk/                     Position sizing, VaR, drawdown
  psychology/               Behavioral biases, discipline
02-Instruments/           → Specific tradeable contracts
  commodities-energy/       Brent, WTI, TTF, Henry Hub
  commodities-metals/       Copper, gold, aluminum, silver
  commodities-agriculture/  Corn, soybeans, wheat
  commodities-softs/        Cocoa, coffee, sugar, cotton
  fx/                       EUR/USD, USD/JPY, AUD/USD
  rates/                    Treasuries, Bunds, swaps
  equities/                 Indices, ETFs, single stocks
  crypto/                   BTC, ETH, DeFi
03-Markets/               → Exchanges, venues, regulation
04-Strategies/            → Trading strategies and playbooks
  relative-value/           Brent/WTI spread, crack spread, calendar spreads
  mean-reversion/           Pairs trading, z-score strategies
  trend-following/          Momentum, breakout systems
  volatility/               Vol selling, straddles
  event-driven/             Earnings, data releases, OPEC
  execution/                VWAP, TWAP, algo strategies
05-People-and-Firms/      → Notable traders, firms, researchers
06-Data-and-Indicators/   → Economic releases, reports, data sources
09-Resources/             → Books, papers, courses
```

## Domain Tags

Notes are tagged by domain for filtering and graph coloring. Tags are hierarchical:

| Domain | Example Tags |
|--------|-------------|
| Energy | `#energy/crude/brent`, `#energy/natgas/ttf`, `#energy/refined/gasoline` |
| Metals | `#metals/precious/gold`, `#metals/base/copper`, `#metals/ferrous/iron-ore` |
| Agriculture | `#agri/grains/corn`, `#agri/softs/cocoa`, `#agri/oilseeds/soybeans` |
| FX | `#fx/g10/eurusd`, `#fx/em/usdbrl`, `#fx/structure` |
| Rates | `#rates/govies/ust`, `#rates/swaps`, `#rates/credit` |
| Cross cutting | `#macro`, `#quant`, `#risk`, `#execution`, `#microstructure` |

Searching `#energy` returns all energy notes. Searching `#energy/natgas` returns only natural gas notes.

## Note Format

Every note follows the same structure:

- **Definition** — plain English first, then technical precision
- **Why it matters** — specific to commodities and FX trading
- **Concrete example** — real instruments, real numbers, step by step
- **Key mechanics and formulas** — with plain English variable definitions
- **Prerequisites** — what you need to know first
- **Related concepts** — what to learn next (5 to 8 linked items)
- **Common misconceptions** — real traps traders fall into
- **Sources** — books, exchange guides, research papers

## Contributing

Contributions welcome. Fork the repo, create notes following the format above with proper domain tags and `[[wiki links]]`, and submit a PR.

## License

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Free to share and adapt with attribution.

## Author

Built by Brian Banna as a personal learning system for commodity and FX trading.
