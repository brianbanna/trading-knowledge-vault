---
aliases: [notional, notional value, face value, nominal value]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Notional

## Definition
The notional is the face value of a trade, the reference amount on which payments and [[PnL]] are calculated. When someone says "I traded 10 million EUR/USD," the 10 million euros is the notional. It does not mean 10 million changed hands in cash. In [[Futures Contract]]s, the notional is the contract size times the price. In [[FX Swap]]s and [[Forward Contract]]s, the notional is the principal amount exchanged. It is the number that scales everything: your risk, your margin, and your profit or loss.

## Why it matters (commodities and FX)
Every risk metric depends on notional. Your [[PnL]] per [[Pip]] in FX is directly proportional to the notional. A 1 pip move on 1 million EUR/USD is 100 USD. The same move on 100 million is 10,000 USD. In commodities, a [[Futures Contract]] on WTI crude has a notional of 1,000 barrels times the price, so at 80 USD per barrel, 1 contract is 80,000 USD notional. Knowing your aggregate notional across the book tells you your total exposure, which is the starting point for all [[Mark to Market]] and risk calculations.

## Concrete example
**Win scenario:** You go [[Long]] 5 million EUR/USD at 1.0800. The [[Spot Rate]] moves to 1.0850, a gain of 50 [[Pip]]s. Your [[PnL]] = 5,000,000 x 0.0050 = 25,000 USD. The notional (5 million EUR) is what turns a 50 pip move into a dollar amount.

**Fail scenario:** Same [[Position]], but the rate drops to 1.0750, a loss of 50 pips. Your [[PnL]] = 5,000,000 x (negative 0.0050) = negative 25,000 USD. The notional works identically in both directions. A junior trader who accidentally enters 50 million instead of 5 million has 10x the loss: negative 250,000 USD. Fat finger errors on notional are among the most common and costly mistakes.

## Key mechanics and formulas
- FX notional PnL: PnL = Notional x (Exit Price minus Entry Price)
  - Notional: the face value in the base [[Currency Pair]] currency
- Futures notional: Notional = Number of Contracts x Contract Multiplier x Price
  - Contract Multiplier: units per contract (1,000 barrels for WTI, 5,000 bushels for corn)
  - Price: current futures price
- Gross notional: sum of absolute notional across all [[Position]]s (ignores direction)
- Net notional: sum of signed notional ([[Long]] positive, [[Short]] negative)

## Prerequisites
- [[Currency Pair]]
- [[Futures Contract]]
- [[Pip]]

## Related concepts (learn next)
- [[Position]] , the directional holding whose size is defined by notional
- [[Leverage]] , because notional is usually much larger than the margin posted
- [[Mark to Market]] , which revalues the notional at current prices daily
- [[Margin]] , the cash collateral required as a fraction of the notional
- [[PnL]] , the profit or loss calculated from the notional
- [[DV01]] , the dollar value of 1 [[Basis Point]] move, scaled by notional
- [[Contract Specifications]] , which define the notional per contract

## Common misconceptions
- **Notional is not the amount of money at risk.** A 100 million notional FX trade might require only 2 million in [[Margin]]. The notional measures exposure, not capital deployed.
- **Notional is not the same as market value.** For a [[Futures Contract]] at initiation, market value is zero (no money changes hands), but the notional can be millions.
- **Adding notionals across different instruments without adjusting for risk is misleading.** 10 million in EUR/USD and 10 million in USD/TRY have vastly different risk profiles despite identical notionals.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Understanding Notional Value"
- BIS, "OTC Derivatives Statistics" (notional outstanding methodology)
