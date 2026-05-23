---
aliases: [liquidity risk, liquidity mismatch, illiquidity risk, funding liquidity]
tags:
  - "#risk"
  - "#microstructure"
date-added: "2026-03-20"
---

# Liquidity Risk

## Definition

Liquidity risk is the risk that you cannot exit or adjust a position at a reasonable price when you need to. It has 2 dimensions: market liquidity risk (the asset is hard to trade without moving the price) and funding liquidity risk (you cannot meet margin or collateral, forcing liquidation at bad prices). Both interact: when [[Volatility]] spikes, market liquidity dries up AND margin requirements increase, creating a feedback loop. Liquidity risk is what turns a manageable loss into a catastrophic one.

## Why it matters (commodities and FX)

Commodity markets have highly uneven [[Liquidity]]. The [[Front Month]] of [[WTI Crude Oil]] trades 500,000+ contracts/day. The 18th month trades maybe 5,000. A [[Calendar Spread]] with one leg in an illiquid month carries liquidity mismatch: one leg exits easily, the other does not. In fast markets, the mismatch turns a hedged position into a naked directional bet.

[[Relative Value Trade|Spread trades]] are especially exposed because both legs must trade simultaneously. If one leg freezes (exchange halt, margin cascade, counterparty failure), the spread unravels. This happened to many firms during the 2022 LME nickel squeeze: the exchange halted nickel for a week, leaving hedged positions (long nickel, short another metal) with one leg locked while the other moved freely.

## Concrete example

**Concrete:** LME Nickel, March 2022. A short squeeze ran nickel from $25,000 to over $100,000/tonne in hours. LME halted trading and cancelled trades. Firms with hedged positions (long copper / short nickel relative value) could not exit the nickel leg. Copper kept trading and fell as broader risk off hit metals. The "hedged" spread became a naked short copper position. A trade designed to be market neutral generated catastrophic losses. The exchange itself was the liquidity event, not the market.

**Simplified:** Liquidity is the ability to trade size at a price close to the screen. Risk is that liquidity vanishes precisely when you need it. Market makers pull quotes when vol spikes. Exchanges can halt trading. Funding partners cut credit. A position you assumed you could exit at the bid is suddenly stuck. Spread trades make this worse because they need both legs to be liquid at the same time. When one leg freezes and the other does not, your hedge becomes a naked bet.

## Key mechanics and formulas

**Liquidity risk dimensions:**

| Type | Definition | Measurement |
|------|-----------|-------------|
| Market liquidity | Trade without price impact | [[Bid-Ask Spread]], depth, [[Market Impact]] |
| Funding liquidity | Meet margin and collateral needs | Margin utilization, cash buffer, credit lines |

**Liquidity adjusted VaR:**
`LVaR = VaR + (0.5 × Bid-Ask Spread × Position Size)`

Adds the cost of liquidation to the standard risk measure.

**Days to liquidate:**
`Days = Position Size / (ADV × Participation Rate)`

10,000 WTI contracts, ADV 500,000, 5% participation: 10,000 / 25,000 = 0.4 days. 10,000 contracts in a thin month with ADV 5,000: 10,000 / 250 = 40 days.

**Liquidity mismatch score:**
`Mismatch = Max(Days to Liquidate) / Min(Days to Liquidate)`

Mismatch above 5x is a red flag for spread trades.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]
- [[Volatility]]

## Related concepts (learn next)
- [[Liquidity]] — the microstructure concept. Liquidity risk is what happens when liquidity fails.
- [[Market Impact]] — cost of trading large positions, directly related.
- [[Slippage]] — execution consequence of liquidity risk.
- [[Volatility]] — vol and liquidity are inversely correlated. High vol = low liquidity = high liquidity risk.
- [[Structural Break]] — liquidity can change structurally (regulation, exchange rule changes, participant exit).
- [[Hedging]] — hedges only work if both legs can be traded. Liquidity risk is the primary threat to hedged positions.

## Common misconceptions

**"Spread trades have no liquidity risk."** Spread trades have a different liquidity risk: you cannot exit both legs simultaneously or at fair value. Often worse than directional risk because the hedge unravels.

**"I can always get out at the bid."** In a crisis, the bid disappears. The order book empties. The liquidity on screen was mostly passive makers who pull when vol spikes.

**"Exchange traded instruments are always liquid."** Exchange traded means standardized and centrally cleared, not necessarily liquid. Many listed months have negligible volume. Even the most liquid contracts go illiquid during circuit breakers, halts, or flash crashes.

## Sources

- Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity" (2009, Review of Financial Studies)
- LME Nickel crisis post-mortem reports (2022)
- CME Group: margin and risk management documentation
