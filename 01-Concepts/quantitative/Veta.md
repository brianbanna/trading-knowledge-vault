---
aliases: [veta, vega decay, DvegaDtime, dVega/dTime, vega bleed]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-05-23"
---

# Veta

## Definition

Veta is the second order greek that measures the rate at which [[Vega]] changes as time passes. Plain English: vega is not constant through the life of an option. As expiry approaches, vega shrinks. Veta tells you how fast. Mathematically, veta = d(Vega) / d(t) = d²(Option price) / d(σ × t). Also written as DvegaDtime.

Veta is the "vega bleed" of an option. A 90 day ATM option may have vega 0.40. The same option 30 days later has vega 0.23. The 0.17 of vega that disappeared over 60 days is veta in action, equivalent to roughly 0.003 of vega lost per day. For [[0DTE]] options, veta is enormous and dominates the final hours of vega exposure.

Veta is typically reported as a negative number per calendar day for long option positions, since vega decays as time passes. By [[Put Call Parity]], veta of a call equals veta of a put (same strike, same expiry).

## Why it matters (commodities and FX)

Veta is the greek that traps systematic vol sellers and vol buyers who do not model time evolution properly:

- **Long volatility portfolios bleed vega.** A fund running long vol as a tail hedge (long [[VIX]] options, long deep OTM [[SPX Put|SPX puts]]) does not just lose [[Theta]] daily. The vega exposure itself decays, so the protection thins out as time passes even if vol does not move. Rolling the hedge is needed not only because options expire but because veta erodes the protective greek profile.
- **Short vol books face vega convergence into expiry.** Selling a 30 day [[Strangle]] on [[Brent Crude]] gives initial short vega exposure. By day 25, the vega has decayed via veta to a fraction of the initial level. The trader's vol view is essentially over by then, even though the option still has 5 days of theta to collect.
- **Vega term structure trades.** Calendar spreads (long back month vega, short front month vega) are explicitly veta trades. The front month leg loses vega faster than the back month leg, which is the source of the trade's P&L pattern as time passes.
- **Commodity options around delivery.** [[WTI Crude Oil]] options expire roughly 3 business days before futures delivery. In the final week, vega collapses via veta even as gamma and charm explode. Risk reports that show vega without showing veta misrepresent the actual vol exposure profile going forward.

For [[FX]] options with maturities aligned to economic releases (NFP, CPI, central bank meetings), veta determines how much vega exposure you actually have on the event day vs the day you put the trade on.

## Concrete example

A volatility fund is long 500 contracts of [[VIX]] 18 strike calls expiring in 60 days. Spot VIX: 14. Implied vol on VIX options: 80% (VVIX). Initial vega per contract: 0.045.

Total initial vega exposure: 500 × 0.045 × 100 (VIX multiplier) = 2,250 USD per 1 vol point change in VIX implied vol.

Fund's purpose: tail hedge in case VIX spikes. Reasoning: pay 30 days of theta, hope for a vol explosion.

30 days pass. Spot VIX unchanged at 14. No vol event. Vega per contract has decayed via veta to 0.028. Total vega exposure: 1,400 USD per vol point, a 38% reduction.

The fund still has 30 days of "tail protection" on paper, but their vega exposure has shrunk by more than a third. If a vol event hits on day 35 instead of day 1, the same 5 point VIX vol spike now produces 5 × 1,400 = 7,000 USD profit, instead of the 5 × 2,250 = 11,250 USD it would have produced at trade inception. The hedge is 38% weaker.

What if the fund had only watched vega (initial 2,250) and theta (decaying daily) but ignored veta? They would believe their tail hedge was intact. In reality, vega has bled out from underneath them at a rate of roughly 17 USD per day of vega exposure lost (2,250 × 0.038 average daily veta = ~85 USD of "vega value" lost per day even before realized vol shows up).

The right answer is to roll the long vega position before veta has eroded it, typically when remaining tenor drops below 30 to 45 days for VIX type tail hedges.

What if vol exploded on day 5? Vega exposure was still 2,100 USD (only slight veta bleed). The fund captures most of the move. Veta is most punishing when the vol event is delayed, which is the typical case.

