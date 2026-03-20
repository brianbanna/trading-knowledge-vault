---
aliases: [futures contract, futures, exchange traded futures]
tags:
  - "#quant"
  - "#microstructure"
date-added: "2026-03-20"
---

# Futures Contract

## Definition
A futures contract is a standardized, exchange traded agreement to buy or sell a specific quantity of a commodity or financial instrument at a predetermined price on a specified future date. Unlike a [[Forward Contract]] (which is OTC and customizable), futures have standard contract sizes, delivery dates, and quality specifications set by the exchange (CME, ICE, LME, and others). All futures are centrally cleared through a clearinghouse, which interposes itself between buyer and seller and eliminates bilateral counterparty credit risk. [[Margin]] requirements (typically 5 to 15% of notional value) provide built in leverage, meaning a trader controls a large notional position with a fraction of its value as collateral. Positions are marked to market daily, with gains credited and losses debited from the margin account at the end of each trading session. Futures are the primary instrument for commodity price discovery, hedging, and speculative access across energy, metals, agriculture, and financial markets.

## Why it matters (commodities and FX)
Futures are the backbone of commodity markets, providing the price transparency and liquidity that physical markets rely on for benchmarking and risk transfer. A corn farmer, an oil refiner, and an airline all use futures to hedge their price exposure, while speculators and market makers provide the liquidity that makes those hedges possible. The forward curve visible through futures prices across different expiry months reveals the market's expectation of future supply and demand conditions, including [[Contango Roll Cost|contango]] and [[Backwardation Roll Gain|backwardation]] structures. For new traders, understanding futures mechanics (margin, daily settlement, expiry, and delivery) is the prerequisite for every other concept in commodity trading.

## Concrete example
**Success case:** A crude oil trader buys 1 NYMEX WTI June contract at $80.00/bbl. The contract represents 1,000 barrels ($80,000 notional). Initial [[Margin]] is approximately $6,000. WTI rallies to $85.00/bbl over 2 weeks. Profit: $5.00 x 1,000 barrels = $5,000, an 83% return on margin. The leverage amplifies the 6.25% spot move into an outsized percentage gain on capital deployed.

**Failure case:** The same trader buys 1 WTI June contract at $80.00/bbl. Crude drops to $74.00/bbl on an unexpected OPEC+ production increase. Loss: $6.00 x 1,000 = $6,000, wiping out the entire initial margin. The trader receives a [[Margin|margin call]] and must post additional funds immediately or face forced liquidation at unfavorable prices. The lesson: futures leverage amplifies losses just as aggressively as gains.

## Key mechanics and formulas
- **Contract size examples:** WTI crude = 1,000 barrels; Corn = 5,000 bushels; Gold = 100 troy ounces; E mini S&P 500 = $50 x index
- **Tick size and value:** WTI = $0.01/bbl ($10 per tick); Corn = 1/4 cent/bu ($12.50 per tick); Gold = $0.10/oz ($10 per tick)
- **Leverage = Notional value / Initial margin.** Typical commodity futures leverage: 10x to 20x.
- **Daily settlement (mark to market):** At close, the clearinghouse calculates each position's P&L and adjusts margin accounts. Gains are withdrawable; losses must be covered.
- **Expiry and rollover:** Most traders close positions before the [[Delivery|first notice day]] and roll into the next contract month, incurring [[Contango Roll Cost]] or earning [[Backwardation Roll Gain]].

## Prerequisites
- [[Margin]]
- [[Delivery]]

## Related concepts (learn next)
- [[Forward Contract]] is the OTC, customizable counterpart to exchange traded futures, used extensively in physical commodity markets.
- [[Margin]] mechanics define the leverage, risk, and capital requirements of futures trading.
- [[Delivery]] is the physical settlement process that anchors futures prices to spot market reality.
- [[Cash Settlement]] is the alternative settlement method where no physical commodity changes hands.
- [[Spread Trade]] involves simultaneous long/short positions in related futures, the dominant professional trading approach.
- [[Contango Roll Cost]] is the loss incurred when rolling long futures in an upward sloping curve.
- [[Backwardation Roll Gain]] is the profit earned when rolling long futures in a downward sloping curve.
- [[Option]] contracts on futures provide asymmetric payoffs and are widely traded on commodity exchanges.

## Common misconceptions
- **"Futures are just gambling."** Futures exist primarily for hedging. Producers and consumers use them to manage price risk. Speculator participation provides the liquidity that makes hedging possible and efficient.
- **"You need the full notional value to trade."** Futures are margined instruments requiring only a fraction of notional value. However, the trader is responsible for the full P&L, which can exceed the margin posted.
- **"All futures involve physical delivery."** Many contracts ([[Cash Settlement|cash settled]] equity index futures, financial WTI, and others) settle financially. Even among physically deliverable contracts, over 95% of positions are closed before delivery.
- **"Futures prices equal expected future spot prices."** Futures prices reflect expected spot prices adjusted for cost of carry, convenience yield, and risk premiums. The relationship is more complex than simple expectations.

## Sources
- CME Group, "Understanding Futures"
- John Hull, "Options, Futures, and Other Derivatives"
- Commodity Trading Manual, Chicago Board of Trade
- "The Economics of Futures Trading" by B.A. Goss and B.S. Yamey
