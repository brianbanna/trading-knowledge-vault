---
aliases: [forward points, swap points, FX forward points]
tags:
  - "#fx"
date-added: "2026-03-20"
---

# Forward Points

## Definition
Forward points (swap points) are the [[Pip|pips]] added to or subtracted from the [[Spot Rate|spot rate]] to derive the forward rate for a given delivery date. They reflect the [[Interest Rate Differential|interest rate differential]] between the 2 currencies in the [[Currency Pair|pair]], adjusted for time to maturity. When the base currency has the higher rate, forward points are negative (base trades at a forward discount). When the base has the lower rate, forward points are positive (forward premium). Quoted for standard tenors (overnight, 1W, 1M, 2M, 3M, 6M, 1Y) and are the building blocks for [[FX Swap|FX swap]] and outright forward pricing.

## Why it matters (commodities and FX)
Forward points set the cost or benefit of hedging future FX exposure. A commodity exporter selling crude in USD who hedges by selling USD/CAD 6 months forward receives or pays the points, directly affecting the hedge rate. If forward points are −80 on 1.3600 spot, the 6 month forward is 1.3520: the hedger locks in 80 pips worse than spot. For carry traders, forward points are the carry. Earning positive points on a long position equals earning the rate differential. Essential for anyone rolling FX positions, since roll cost or benefit accrues through the swap points paid at each roll.

## Concrete example
**Concrete:** EUR/USD spot 1.0800. US 6 month rate 5.00%, EUR 6 month rate 3.00%. Forward points ≈ 1.0800 × (0.03 − 0.05) × 0.5 / (1 + 0.05 × 0.5) = −0.01054, or ~−105 pips. 6 month forward = 1.0800 − 0.0105 = 1.0695. A European company hedging 10M USD receivable sells USD / buys EUR forward at 1.0695 instead of spot at 1.0800, receiving 105 fewer pips per EUR. Over 1 year this cost equals the 200 bps rate differential. If unhedged and EUR/USD moves to 1.1200, spot would have won. If EUR/USD falls to 1.0400, the 1.0695 forward outperforms.

**Simplified:** A forward exchange rate is not a prediction. It is spot adjusted for the rate gap between the 2 currencies so no risk free arbitrage exists. If dollars pay 5% and euros pay 3%, a 6 month forward EUR/USD has to be lower than spot by roughly the rate gap. Those pips of adjustment are forward points. If you hedge by buying or selling forward, you are paying or receiving the rate differential, not predicting anything.

## Key mechanics and formulas
- **Forward rate:** F = S × (1 + r_quote × t) / (1 + r_base × t).
- **Forward points:** FP = F − S = S × [(r_quote − r_base) × t] / (1 + r_base × t).
- **Sign:** Positive = forward > spot (base at premium). Negative = forward < spot (base at discount).
- **Bid/offer:** Forward bid = Spot bid + Points bid; Forward offer = Spot offer + Points offer.
- **Annualized carry:** Carry (%) ≈ (Forward points / Spot) / Time fraction × 100.
- **Broken dates:** Non standard tenors are interpolated linearly between surrounding standard points.
- **Tom/Next (T/N):** 1 day forward point used to roll spot positions; accrues daily to holders.

## Prerequisites
- [[Spot Rate]]
- [[Interest Rate Differential]]
- [[Pip]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Covered Interest Parity]]: theoretical foundation that forward points equal the rate differential (up to the [[Cross Currency Basis|basis]]).
- [[FX Swap]]: the instrument trading forward points; near leg is spot, far leg is forward.
- [[Cross Currency Basis]]: deviation from CIP embedded in actual forward points beyond the pure rate differential.
- [[NDF]]: forward points for non deliverable currencies, cash settled.
- [[Carry Trade]]: forward points are the carry earned or paid.
- [[Interest Rate Differential]]: the fundamental driver of forward points.
- [[Uncovered Interest Parity]]: if UIP held, forward points would predict future spot; empirically they do not.

## Common misconceptions

**"Forward points predict where spot is going."** They reflect rate differentials, not directional expectations. Negative 100 pips does not mean spot will fall 100 pips.

**"Forward points are a broker fee."** Points are a mathematical consequence of rate differentials. They exist identically in the interbank market and are not a fee.

**"Larger forward points mean worse hedging outcomes."** Negative forward points on USD (when US rates are higher) benefit USD sellers hedging forward. Sign depends on direction: a cost for one party is a benefit for the counterparty.

## Sources
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
- BIS, "Triennial Central Bank Survey," 2022.
- Reuters, "FX Forward Points: Market Conventions and Calculations."