## Key mechanics and formulas

**Veta for a vanilla call or put (Black Scholes):**

`Veta = -S × e^(-qT) × N'(d1) × sqrt(T) × [q + (r - q) × d1 / (σ × sqrt(T)) - (1 + d1 × d2) / (2T)]`

Where N'() = standard normal PDF, q = dividend yield (or foreign rate for FX), r = risk free rate. The dominant term for typical options is -N'(d1) × d1 × d2 / (2 × sqrt(T) × σ), the time scaling component.

**Useful intuition:**
- Veta is approximately zero for deep ITM and deep OTM options (vega is already near zero)
- Veta is largest in magnitude for ATM options
- Veta scales roughly as 1/sqrt(T): a 30 day ATM option has veta about 1.7 times that of a 90 day ATM option
- For [[0DTE]] options, veta per hour can exceed total vega within 2 to 3 hours

**Useful approximation for ATM options:**

`Vega_ATM ≈ S × N'(0) × sqrt(T) / σ_annualized`

Differentiating: `Veta_ATM ≈ - S × N'(0) / (2 × sqrt(T) × σ_annualized)`

So vega decays as 1/sqrt(T) and veta scales as 1/sqrt(T) inversely as well, meaning shorter dated options have proportionally more vega bleed per unit of time remaining.

**Calendar spread P&L decomposition:**

For a long back month vega / short front month vega trade:
- Front month vega bleeds faster (via veta)
- Net effect: total book vega grows over time (long vega position survives, short bleeds)
- This is the structural P&L of the calendar even if vol is unchanged

**Aggregation:** Veta is additive at the book level. Most institutional greek reports show veta alongside theta as "time greeks" because both describe time evolution.

## Prerequisites
- [[Vega]]
- [[Theta]]
- [[Option]]
- [[Greeks]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Vega]] - veta is the time derivative of vega, so understanding vega dynamics is the prerequisite.
- [[Theta]] - theta and veta are the two time greeks. Theta is the cost of holding, veta is the decay of vol sensitivity.
- [[Charm]] - charm is to delta what veta is to vega. Both are time bleeds of first order greeks.
- [[Color]] - color is to gamma what veta is to vega. The full set of time bleed greeks.
- [[Volga]] - veta interacts with volga in determining how the second order vol exposure evolves over time.
- [[VIX]] and [[VVIX]] - VIX options used as tail hedges are dominated by veta as their primary risk decay channel.
- [[0DTE]] - extreme veta in the final hours of 0DTE options means vega protection collapses inside a single trading session.

## Common misconceptions

**"Vega is constant for the life of the option."** False. Vega is highest for ATM options around T = 0.25 years (3 months), and decays in both directions: as T → 0 vega goes to zero, and for deep OTM/ITM vega also approaches zero. Veta captures this decay.

**"Theta is the only time greek I need."** Theta tells you cost of holding. Veta tells you how your vol sensitivity itself is eroding. For long vol books, ignoring veta means you think your hedge is intact when in fact it has bled out.

**"Veta only matters near expiry."** Close to true for short dated options, but for long dated vol books (1Y+), veta is also material because the absolute vega values are large. A 2Y vega book bleeds vega measurably even at long horizons; the bleed just looks slow in percentage terms.

**"Veta and theta move together."** They are related but distinct. Theta is the cost of holding measured in dollars per day. Veta is the rate of change of vega in dollars-of-vega-exposure per day. A position can have low theta (because spot is far from any strike) but meaningful veta if it holds ATM-like vega exposure.

**"Calendar spreads are pure vega trades."** No. Calendar spreads are primarily veta trades, with secondary vega and theta components. The thesis "front vega bleeds faster than back vega" IS the veta thesis. Vol level changes affect both legs roughly equally; the differential decay is what creates the P&L pattern.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form veta and other second order time greeks.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. Treatment of vega term structure and veta in FX vol books.
- Sinclair, Euan. *Volatility Trading*, 2nd ed. Practical discussion of vega decay and tail hedge rolling.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. Discussion of vega term structure dynamics.
- Hull, John. *Options, Futures, and Other Derivatives*. Standard treatment of greek decomposition.
