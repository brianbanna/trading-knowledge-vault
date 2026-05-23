---
aliases: [VVIX, CBOE VVIX, vol of vol index, VIX of VIX]
tags:
  - "#equities/indices"
  - "#risk"
  - "#quant"
date-added: "2026-05-23"
---

# VVIX

## Definition

VVIX is the CBOE's index of the implied volatility of [[VIX]] options. Plain English: VIX tells you how much SPX is expected to move. VVIX tells you how much VIX itself is expected to move. The vol of the vol gauge. VVIX is computed with the same model free, integrated OTM option formula as VIX, applied to VIX options. The output is annualized, percentage based, and trades in the 70 to 140 range, well above VIX because vol of an already volatile series compounds.

Conceptually it is the market's price for [[Vol of Vol]], the second moment of the vol distribution. High VVIX means the market is paying up for protection against VIX spikes (long VIX calls, long volatility options).

## Why it matters (commodities and FX)

VVIX is the cleanest publicly available proxy for systemic tail risk premium. When VVIX is high while VIX is low, the market is calm on the surface but paying up for tail insurance. This divergence preceded several VIX explosions (February 2018, March 2020 early signals).

For a commodities or FX trader who does not directly trade VIX products, VVIX still matters:

- VVIX leads [[Carry Unwind|carry unwinds]] more reliably than VIX. A rising VVIX with flat VIX suggests dealers and hedge funds are quietly hedging tails, which precedes risk off rotation that crushes [[USDMXN]] short, [[USDZAR]] short, EM equity longs.
- VVIX informs the cost of tail hedging in commodity vol (OVX, GVZ). When VVIX is elevated, commodity dealers widen wings and skew steepens in [[Brent Crude]] and [[Henry Hub Natural Gas]] options.
- VVIX is the [[Volga]] price signal for equity. Long volga positions ([[Butterfly|butterflies]], [[Strangle|strangles]]) get expensive when VVIX is high, cheap when low.

VVIX is also the input to dispersion trading and tail hedge fund strategies. Pierre Andurand and other macro/commodity traders watch VVIX to time cheap [[Brent Crude]] tail upside via long dated calls.

## Concrete example

**Concrete:** Calm August. VIX at 13.5 near multi year lows, SPX at all time highs. Trader is long $5M [[USDMXN]] short MXN carry earning ~6% annual. VVIX prints 122 vs a 90 day average of 95. Reading: someone is paying up for VIX calls while spot vol is asleep. Action: cut MXN carry 40% and add a long [[USDJPY]] short USDJPY put hedge (cheap because realized vol is low). 2 weeks later: weak China PMI + hawkish Fed. VIX explodes from 13.5 to 28, MXN drops 3.5%. Carry book loses 1.4% instead of 3.5%, saving $105,000 on $5M. USDJPY put hedge gains 90% on premium.

**Simplified:** VIX tells you how anxious the market is now. VVIX tells you whether someone is quietly buying tail insurance for next month. If VVIX is high while VIX is calm, somebody big is hedging. That is usually an early warning that a vol shock is being priced in but has not hit yet. Cut carry, buy cheap tail hedges, and wait. The signal is not perfect but the cost of acting on it is low because regular options are cheap when realized vol is calm.

## Key mechanics and formulas

**Calculation:** Same model free integrated OTM option formula as [[VIX]], applied to VIX options across the front 2 expiries (30 day target).

`VVIX² = (2/T) × Σ (ΔK_i / K_i²) × e^(rT) × Q(K_i) − (1/T) × (F/K_0 − 1)²`

where Q(K_i) are VIX option mid prices, not SPX option mid prices.

**Typical levels:**
- <80: extreme complacency in vol space
- 80 to 100: low vol of vol regime
- 100 to 120: normal
- 120 to 140: elevated tail hedging
- >140: stress, often with VIX > 25
- Peaks: 200+ during March 2020 panic and February 2018 Volmageddon

**Useful ratios and signals:**

`VVIX / VIX`: normalized tail premium. High ratio (e.g. >8) signals tail hedging dominant relative to spot vol level.

`Δ VVIX / Δ VIX`: VVIX move per point of VIX move. Persistently high beta = market repricing tail distribution wider, not just moving along existing distribution.

**Vol of vol vs volga:** VVIX measures actual or expected vol of vol. [[Volga]] is a greek measuring option price sensitivity to vol changes. VVIX is observable; volga is a model output.

**Term structure:** VVIX has its own forward curve (less commonly traded than VX). Slope provides information on whether the tail bid is short term or persistent.

## Prerequisites
- [[VIX]]
- [[Vol of Vol]]
- [[Implied Volatility]]
- [[Option]]
- [[Vega]]

## Related concepts (learn next)
- [[VIX]] - VVIX is meaningless without the underlying VIX construction.
- [[Vol of Vol]] - the conceptual framework. VVIX is one implementation for equity index vol.
- [[Volga]] - the greek that captures price sensitivity VVIX is pricing.
- [[Vol Surface]] - SPX surface curvature (smile/skew) is partly driven by what VVIX implies about tails.
- [[Risk-On Risk-Off]] - VVIX often gives earlier RORO signals than VIX, especially distinguishing complacency from genuine calm.
- [[Carry Unwind]] - VVIX spikes ahead of VIX often coincide with the first leg of carry unwinds.
- [[0DTE]] - 0DTE dominance has distorted the VVIX/realized VIX move relationship, since 0DTE flow does not feed VVIX directly.

## Common misconceptions

**"VVIX going up means VIX is going up."** Not necessarily. VVIX can rise while VIX stays flat or falls. That is the most informative scenario: traders are paying up for vol upside while spot vol is calm.

**"VVIX is just VIX squared or a derived number."** It is independently computed from VIX options market prices using the VIX formula structure. A market data point, not a transformation.

**"You can trade VVIX directly."** No. No VVIX futures or ETPs exist. To express a vol of vol view, trade VIX options ([[Butterfly|butterflies]] for pure volga, [[Strangle|strangles]] for vol of vol + direction), or SPX butterflies further out the surface.

**"High VVIX is a sell signal for equities."** A probability shift, not deterministic. Many VVIX spikes resolve without a VIX explosion. Base rate matters: VVIX > 130 is stronger when combined with rising [[Realized Volatility]] or widening credit spreads.

## Sources

- CBOE: VVIX methodology document. Available on cboe.com.
- Park, Yang Ho. "Volatility of Volatility and Tail Risk Premiums." Journal of Financial Econometrics, 2015.
- Bardgett, Gourier, Leippold. "Inferring volatility dynamics and risk premia from the S&P 500 and VIX markets." Journal of Financial Economics, 2019.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley. Chapter on vol of vol.
