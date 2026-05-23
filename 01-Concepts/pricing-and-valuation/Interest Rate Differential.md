---
aliases: [interest rate differential, rate differential, IRD]
tags:
  - "#fx"
  - "#rates"
date-added: "2026-03-20"
---

# Interest Rate Differential

## Definition
The interest rate differential (IRD) is the difference between benchmark rates of 2 countries whose currencies form a [[Currency Pair|currency pair]]. The single most important fundamental driver of FX forward pricing and a key input to [[Carry Trade|carry trade]] strategies. Measured using short term rates (OIS, 3 month SOFR/LIBOR, central bank policy rates) for near term forwards and government bond yields for longer tenors. A widening IRD in favor of 1 currency increases its forward discount or premium, and spot often appreciates as capital flows toward the higher yield. The IRD is the bridge connecting monetary policy to exchange rate behavior.

## Why it matters (commodities and FX)
Commodity firms hedging future FX exposure pay or receive the IRD through [[Forward Points|forward points]]. A Canadian oil producer selling USD forward against CAD at 6 months receives or pays points driven by the US/Canada rate differential. If US rates are 100 bps above Canadian, the forward USD/CAD is below spot (USD at discount), benefiting the producer selling USD forward. For FX traders, monitoring IRD changes is critical: a hawkish central bank surprise shifts the IRD and can move spot by hundreds of [[Pip|pips]] in a session.

## Concrete example
**Concrete:** 2023. Fed funds 5.25%, BOJ −0.10%, USD/JPY IRD of 5.35%. This translates to roughly 2,000 forward points of USD premium over 1 year (USD/JPY forward ~2 yen above spot). A carry trader long USD/JPY at 145.00 earns ~5.35% annualized carry. January 2024: BOJ signals normalization. USD/JPY drops from 148 to 141 in 2 weeks as the market reprices a narrower IRD. The 7 yen (700 pip) spot loss dwarfs months of carry income, showing that IRD direction matters more than IRD level.

**Simplified:** Two currencies, two interest rates. The gap between those rates is the IRD. If you hold the higher rate currency, you earn the gap. If you hedge forward, you pay or receive the gap baked into forward points. The catch: when the market expects the gap to narrow, the high yield currency drops fast and erases years of carry. Trading the IRD is trading the direction of central bank policy spreads, not the absolute level.

## Key mechanics and formulas
- **IRD** = Interest rate (currency A) − Interest rate (currency B).
- **Forward rate:** Forward = Spot × (1 + Rate_quote × days/360) / (1 + Rate_base × days/360). Forward premium or discount driven entirely by IRD.
- **Carry (annualized):** Approximately equal to IRD for short tenors. USD rate 5.25%, JPY rate 0.10%, carry on long USD/JPY ≈ 5.15%.
- **Forward points (approx):** Forward points ≈ Spot × (Rate_quote − Rate_base) × days / 360.
- **2 year rate differential:** A better predictor of FX trends than the overnight rate differential because it captures expected policy paths.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]
- [[Forward Points]]

## Related concepts (learn next)
- [[Forward Points]]: the direct market expression of the IRD, quoted in pips.
- [[Covered Interest Parity]]: the no arbitrage condition linking spot, forward, and rates.
- [[Uncovered Interest Parity]]: theory that IRD should predict future spot depreciation of the high rate currency (empirically fails).
- [[Carry Trade]]: long high rate, short low rate, capturing the IRD.
- [[Monetary Policy Divergence]]: when central banks move rates in opposite directions, IRD widens and FX trends accelerate.
- [[Cross Currency Basis]]: a premium or discount on top of the IRD reflecting funding stress.
- [[Carry Unwind]]: when IRD positions are liquidated en masse, spot moves violently against the carry direction.

## Common misconceptions

**"Higher rates always mean a stronger currency."** A high rate can reflect high inflation and economic instability (TRY, ARS). Rates must be evaluated in real terms and against market expectations.

**"The IRD is static."** It is dynamic. What matters for FX is not the current level but the expected change. A narrowing IRD weakens a high yield currency even if the rate is still higher.

**"Only the overnight rate matters."** The FX market prices the entire curve. A shift in 2 year swap rate expectations moves spot more than an actual overnight change that was already priced in.

## Sources
- Engel, Charles, "The Forward Discount Anomaly and the Risk Premium," Handbook of International Economics, 2014.
- Clarida, Richard et al., "Monetary Policy Rules and Macroeconomic Stability," Quarterly Journal of Economics, 2000.
- BIS Quarterly Review, "Dollar Funding and Interest Rate Parity."
