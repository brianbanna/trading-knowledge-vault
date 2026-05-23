---
aliases: [notional, notional value, face value, nominal value]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Notional

## Definition
The notional is the face value of a trade, the reference amount on which payments and [[PnL]] are calculated. "I traded 10 million EUR/USD" means the 10 million euros is the notional, not that 10 million in cash changed hands. In [[Futures Contract]]s, notional = contract size × price. In [[FX Swap]]s and [[Forward Contract]]s, notional is the principal exchanged. It scales everything: your risk, your margin, your profit and loss.

## Why it matters (commodities and FX)
Every risk metric depends on notional. [[PnL]] per [[Pip]] in FX is directly proportional. A 1 pip move on 1M EUR/USD is 100 USD. The same move on 100M is 10,000 USD. In commodities, a WTI [[Futures Contract]] has notional = 1,000 barrels × price, so at 80 USD/bbl, 1 contract = 80,000 USD notional. Aggregating notional across the book tells you total exposure, the starting point for all [[Mark to Market]] and risk work.

## Concrete example

**Concrete:** You go [[Long]] 5M EUR/USD at 1.0800. The [[Spot Rate]] moves to 1.0850, a 50 [[Pip]] gain. [[PnL]] = 5,000,000 × 0.0050 = 25,000 USD. The notional turns 50 pips into the dollar amount. Fat finger case: same position but the trader entered 50M instead of 5M. The 50 pip adverse move now costs 250,000 USD, 10x larger. Notional errors are among the most common and costly mistakes on a trading floor; they show up in operational risk reports as fat finger incidents.

**Simplified:** The size of your trade, in the base asset's units. 10M EUR/USD = 10 million euros. 100 lots of WTI = 100,000 barrels. PnL = notional × price move. Bigger notional means bigger PnL in both directions. Almost every trading mistake is somehow a notional error.

## Key mechanics and formulas
- FX notional PnL: PnL = Notional × (Exit Price minus Entry Price)
  - Notional: face value in the base [[Currency Pair]] currency
- Futures notional: Notional = Number of Contracts × Contract Multiplier × Price
  - Contract Multiplier: units per contract (1,000 barrels for WTI, 5,000 bushels for corn)
  - Price: current futures price
- Gross notional: sum of absolute notional across all [[Position]]s (ignores direction)
- Net notional: sum of signed notional ([[Long]] positive, [[Short]] negative)

## Prerequisites
- [[Currency Pair]]
- [[Futures Contract]]
- [[Pip]]

## Related concepts (learn next)
- [[Position]], the directional holding whose size is defined by notional
- [[Leverage]], because notional is usually much larger than margin posted
- [[Mark to Market]], which revalues notional at current prices daily
- [[Margin]], the cash collateral required as a fraction of notional
- [[PnL]], profit or loss calculated from notional
- [[DV01]], dollar value of a 1 [[Basis Point]] move, scaled by notional
- [[Contract Specifications]], which define notional per contract

## Common misconceptions
- **Notional is not money at risk.** A 100M FX trade might require 2M in [[Margin]]. Notional measures exposure, not capital deployed.
- **Notional is not market value.** A [[Futures Contract]] at initiation has zero market value (no cash changes hands) but notional in the millions.
- **Adding notionals across instruments without risk adjustment is misleading.** 10M EUR/USD and 10M USD/TRY have vastly different risk despite identical notionals.

## Sources
- Hull, J. *Options, Futures, and Other Derivatives*, 11th ed., Chapter 2
- CME Group, "Understanding Notional Value"
- BIS, "OTC Derivatives Statistics" (notional outstanding methodology)
