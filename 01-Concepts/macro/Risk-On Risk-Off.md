---
aliases: [risk-on risk-off, RORO, risk on, risk off, risk appetite, risk sentiment]
tags:
  - "#macro"
date-added: "2026-03-20"
---

# Risk-On Risk-Off

## Definition

Risk on / risk off (RORO) describes the dominant regime in which financial markets oscillate between 2 states: risk on (investors seek higher returns by moving into riskier assets) and risk off (investors prioritize capital preservation by moving into [[Safe Haven Assets]]). In a risk on environment, equities, credit, [[Commodity Currencies]], industrial commodities, and EM assets rise together. In a risk off environment, these assets fall while Treasuries, gold, JPY, CHF, and USD strengthen. The RORO framework captures the reality that cross asset [[Correlation|correlations]] spike during stress, with most assets moving as a single "risk" factor.

## Why it matters (commodities and FX)

In RORO regimes, individual commodity fundamentals matter less than the macro risk regime. A copper trader with a bullish supply/demand thesis can lose money if a risk off event (banking crisis, geopolitical escalation, recession fears) overwhelms the micro fundamentals. An FX trader long AUD/JPY is simultaneously expressing risk on (long commodity currency, short safe haven). Understanding which regime the market is in, and which asset moves are fundamentally driven vs. RORO driven, is critical for position sizing, [[Hedging]], and trade timing.

Energy commodities have a complex relationship with RORO: they are risk on (demand driven) but also respond to [[Supply Shock|supply shocks]] that may themselves trigger risk off. Oil can rise on a Middle East escalation (supply risk) while equities and commodity currencies fall (risk off).

## Concrete example

**March 2023 (SVB/banking crisis):** Regional bank failures triggered risk off. In 1 week: S&P 500 fell 4%, US 2Y yield fell 100bp (flight to safety), [[Gold Futures|gold]] rallied $100/oz, AUD/USD fell 3%, USD/JPY fell 4% (JPY safe haven), [[Copper Futures|copper]] fell 4%. The fundamental story for copper (tight supply, green energy demand) did not change at all, but RORO flows overwhelmed fundamentals temporarily. Traders who sized their copper long for fundamental risk only, without accounting for RORO, were stopped out before the fundamental thesis could play out.

**Measuring risk on/off:** The VIX (equity implied vol) is the most common risk off indicator. VIX below 15 = risk on. VIX above 25 = risk off. VIX above 35 = crisis. Other indicators: credit spreads (CDX HY), gold/copper ratio, AUD/JPY, EM sovereign CDS.

## Key mechanics and formulas

**RORO correlation regime:**
In risk off: `Corr(Equities, Commodities) → +0.7 to +0.9` (both fall together)
In risk on: `Corr(Equities, Commodities) → +0.3 to +0.5` (both rise but more idiosyncratic)
In risk off: `Corr(Gold, Equities) → -0.3 to -0.6` (gold rises as equities fall)

**Risk on basket:** Equities, credit, [[Commodity Currencies]] (AUD, CAD, NOK), EM FX, industrial metals (copper, aluminum), energy (crude)

**Risk off basket:** US Treasuries, [[Gold Futures|gold]], JPY, CHF, USD, VIX

**Simple risk regime indicator:**
`Risk Score = z(SPX) + z(CDX) + z(AUDJPY) - z(VIX) - z(Gold)`

Normalize each to z-scores. Positive composite = risk on. Negative = risk off.

## Prerequisites
- [[Correlation]]
- [[Volatility]]
- [[Safe Haven Assets]]

## Related concepts (learn next)
- [[Safe Haven Assets]] - the instruments that benefit from risk off. Understanding which safe havens work in which scenarios.
- [[Regime Shift]] - when the market transitions from risk on to risk off or vice versa. These transitions are where the biggest P&L happens.
- [[Commodity Currencies]] - the FX expression of risk on. Long commodity currencies is a risk on trade.
- [[Volatility]] - VIX and implied vol regimes are the thermometer for RORO.
- [[Correlation]] - RORO regimes change cross asset correlations. Portfolio risk calculations must account for regime dependent correlations.
- [[Hedging]] - risk off environments demand defensive positioning. Knowing how to hedge commodity portfolios during RORO events.
- [[Carry Trade]] - carry trades are risk on. They unwind violently during risk off, amplifying safe haven currency moves.

## Common misconceptions

**"Risk on/off is binary."** It is a spectrum. Markets can be mildly risk off (gradual rotation into bonds, moderate VIX) or acutely risk off (panic liquidation, VIX at 50+). The intensity matters for sizing hedges.

**"Commodity fundamentals do not matter in risk off."** They do, but on a delayed basis. If copper fundamentals are genuinely tight, the risk off selloff creates a buying opportunity. The skill is surviving the drawdown to capture the fundamental value.

**"USD always strengthens in risk off."** The USD strengthens in GLOBAL crises (dollar liquidity demand) but can weaken in US SPECIFIC crises (fiscal concerns, US political instability, US recession). The "dollar smile" captures this: USD strong at both extremes, weak in the middle.

## Sources

- Baele, Bekaert, Inghelbrecht, and Wei, "Flights to Safety" (2020, Review of Financial Studies)
- BIS: "Risk On/Risk Off" (Quarterly Review, 2012)
- Ilmanen, "Expected Returns" (2011), macro regime chapters
