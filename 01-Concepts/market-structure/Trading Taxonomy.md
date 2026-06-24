---
aliases: [trading axes, prop vs discretionary, trading role taxonomy, trading style taxonomy, types of trading]
tags:
  - "#microstructure"
  - "#quant"
  - "#regulation"
date-added: "2026-06-24"
---

# Trading Taxonomy

## Definition

A trading role is not a single label. It is a coordinate on several independent axes at once. The most common beginner mistake is comparing 2 axes that are not the same axis, for example "prop vs discretionary." That is a category error, like asking the difference between Italian and spicy. Prop answers *whose capital and whose P&L*. Discretionary answers *how the decision is made, human or model*. They are orthogonal: every combination exists. To describe a real seat precisely, you place it on all 8 axes below and read off the vector.

## Why it matters (commodities and FX)

The taxonomy is the precise coordinate gap between the seat you want and the seat your background signals. A commodities trading house, a financial prop shop, a systematic fund, and a bank flow desk all say "trading," yet they share almost no coordinates. Hiring managers filter on the vector, not the word. A physical desk wants commercial judgment that uses paper as a tool, not a fund quant who optimizes signals. Knowing your own coordinates versus the target's tells you exactly which dimensions to move, and in what order, before a recruiting cycle. It also tells you why a CV that screams "fund plus systematic" gets filtered out of a "proprietary plus discretionary plus physical" search even when the skills overlap.

## The 8 axes

### Axis 1: Capital and business model

*Whose money, whose P&L. The axis that decides what your job actually is.*

- **Proprietary**: the firm trades its own money, keeps its own P&L, eats its own losses. 2 distinct species the industry treats as separate worlds:
  - *Financial prop shops*: Jane Street, Jump, Optiver, IMC, DRW, Citadel Securities. Mostly market making and arbitrage, high volume, short horizon.
  - *Physical houses*: Vitol, Trafigura, Glencore, Cargill. Trade their own book on physical flows.
  - Quirk: "prop shop" only ever refers to the first group. Nobody calls Vitol a prop shop even though every barrel is its own risk. The term is reserved, not literal.
- **Agency, flow, sell side**: bank desks that execute and make markets for clients, earning the spread, not the position. Since Dodd Frank (2010, Volcker Rule) banks are largely barred from pure prop, so a modern bank desk is mostly flow with positioning incidental to facilitating client orders.
- **Buy side, fund**: you run other people's capital for a management fee plus a performance fee. Hedge funds, macro funds, CTAs.
- **Physical desk lands**: proprietary.

### Axis 2: Decision process

*Human or model makes the call.*

- **Discretionary**: a human carries the book and the commercial read. Models inform, the person decides and owns it. Example: a [[Trafigura]] crude trader.
- **Systematic, quant**: rules and models generate and often execute trades. The human builds the system, not the individual trade. Example: a CTA, an HFT desk.
- **Hybrid, quantamental**: a human using quant signals to build conviction, or a systematic book with human overlays. Example: a physical desk strategist. This is the realistic bridge from a quant background into a discretionary seat.
- **Physical desk lands**: discretionary.

### Axis 3: Liquidity role

*Do you make the price or take it. Distinct from capital: a bank desk and Jane Street both make markets on different capital models.*

- **Provider, maker**: quotes 2 sided prices, earns the bid ask spread, profits from volume and flow. Core risk is inventory and [[Adverse Selection]]. Example: Citadel Securities, a bank FX desk. See [[Liquidity]].
- **Taker**: crosses the spread to express a view, pays the spread as a cost, profits from being right on direction or relationship. Example: a macro fund, a hedger.
- **Physical desk lands**: taker in paper (it pays the spread to hedge and position), but in physical it acts as a principal intermediary providing liquidity to the cargo market, willing to lift the barrel nobody else will and warehouse the risk. That dual nature is part of the house edge.

### Axis 4: Holding period

*How long the risk lives.*

- **HFT**: microseconds to seconds. Almost always systematic and prop.
- **Intraday**: flat by the close.
- **Swing**: days to weeks.
- **Position**: months to years.
- **Physical desk lands**: swing to position. Cargo clears in days to months, never HFT.

### Axis 5: Physical vs paper

*Do you touch the cargo.*

- **Physical**: the cargo itself. Edge in logistics, information, arbitrage, and optionality on the asset. See [[Physical vs Paper Freight]].
- **Paper**: derivatives (futures, swaps, options). Edge in pricing, flow, and positioning.
- **Physical desk lands**: physical core, paper overlay to [[Hedging|hedge]] and position.

### Axis 6: Risk structure

*Directional, spread, or hedged.*

- **Outright**: directional bet on the price level. Example: long [[WTI Crude Oil]] because you think crude rises.
- **Relative value**: bet on the spread between 2 related instruments. See [[Relative Value Trade]] and [[Spread Trade]].
- **Market neutral**: hedged so net direction is roughly 0, profit from convergence. Example: a stat arb pair.
- **Physical desk lands**: relative value heavy. Locational arb (where), [[Calendar Spread|calendar arb]] (when), [[Quality Spread|quality arb]] (which grade). [[Brent-WTI Spread]], the [[Crack Spread]], and the [[Sugar-Ethanol Spread]] are all this.

