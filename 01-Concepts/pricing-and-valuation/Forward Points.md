---
aliases: [forward points, swap points, FX forward points]
tags:
  - "#fx"
date-added: "2026-03-20"
---

# Forward Points

## Definition
Forward points (also called swap points) are the number of [[Pip|pips]] added to or subtracted from the [[Spot Rate|spot rate]] to derive the forward exchange rate for a given delivery date. They reflect the [[Interest Rate Differential|interest rate differential]] between the 2 currencies in the [[Currency Pair|pair]], adjusted for the time to maturity. When the base currency has a higher interest rate than the quote currency, the forward points are negative (the base trades at a forward discount). When the base currency has a lower rate, forward points are positive (forward premium). Forward points are quoted in the market for standard tenors (overnight, 1 week, 1 month, 2 months, 3 months, 6 months, 1 year) and are the building blocks for [[FX Swap|FX swap]] and outright forward pricing.

## Why it matters (commodities and FX)
Forward points determine the cost or benefit of hedging future FX exposures. A commodity exporter selling crude in USD who hedges by selling USD/CAD forward 6 months out receives or pays forward points that directly affect the effective hedge rate. If forward points are −80 on a 1.3600 spot, the 6 month forward is 1.3520, meaning the hedger locks in a rate 80 pips worse than spot. For carry traders, forward points represent the carry: earning positive points on a long position is equivalent to earning the interest rate differential. Understanding forward points is essential for anyone rolling FX positions, as the roll cost or benefit accrues through the swap points paid at each roll date.

## Concrete example
EUR/USD spot is 1.0800. US 6 month rate is 5.00%, EUR 6 month rate is 3.00%. Forward points ≈ 1.0800 × (0.03 − 0.05) × 0.5 / (1 + 0.05 × 0.5) = 1.0800 × (−0.01) / 1.025 = −0.01054, or approximately −105 pips. The 6 month forward is 1.0800 − 0.0105 = 1.0695. A European company hedging 10 million USD receivable sells USD / buys EUR forward at 1.0695 instead of spot at 1.0800, receiving 105 fewer pips per EUR. Over 1 year, this cost equals the 200 bps rate differential. If the company had not hedged and EUR/USD moved to 1.1200, the spot outcome would have been better, but the hedge provided certainty. Conversely, if EUR/USD fell to 1.0400, the forward at 1.0695 far outperformed spot.

## Key mechanics and formulas
- **Forward rate**: F = S × (1 + r_quote × t) / (1 + r_base × t).
- **Forward points**: FP = F − S = S × [(r_quote − r_base) × t] / (1 + r_base × t).
- **Sign convention**: Positive points mean the forward rate > spot (base currency at premium). Negative points mean forward < spot (base at discount).
- **Bid/offer on points**: The forward spread is the spot spread plus the swap spread. Forward bid = Spot bid + Points bid; Forward offer = Spot offer + Points offer.
- **Annualized carry from points**: Carry (%) ≈ (Forward points / Spot) / Time fraction × 100.
- **Broken dates**: Non standard tenors are interpolated linearly between the 2 surrounding standard tenor points.
- **Tom/Next (T/N)**: The 1 day forward point used to roll spot positions; accrues daily to holders of open positions.

## Prerequisites
- [[Spot Rate]]
- [[Interest Rate Differential]]
- [[Pip]]
- [[Currency Pair]]

## Related concepts (learn next)
- [[Covered Interest Parity]]: the theoretical foundation guaranteeing forward points equal the rate differential (up to the [[Cross Currency Basis|basis]]).
- [[FX Swap]]: the instrument through which forward points are traded; the near leg is spot and the far leg is the forward.
- [[Cross Currency Basis]]: the deviation from CIP embedded in actual forward points beyond the pure rate differential.
- [[NDF]]: forward points for non deliverable currencies, where the forward is cash settled rather than physically delivered.
- [[Carry Trade]]: forward points represent the carry earned or paid; positive points = earning carry on a long base position.
- [[Interest Rate Differential]]: the fundamental driver of forward points.
- [[Uncovered Interest Parity]]: if UIP held, forward points would be an unbiased predictor of future spot; they are not.

## Common misconceptions
1. **Forward points predict where spot is going**: Forward points reflect interest rate differentials, not market expectations of future spot direction. A negative 100 pip forward does not mean the market expects spot to fall 100 pips.
2. **Forward points are a cost imposed by the broker**: Points are a mathematical consequence of interest rate differentials. They exist in the interbank market identically and are not a fee.
3. **Larger forward points always mean worse hedging outcomes**: Negative forward points on USD (when US rates are higher) benefit USD sellers hedging forward. The sign depends on your direction: what is a cost for one party is a benefit for the other.

## Sources
- Hull, John C., *Options, Futures, and Other Derivatives*, 11th ed.
- BIS, "Triennial Central Bank Survey," 2022.
- Reuters, "FX Forward Points: Market Conventions and Calculations."
