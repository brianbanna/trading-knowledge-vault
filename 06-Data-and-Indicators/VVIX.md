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

VVIX is the CBOE's index of the implied volatility of [[VIX]] options. Plain English: VIX tells you how much SPX is expected to move. VVIX tells you how much VIX itself is expected to move. It is the "vol of the vol gauge." VVIX is calculated using the same model free, integrated OTM option formula as VIX, but applied to VIX options instead of SPX options. The output is annualized, expressed as a percentage, and typically trades in the 70 to 140 range, well above VIX itself because vol of an already volatile series compounds.

Conceptually it is the market's price for [[Vol of Vol]], the second moment of the vol distribution. High VVIX means the market is paying up for protection against VIX spikes (long VIX calls, long volatility options).

## Why it matters (commodities and FX)

VVIX is the cleanest publicly available proxy for systemic tail risk premium. When VVIX is high while VIX is low, the market is calm on the surface but paying up for tail insurance. This divergence has historically preceded several VIX explosions (February 2018, March 2020 early signals).

For a commodities or FX trader who does not directly trade VIX products, VVIX still matters:

- VVIX leads [[Carry Unwind|carry unwinds]] more reliably than VIX itself. A rising VVIX with flat VIX suggests dealers and hedge funds are quietly hedging tails. This precedes risk off rotation that crushes [[USDMXN]] short, [[USDZAR]] short, EM equity longs.
- VVIX informs the cost of tail hedging in commodity vol (OVX, GVZ). When VVIX is elevated, commodity dealers widen wing markets and skew steepens in [[Brent Crude]] and [[Henry Hub Natural Gas]] options.
- VVIX is the [[Volga]] price signal for the equity market. Long volga positions ([[Butterfly|butterflies]], [[Strangle|strangles]]) become expensive when VVIX is high and cheap when VVIX is low.

VVIX is also the input to dispersion trading and tail risk hedge fund strategies. Pierre Andurand and other macro/commodity traders watch VVIX to time when to put on cheap [[Brent Crude]] tail upside via long dated calls.

## Concrete example

It is a calm August. VIX is at 13.5, near multi year lows. SPX is at all time highs. A discretionary FX trader is long a [[USDMXN]] short MXN carry book earning ~6% annual.

The trader checks VVIX: 122, well above its 90 day average of 95. The VIX is calm, but vol of vol is bid. Reading: someone is paying up for VIX calls. Probable interpretation: dealer gamma hedging is building, or a large macro fund is putting on a tail hedge.

Action: trader cuts MXN carry by 40% and adds long [[USDJPY]] short USDJPY puts as a cheap macro tail hedge (funded by carry). Cost of the hedge is small because realized vol is low so option premiums are subdued, even though VVIX is elevated.

Two weeks later: weak China PMI plus a hawkish Fed surprise. VIX explodes from 13.5 to 28, MXN drops 3.5%. The carry book takes a 1.4% loss instead of the 3.5% it would have. The USDJPY put hedge gains 90% on premium (vega and gamma).

Outcome: VVIX was the signal, not VIX. If the trader had only watched VIX (which was asleep at 13.5), no action would have been taken and the carry book would have eaten the full unwind.

What if instead VVIX had been at 78 (low)? Reading would be complacency, no tail bid, fine to keep carry on. The signal would correctly say "no hedge needed."

## Key mechanics and formulas

**Calculation:** Same model free integrated OTM option formula as [[VIX]], applied to VIX options across the front two expiries (30 day target).

`VVIX² = (2/T) × Σ (ΔK_i / K_i²) × e^(rT) × Q(K_i) - (1/T) × (F/K_0 - 1)²`

where the Q(K_i) are VIX option mid prices, not SPX option mid prices.

**Typical levels:**
- < 80: extreme complacency in vol space
- 80 to 100: low vol of vol regime
- 100 to 120: normal
- 120 to 140: elevated tail hedging
- > 140: stress, often coincides with VIX > 25
- Peaks: 200+ during March 2020 panic and February 2018 Volmageddon

**Useful ratios and signals:**

`VVIX / VIX`: a normalized read on tail premium. High ratio (e.g. > 8) suggests tail hedging dominant relative to spot vol level.

`Δ VVIX / Δ VIX`: how much VVIX moves per point of VIX move. Persistently high beta = market repricing tail distribution wider, not just moving along existing distribution.

**Vol of vol vs volga:** VVIX measures the actual or expected volatility of vol. [[Volga]] is a greek measuring sensitivity of option price to vol changes. VVIX is observable; volga is a model output.

**Term structure:** VVIX has its own forward curve (less commonly traded than VX), and its slope provides additional information about whether the tail bid is short term or persistent.

## Prerequisites
- [[VIX]]
- [[Vol of Vol]]
- [[Implied Volatility]]
- [[Option]]
- [[Vega]]

## Related concepts (learn next)
- [[VIX]] - VVIX is meaningless without understanding the underlying VIX construction and what drives VIX dynamics.
- [[Vol of Vol]] - the conceptual framework. VVIX is one specific implementation of vol of vol for equity index vol.
- [[Volga]] - the greek that captures volga is the price sensitivity that VVIX is pricing. Vol traders use both interchangeably with care.
- [[Vol Surface]] - the SPX vol surface curvature (smile/skew) is partly driven by what VVIX is implying about tail distributions.
- [[Risk-On Risk-Off]] - VVIX often gives earlier RORO signals than VIX, especially in distinguishing complacency from genuine calm.
- [[Carry Unwind]] - VVIX spikes ahead of VIX often coincide with the first leg of carry unwinds.
- [[0DTE]] - 0DTE option dominance has distorted the relationship between VVIX and realized VIX moves, since 0DTE flow does not feed VVIX directly.

## Common misconceptions

**"VVIX going up means VIX is going up."** Not necessarily. VVIX can rise while VIX stays flat or even falls. That is the most informative scenario: it means traders are paying up for vol upside protection while spot vol is calm.

**"VVIX is just VIX squared or some derived number."** It is independently computed from VIX options market prices using the same formula structure as VIX. It is a market data point, not a transformation of VIX.

**"You can trade VVIX directly."** No. There are no VVIX futures or ETPs. To express a vol of vol view, you trade VIX options ([[Butterfly|butterflies]] for pure volga, [[Strangle|strangles]] for vol of vol + direction), or you use SPX option butterflies further out the surface.

**"High VVIX is a sell signal for equities."** It is a probability shift, not a deterministic signal. Many VVIX spikes resolve without a VIX explosion. The base rate matters: VVIX > 130 has historically been a stronger signal when combined with rising [[Realized Volatility]] or deteriorating credit spreads, not in isolation.

## Sources

- CBOE: VVIX methodology document. Available on cboe.com.
- Park, Yang Ho. "Volatility of Volatility and Tail Risk Premiums." Journal of Financial Econometrics, 2015.
- Bardgett, Gourier, Leippold. "Inferring volatility dynamics and risk premia from the S&P 500 and VIX markets." Journal of Financial Economics, 2019.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley. Chapter on vol of vol.