### Axis 7: Instrument linearity

*The payoff shape of what you trade. Distinct from Axis 5: a paper trader can be linear or nonlinear.*

- **Linear (delta one)**: cash, futures, forwards, swaps. P&L moves 1 for 1 with the underlying, no optionality.
- **Nonlinear (convex)**: options and anything with embedded optionality. P&L is curved, Greeks matter.
- **Physical desk lands**: linear paper for hedging, but the physical asset itself carries embedded options. Storage is a [[Calendar Spread|calendar spread]] option, a ship is an option on freight, a refinery is a [[Crack Spread|crack]] option. The skill is seeing the optionality in the physical and deciding whether to monetize it with paper. Ties to [[Roll Yield]], [[Storage Economics]], and [[Convenience Yield]].

### Axis 8: Asset class and market

*Which complex.*

- Energy (oil, products, gas, power), metals (base, precious), ags and softs, freight, plus the financial cross overs (rates, FX, equity index) that physical desks watch as macro drivers.
- **Physical desk lands**: one complex deep, not all at once.

## Key mechanics and formulas

A role is not a label, it is a vector with 1 value per axis. Decompose real roles and the structure is obvious:

| Axis | Trafigura crude trader | Jane Street trader | Brevan macro PM |
| --- | --- | --- | --- |
| Capital | proprietary | proprietary | fund |
| Decision | discretionary | systematic | discretionary |
| Liquidity | physical provider, paper taker | maker | taker |
| Horizon | swing to position | HFT to intraday | position |
| Physical / paper | physical core plus overlay | paper only | paper |
| Risk structure | relative value | market neutral | outright plus RV |
| Linearity | linear hedge plus physical optionality | heavy options | linear plus options |
| Market | crude | cross asset | rates, FX, macro |

All 3 say "trading." They share almost no coordinates. That is the whole point: the word "trader" carries no information until you read the vector.

## Concrete example

Map a quant or HFT background against a target physical desk seat and the gap becomes a checklist:

| Axis | Quant or HFT background signals | Target physical desk seat |
| --- | --- | --- |
| Capital | fund dialect | proprietary |
| Decision | systematic | discretionary |
| Liquidity | signal taker | physical principal, paper taker |
| Horizon | swing | swing to position |
| Physical / paper | paper only | physical core plus overlay |
| Risk structure | RV plus factor bets | relative value |
| Linearity | linear futures | linear hedge plus physical optionality |
| Market | cross commodity | one complex deep |

- Already matching: horizon, risk structure.
- Gap of 4 coordinates: capital dialect, decision process, physical vs paper, liquidity role.
- 3 of those 4 are hard to change from outside a seat. 1 (how you frame and what you build) can move now, before the next cycle. That is the highest leverage move: re-present existing work in proprietary, discretionary, physical language rather than fund, systematic, signal language.

The taxonomy is not trivia. It tells you exactly which coordinates to move, and the order to move them.

## Prerequisites

- [[Liquidity]]
- [[Relative Value Trade]]
- [[Hedging]]

## Related concepts (learn next)

- [[Adverse Selection]] — the core risk a liquidity maker carries, and why making is not free money.
- [[Spread Trade]] — the executable form of the relative value coordinate on Axis 6.
- [[Crack Spread]] — a worked physical desk relative value trade spanning crude and refined products.
- [[Brent-WTI Spread]] — locational and quality arbitrage between 2 crude benchmarks.
- [[Convenience Yield]] — why a physical holder values the barrel above its forward, the source of physical optionality.
- [[Storage Economics]] — storage as an embedded calendar spread option, the clearest Axis 7 example.
- [[Roll Yield]] — how a paper position bleeds or earns over time, the cost of expressing a view without the physical.
- [[Single Dealer Platform]] — the venue layer where the maker versus taker distinction on Axis 3 plays out in FX.

## Common misconceptions

- **"Prop and discretionary are alternatives."** They are different axes. A trader is always at a point on both at once. Every combination is a real job.
- **"Prop shop and proprietary mean the same thing."** Every physical house trades proprietary capital, yet none is called a prop shop. The term is reserved for financial market makers and arbitrageurs. Using it loosely signals you do not know the industry.
- **"A bank desk is prop because it takes risk."** Since the Volcker Rule, bank desks are mostly flow. Positioning is incidental to facilitating client orders, not the business model.
- **"Physical traders only trade cargo."** They run a physical core with a paper overlay. The edge is seeing the optionality embedded in the physical asset and deciding when to monetize it with linear or nonlinear paper.

## Sources

- Dodd Frank Wall Street Reform and Consumer Protection Act (2010), Volcker Rule provisions on proprietary trading.
- Industry structure as described in commodity trading house disclosures (Vitol, Trafigura, Glencore annual reviews).
- Tamvakis, *Commodity Trade and Finance*, on physical versus paper and the principal intermediary role.
