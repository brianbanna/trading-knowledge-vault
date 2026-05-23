---
aliases: [futures contract, futures, exchange traded futures]
tags:
  - "#quant"
  - "#microstructure"
date-added: "2026-03-20"
---

# Futures Contract

## Definition
A futures contract is a standardized, exchange traded agreement to buy or sell a specific quantity of a commodity or financial instrument at a predetermined price on a specified future date. Unlike a [[Forward Contract]] (OTC, customizable), futures have standard sizes, delivery dates, and quality specs set by the exchange (CME, ICE, LME). All futures clear through a clearinghouse, which interposes between buyer and seller and eliminates bilateral counterparty risk. [[Margin]] requirements (5 to 15% of notional) provide built in leverage: a trader controls a large notional with a fraction of its value as collateral. Positions mark to market daily, gains credited and losses debited from the margin account at session close. Futures are the primary instrument for commodity price discovery, hedging, and speculative access across energy, metals, agriculture, and financial markets.

## Why it matters (commodities and FX)
Futures are the backbone of commodity markets, providing the price transparency and liquidity physical markets rely on for benchmarking and risk transfer. A corn farmer, oil refiner, and airline all use futures to hedge price exposure, while speculators and market makers provide the liquidity that makes those hedges possible. The forward curve visible through futures across expiries reveals expected supply and demand, including [[Contango Roll Cost|contango]] and [[Backwardation Roll Gain|backwardation]] structures. Futures mechanics (margin, daily settlement, expiry, delivery) are the prerequisite for every other commodity trading concept.

## Concrete example

**Concrete:** Trader buys 1 NYMEX WTI June contract at $80.00/bbl. Contract represents 1,000 barrels ($80,000 notional). Initial [[Margin]] ~$6,000. WTI rallies to $85.00/bbl over 2 weeks. Profit $5.00 × 1,000 = $5,000, 83% return on margin from a 6.25% spot move. Failure mirror: same trade, crude drops to $74.00/bbl on an unexpected OPEC+ increase. Loss $6,000 wipes the initial margin. Trader receives a [[Margin|margin call]] and must post additional funds or face forced liquidation at unfavorable prices. Leverage amplifies losses as aggressively as gains.

**Simplified:** A futures contract is a standardized bet on the price of something at a future date, traded on an exchange. You only put up a fraction of the contract's value as collateral, so a small move in the underlying creates a large percentage move in your account. That cuts both ways: gains and losses are amplified by the leverage. Most positions close before expiry rather than going to physical delivery.

## Key mechanics and formulas
- **Contract size examples:** WTI = 1,000 barrels; Corn = 5,000 bushels; Gold = 100 troy ounces; E mini S&P 500 = $50 × index
- **Tick size and value:** WTI = $0.01/bbl ($10 per tick); Corn = 1/4 cent/bu ($12.50); Gold = $0.10/oz ($10)
- **Leverage = Notional / Initial margin.** Typical commodity leverage: 10x to 20x.
- **Daily mark to market:** At close, clearinghouse calculates each position's PnL and adjusts margin accounts.
- **Expiry and rollover:** Most traders close before [[Delivery|first notice day]] and roll into the next month, incurring [[Contango Roll Cost]] or earning [[Backwardation Roll Gain]].

## Prerequisites
- [[Margin]]
- [[Delivery]]

## Related concepts (learn next)
- [[Forward Contract]] is the OTC, customizable counterpart used in physical commodity markets.
- [[Margin]] mechanics define leverage, risk, and capital requirements.
- [[Delivery]] anchors futures prices to spot reality.
- [[Cash Settlement]] is the alternative settlement method.
- [[Spread Trade]] is the dominant professional approach: simultaneous long/short positions in related futures.
- [[Contango Roll Cost]] is the loss rolling long futures in an upward sloping curve.
- [[Backwardation Roll Gain]] is the profit rolling long futures in a downward sloping curve.
- [[Option]] contracts on futures provide asymmetric payoffs.

## Common misconceptions

**"Futures are gambling."** Futures exist primarily for hedging. Producers and consumers use them to manage price risk. Speculator participation provides the liquidity that makes hedging possible.

**"You need the full notional to trade."** Futures are margined, requiring only a fraction. The trader is responsible for the full PnL, which can exceed margin posted.

**"All futures involve physical delivery."** Many ([[Cash Settlement|cash settled]] equity index, financial WTI) settle financially. Over 95% of physically deliverable positions close before delivery.

**"Futures prices equal expected future spot prices."** Futures reflect expected spot adjusted for cost of carry, convenience yield, and risk premiums. The relationship is more complex than simple expectations.

## Sources
- CME Group, "Understanding Futures"
- John Hull, "Options, Futures, and Other Derivatives"
- Commodity Trading Manual, Chicago Board of Trade
- "The Economics of Futures Trading" by B.A. Goss and B.S. Yamey
