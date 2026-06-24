---
aliases: [Trafigura Group, Trafigura Pte Ltd]
tags:
  - "#energy/crude"
  - "#metals/base"
date-added: "2026-06-24"
---

# Trafigura

## Definition

Trafigura is one of the largest independent physical commodity trading houses in the world, alongside [[Vitol]], [[Glencore]], Gunvor, and Mercuria. In plain terms, it buys physical raw materials where they are cheap or unwanted, moves and stores them, and sells them where they are needed and dearer, financing and hedging the flow along the way. Its 2 core books are oil and petroleum products, and metals and minerals, where it is the largest trader of non ferrous concentrates. Founded in 1993 by Claude Dauphin, Eric de Turckheim and partners out of the remnants of Marc Rich + Co (the same lineage that produced Glencore), it is a private, employee owned partnership registered in Singapore with major trading hubs in Geneva and Houston. It is asset backed: it owns logistics, storage, and processing infrastructure (Impala Terminals, the Nyrstar smelting business, a Puma Energy stake) rather than trading purely on paper.

## Why it matters (commodities and FX)

Trafigura is the archetype of the proprietary, discretionary, physical desk seat described in [[Trading Taxonomy]]. Studying it teaches what a physical trading house actually does and where its edge comes from:

- **It moves prices and reads flow.** As a principal intermediary it sees physical supply and demand before the screen does. That information edge feeds its paper positioning.
- **Its edge is logistics, financing, and arbitrage, not forecasting.** It profits from locational, calendar, and quality spreads, the relative value coordinate, not from calling the flat price.
- **It carries optionality in real assets.** A storage tank is a [[Calendar Spread|calendar spread]] option, a chartered ship is an option on freight, a smelter is an option on the treatment charge. See [[Storage Economics]] and [[Convenience Yield]].
- **It hedges its physical book on paper.** Every barrel bought is typically sold forward on futures or swaps, so the house is long basis and short flat price, isolating the [[Relative Value Trade|relative value]] it is actually paid for.

For an aspiring physical trader, Trafigura is the target employer template: it wants commercial judgment that uses paper as a tool, not a quant who optimizes signals on screen prices.

## Concrete example

The 2020 oil contango carry, a textbook house trade Trafigura and its peers ran at scale.

In April 2020 the demand collapse pushed front month crude far below later months, a steep [[Contango]]. Walk the cash and carry, see [[Cash and Carry Arbitrage]]:

- Buy physical crude in the spot market at, say, 20 dollars per barrel.
- Simultaneously sell a futures contract 6 months out at 35 dollars per barrel.
- Store the barrels (onshore tank or a chartered VLCC as [[Floating Storage|floating storage]]) at a cost of, say, 8 dollars per barrel over the 6 months including financing.
- At expiry, deliver the stored crude against the short future.

If it works: locked spread of 15 dollars minus 8 dollars storage and finance equals 7 dollars per barrel, captured with near zero flat price risk because the sale was hedged the moment the crude was bought. Scale that across millions of barrels.

If it fails: the contango collapses faster than expected and you cannot roll the storage economically, or storage and freight rates spike (VLCC day rates did surge in 2020) and eat the entire spread, or a counterparty on the physical leg defaults. The flat price move is hedged, so the risk is in the basis, the storage cost, and the counterparty, exactly the risks a physical house is built to manage and a screen trader is not.

## Key mechanics and formulas

Trafigura's model, decomposed on the [[Trading Taxonomy]] axes:

- **Capital**: proprietary, employee owned. Profits and losses are the partners' own.
- **Decision**: discretionary, with quant and analytics support.
- **Liquidity role**: principal intermediary in physical (provides liquidity to the cargo market), taker in paper (pays the spread to hedge).
- **Horizon**: swing to position, cargoes clear in days to months.
- **Physical vs paper**: physical core, paper overlay.
- **Risk structure**: relative value heavy, locational, calendar, and quality arbitrage.

Scale markers (round figures, recent fiscal years, not pinned): group revenue on the order of 240 billion dollars, among the largest private companies in the world by turnover, with record net profit in the multiple billions during the 2022 to 2023 dislocation. Margins are thin per barrel or tonne but volume and asset backing make the absolute numbers large.

## Prerequisites

- [[Trading Taxonomy]]
- [[Cash and Carry Arbitrage]]
- [[Relative Value Trade]]

## Related concepts (learn next)

- [[Vitol]] — the largest independent oil trader, the firm Trafigura is most often compared to.
- [[Glencore]] — same Marc Rich lineage, but a listed, mining heavy hybrid rather than a private pure trader.
- [[Contango]] — the curve shape that makes the storage carry trade profitable.
- [[Storage Economics]] — how a house prices the embedded option in a tank or a ship.
- [[Convenience Yield]] — why a physical holder values the barrel above its forward, the source of physical optionality.
- [[Crack Spread]] — a worked refining relative value trade a products desk runs.
- [[Brent-WTI Spread]] — locational arbitrage between 2 crude benchmarks, the kind of spread a crude desk lives in.
- [[OPEC+]] — the supply side actor whose decisions reshape the curves Trafigura trades.

## Common misconceptions

- **"Trafigura is a prop shop."** No. It trades proprietary capital, but "prop shop" is reserved for financial market makers like Jane Street. Trafigura is a physical trading house. See [[Trading Taxonomy]].
- **"Physical traders bet on the oil price."** The core book is hedged. The house is paid for the basis and the logistics, not the flat price. A trader who runs naked flat price exposure is taking risk the firm is not built to reward.
- **"It is a bank or a fund."** It runs its own money on physical flow, not client capital for a fee, and not a screen only paper book. Different business model, different risk, different seat.
- **"The assets are a distraction from trading."** The terminals, ships, and smelters are the trading edge. They are what let the house source, store, and transform, and they are the physical options it monetizes with paper.

## Sources

- Trafigura Group annual reports and responsibility reviews.
- Javier Blas and Jack Farchy, *The World for Sale*, on the commodity trading houses and the Marc Rich lineage.
- Tamvakis, *Commodity Trade and Finance*, on the physical house business model and asset backed trading.
