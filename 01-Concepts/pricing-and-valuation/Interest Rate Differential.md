---
aliases: [interest rate differential, rate differential, IRD]
tags:
  - "#fx"
  - "#rates"
date-added: "2026-03-20"
---

# Interest Rate Differential

## Definition
The interest rate differential (IRD) is the difference between the benchmark interest rates of 2 countries whose currencies form a [[Currency Pair|currency pair]]. It is the single most important fundamental driver of FX forward pricing and a key input to [[Carry Trade|carry trade]] strategies. The IRD is typically measured using short term rates (overnight index swap rates, 3 month LIBOR/SOFR, or central bank policy rates) for near term forwards and government bond yields for longer tenors. When the IRD widens in favor of 1 currency, that currency's forward discount (or premium) increases, and spot often appreciates as capital flows toward the higher yield. The IRD is the bridge connecting monetary policy to exchange rate behavior.

## Why it matters (commodities and FX)
Commodity firms that hedge future FX exposure pay or receive the IRD through [[Forward Points|forward points]]. A Canadian oil producer selling USD forward against CAD at a 6 month tenor receives or pays points driven by the US/Canada rate differential. If US rates are 100 basis points above Canadian rates, the forward USD/CAD will be below spot (USD trades at a discount), benefiting the producer selling USD forward. For FX traders, monitoring IRD changes is critical: a central bank that surprises hawkish shifts the IRD and can move spot by hundreds of [[Pip|pips]] in a session.

## Concrete example
In 2023, the Fed funds rate sits at 5.25% while the Bank of Japan holds at −0.10%, creating an IRD of 5.35% on USD/JPY. This massive differential manifests as roughly 2,000 forward points of USD premium over 1 year (USD/JPY forward is ~2 yen above spot). A carry trader who is long USD/JPY at 145.00 earns approximately 5.35% annualized carry. However, in January 2024, the BOJ signals normalization, and USD/JPY drops from 148 to 141 in 2 weeks as the market reprices a narrower IRD. The 7 yen (700 pip) spot loss dwarfs months of carry income, demonstrating that IRD direction matters more than IRD level.

## Key mechanics and formulas
- **IRD** = Interest rate (currency A) − Interest rate (currency B).
- **Forward rate derivation**: Forward = Spot × (1 + Rate_quote × days/360) / (1 + Rate_base × days/360). The forward premium or discount is driven entirely by the IRD.
- **Carry (annualized)**: Approximately equal to the IRD for short tenors. If USD rate = 5.25% and JPY rate = 0.10%, carry on long USD/JPY ≈ 5.15%.
- **Forward points (approximate)**: Forward points ≈ Spot × (Rate_quote − Rate_base) × days / 360.
- **2 year rate differential**: Often a better predictor of spot FX trends than the overnight rate differential because it captures expected policy paths.

## Prerequisites
- [[Currency Pair]]
- [[Spot Rate]]
- [[Forward Points]]

## Related concepts (learn next)
- [[Forward Points]]: the direct market expression of the IRD, quoted in pips and added to or subtracted from spot.
- [[Covered Interest Parity]]: the no arbitrage condition linking spot, forward, and interest rates across currencies.
- [[Uncovered Interest Parity]]: the theory that the IRD should predict future spot depreciation of the high rate currency (empirically fails).
- [[Carry Trade]]: the strategy of going long the high rate currency and short the low rate currency to capture the IRD.
- [[Monetary Policy Divergence]]: when central banks move rates in opposite directions, the IRD widens and FX trends accelerate.
- [[Cross Currency Basis]]: a premium or discount on top of the IRD that reflects funding stress and supply/demand for currency swaps.
- [[Carry Unwind]]: when IRD positions are liquidated en masse, spot moves violently against the carry direction.

## Common misconceptions
1. **Higher rates always mean a stronger currency**: A high rate may reflect high inflation and economic instability (e.g., TRY, ARS). Rates must be evaluated in real terms and relative to market expectations.
2. **The IRD is static**: The IRD is dynamic. What matters for FX is not the current level but the expected change. A narrowing IRD can weaken a high yield currency even if its rate is still higher.
3. **Only the overnight rate matters**: The FX market prices the entire rate curve. A shift in 2 year swap rate expectations can move spot more than an actual overnight rate change if the change was already priced in.

## Sources
- Engel, Charles, "The Forward Discount Anomaly and the Risk Premium," Handbook of International Economics, 2014.
- Clarida, Richard et al., "Monetary Policy Rules and Macroeconomic Stability," Quarterly Journal of Economics, 2000.
- BIS Quarterly Review, "Dollar Funding and Interest Rate Parity."
