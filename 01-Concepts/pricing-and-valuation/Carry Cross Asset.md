---
aliases: [cross asset carry, carry factor, systematic carry]
tags:
  - "#quant"
  - "#macro"
date-added: "2026-03-20"
---

# Carry Cross Asset

## Definition
Cross asset carry is a systematic factor capturing the return from holding a higher yielding asset funded by a lower yielding one, applied consistently across FX, fixed income, commodities, and equities. In FX, carry is the rate differential: long high rate currency (BRL, MXN), short low rate (JPY, CHF). In commodities, carry is the [[roll yield]]: long backwardated curves, short contangoed ones. In bonds, carry is the yield pickup: long duration funded at the short rate. Carry is one of the oldest and most persistent risk premia, with positive average returns over decades punctuated by severe drawdowns ("crash risk"). It harvests mechanically without forecasting ability, a foundational building block for [[CTA]] and quant macro strategies.

## Why it matters (commodities and FX)
Carry is the most studied and traded factor in FX, with trillions in positioning. The classic carry trade (long AUD, NZD, BRL vs short JPY, CHF, EUR) has averaged 4 to 6% annual returns with tail risk: 2008 saw carry portfolios lose 20 to 30% in 3 months on rapid unwinding. In commodities, roll yield is a major component of total futures return. A commodity index investor ignoring carry may hold deeply contangoed contracts (VIX futures) that bleed value. Systematic commodity funds sort markets by carry, overweighting backwardated and underweighting contangoed contracts. FX and commodity carry interact: commodity exporters (AUD, CAD, NOK) tend to have both higher rates and backwardated curves, creating reinforcing signals.

## Concrete example
**Concrete:** Systematic macro fund builds a cross asset carry portfolio. FX: long 3 highest yielding G10 (AUD 4.35%, NZD 5.50%, NOK 4.50%), short 3 lowest (JPY 0.10%, CHF 1.50%, EUR 3.75%), equal risk weighted. Commodities: long 3 most backwardated (WTI 0.8% monthly roll, copper 0.3%, live cattle 0.5%), short 3 most contangoed (natgas −1.2%, corn −0.4%, gold −0.2%). Year 1: +7.2% (3.8% FX, 3.4% commodity), 8% vol, Sharpe 0.9. Year 2: global risk off triggers simultaneous unwind. AUD −12%, crude −25%, portfolio −15% in 6 weeks. Carry pays for crash risk.

**Simplified:** Carry is the rent you collect for holding the high yielding asset and shorting the low yielding one. In FX, it is the interest rate gap. In commodities, it is the downward slope of the futures curve. In bonds, it is the yield pickup. Most of the time you earn the rent quietly. Occasionally a crash hits and everyone unwinds at once, wiping out a year of rent in weeks. The strategy works on average because investors require compensation for that tail.

## Key mechanics and formulas
- **FX carry**: Carry = r(long) − r(short); equivalently, forward discount = (F − S) / S
- **Commodity carry (roll yield)**: (near − next) / near; positive = backwardation = positive carry
- **Bond carry**: bond yield − funding rate; 10Y at 4.5% funded at 3% → carry 1.5% annualized
- **Portfolio construction**: rank assets by carry; long top quintile, short bottom quintile; equal risk weight within each leg
- **Historical Sharpe**: FX carry 0.5 to 0.8; commodity carry 0.3 to 0.6; combined cross asset 0.7 to 1.0
- **Carry to risk ratio**: annualized carry / annualized vol; tests whether compensation matches risk

## Prerequisites
- [[Interest Rate Differential]]
- [[Roll Yield]]
- [[Forward Rate]]
- [[Backwardation]]
- [[Contango]]

## Related concepts (learn next)
- [[Momentum Cross Asset]]: momentum and carry are partially offsetting; combining improves Sharpe
- [[Value Cross Asset]]: value signals (PPP in FX) filter carry trades, avoiding pairs where carry is offset by overvaluation
- [[Risk Parity]]: incorporates carry as the primary expected return source across assets
- [[CTA]]: many CTAs blend carry with trend for hybrid strategies
- [[Macro Regime]]: carry performs best in Goldilocks regimes, worst in risk off
- [[Correlation Breakdown]]: carry unwinds drive cross asset correlation spikes
- [[Positioning Signal]]: extreme carry positioning (record JPY shorts) signals elevated crash risk
- [[DXY Correlation]]: strong USD environments coincide with EM carry unwinds

## Common misconceptions
**"Carry is free money."** Returns compensate for crash risk. Average ~4 to 6%, worst drawdowns exceed 20%. Risk adjusted, carry is a modest premium, not an arbitrage.

**"CIP means FX carry should not exist."** CIP holds for hedged positions; the carry trade is unhedged. The premium compensates for adverse FX moves. Persistent carry returns violate uncovered interest parity, an empirical puzzle.

**"Commodity carry and FX carry are independent."** They correlate. Commodity exporters (AUD, CAD, NOK) have both higher rates and backwardated curves when commodity prices are high, creating a hidden correlation that amplifies drawdowns.

## Sources
- Koijen, Ralph, Moskowitz, Tobias, Pedersen, Lasse, Vrugt, Evert, "Carry," Journal of Financial Economics (2018)
- Brunnermeier, Markus, Nagel, Stefan, Pedersen, Lasse, "Carry Trades and Currency Crashes," NBER (2008)
- Erb, Claude, Harvey, Campbell, "The Strategic and Tactical Value of Commodity Futures," Financial Analysts Journal (2006)
- Asness, Clifford, Moskowitz, Tobias, Pedersen, Lasse, "Value and Momentum Everywhere," Journal of Finance (2013)
