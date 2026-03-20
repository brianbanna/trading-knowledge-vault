---
aliases: [liquidity risk, liquidity mismatch, illiquidity risk, funding liquidity]
tags:
  - "#risk"
  - "#microstructure"
date-added: "2026-03-20"
---

# Liquidity Risk

## Definition

Liquidity risk is the risk that you cannot exit or adjust a position at a reasonable price when you need to. It has 2 dimensions: market liquidity risk (the asset itself is hard to trade without moving the price) and funding liquidity risk (you cannot meet margin calls or collateral requirements, forcing liquidation at unfavorable prices). Both dimensions interact: when [[Volatility]] spikes, market liquidity dries up AND margin requirements increase, creating a vicious cycle. Liquidity risk is the risk that turns a manageable loss into a catastrophic one.

## Why it matters (commodities and FX)

Commodity markets have highly uneven [[Liquidity]]. The [[Front Month]] of [[WTI Crude Oil]] trades 500,000+ contracts/day. The 18th month trades maybe 5,000. A [[Calendar Spread]] with one leg in an illiquid month faces liquidity mismatch: you can exit one leg easily but not the other. In a fast market, this mismatch can turn a hedged position into a naked directional bet.

[[Relative Value Trade|Spread trades]] are particularly exposed to liquidity risk because they rely on both legs being tradeable simultaneously. If one leg freezes (exchange halt, margin call cascade, counterparty failure), the spread unravels. This is exactly what happened to many firms during the 2022 LME nickel squeeze: the exchange halted nickel trading for a week, leaving hedged positions (long nickel, short another metal) with one leg locked while the other moved freely.

## Concrete example

**LME Nickel (March 2022):** A massive short squeeze drove nickel from $25,000/tonne to over $100,000/tonne in hours. The LME halted trading and cancelled trades. Firms with hedged positions (e.g., long copper / short nickel as a relative value spread) could not exit their nickel leg. Copper continued trading and fell as broader risk off hit metals. The "hedged" spread position became a naked short copper position, generating enormous losses from a trade designed to be market neutral.

**Funding liquidity example:** A trader holds a profitable calendar spread in [[Henry Hub Natural Gas]], long Dec / short Mar. A margin call from a losing position elsewhere forces the trader to liquidate. The Dec contract is liquid but the Mar position is in a thinner month. The trader dumps Dec easily but Mar can only be sold at a 3 tick discount to fair value, erasing profit and adding [[Slippage]].

## Key mechanics and formulas

**Liquidity risk dimensions:**

| Type | Definition | Measurement |
|------|-----------|-------------|
| Market liquidity | Ability to trade without price impact | [[Bid-Ask Spread]], depth, [[Market Impact]] |
| Funding liquidity | Ability to meet margin/collateral needs | Margin utilization, cash buffer, credit lines |

**Liquidity adjusted VaR:**
`LVaR = VaR + (0.5 x Bid-Ask Spread x Position Size)`

Adds the cost of liquidation to the standard risk measure.

**Days to liquidate:**
`Days = Position Size / (ADV x Participation Rate)`

If you hold 10,000 WTI contracts and average daily volume is 500,000, at 5% participation rate, you need 10,000 / 25,000 = 0.4 days. If you hold 10,000 contracts in a thin month with ADV of 5,000, you need 10,000 / 250 = 40 days.

**Liquidity mismatch score:**
`Mismatch = Max(Days to Liquidate across legs) / Min(Days to Liquidate across legs)`

A mismatch score >5x is a red flag for spread trades.

## Prerequisites
- [[Liquidity]]
- [[Bid-Ask Spread]]
- [[Volatility]]

## Related concepts (learn next)
- [[Liquidity]] - the market microstructure concept. Liquidity risk is what happens when liquidity fails.
- [[Market Impact]] - the cost of trading large positions. Directly related to liquidity risk.
- [[Slippage]] - the execution consequence of liquidity risk.
- [[Volatility]] - vol and liquidity are inversely correlated. High vol = low liquidity = high liquidity risk.
- [[Structural Break]] - liquidity can structurally change (new regulation, exchange rule changes, market participant exit).
- [[Hedging]] - hedges only work if both legs can be traded. Liquidity risk is the primary risk to hedged positions.

## Common misconceptions

**"Spread trades have no liquidity risk."** Spread trades have DIFFERENT liquidity risk: the risk that you cannot exit both legs simultaneously or at fair value. This is often worse than directional liquidity risk because the hedge unravels.

**"I can always get out at the bid."** In a crisis, the bid disappears. The order book empties. The "liquidity" you saw on screen was mostly passive market makers who pull their quotes when vol spikes.

**"Exchange traded instruments are always liquid."** Exchange traded means standardized and centrally cleared, not necessarily liquid. Many listed futures months have negligible volume. Even the most liquid contracts can become illiquid during circuit breakers, exchange halts, or flash crashes.

## Sources

- Brunnermeier and Pedersen, "Market Liquidity and Funding Liquidity" (2009, Review of Financial Studies)
- LME Nickel crisis post-mortem reports (2022)
- CME Group: margin and risk management documentation
