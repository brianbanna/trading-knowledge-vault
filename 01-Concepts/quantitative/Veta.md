---
aliases: [veta, vega decay, DvegaDtime, dVega/dTime, vega bleed]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-05-23"
---

# Veta

## Definition

Veta is the rate at which [[Vega]] changes as time passes. Vega is not constant through the life of an option: as expiry approaches, vega shrinks. Veta tells you how fast. Veta = d(Vega) / d(t) = d²(Option price) / d(σ × t). Also written DvegaDtime.

Veta is the vega bleed of an option. A 90 day ATM option may have vega 0.40. The same option 30 days later has vega 0.23. The 0.17 vega that disappeared over 60 days is veta, ~0.003 of vega lost per day. For [[0DTE]] options, veta dominates the final hours of vega exposure.

Veta is typically reported as a negative number per calendar day for long option positions. By [[Put Call Parity]], veta of a call equals veta of a put (same strike, same expiry).

## Why it matters (commodities and FX)

Veta traps systematic vol sellers and vol buyers who do not model time evolution:

- **Long vol portfolios bleed vega.** A fund running long vol as tail hedge (long [[VIX]] options, long deep OTM [[SPX Put|SPX puts]]) does not just lose [[Theta]] daily. The vega exposure itself decays. Protection thins as time passes even if vol does not move. Rolling the hedge is needed because options expire AND veta erodes the protective greek profile.
- **Short vol books face vega convergence into expiry.** Selling a 30 day [[Strangle]] on [[Brent Crude]] gives initial short vega. By day 25, vega has decayed via veta to a fraction of initial. The vol view is essentially over even though 5 days of theta remain.
- **Vega term structure trades.** Calendar spreads (long back month vega, short front month vega) are explicitly veta trades. The front month loses vega faster, which is the source of the trade's P&L pattern as time passes.
- **Commodity options around delivery.** [[WTI Crude Oil]] options expire ~3 business days before futures delivery. In the final week, vega collapses via veta even as gamma and charm explode. Risk reports showing vega without veta misrepresent vol exposure going forward.

For [[FX]] options with maturities aligned to economic releases (NFP, CPI, central bank meetings), veta determines actual vega exposure on the event day vs trade inception.

## Concrete example

**Concrete:** Vol fund long 500 contracts of [[VIX]] 18 strike calls, 60 days to expiry. Spot VIX 14, VVIX 80. Initial vega per contract 0.045. Total initial vega: 500 × 0.045 × 100 (VIX multiplier) = 2,250 USD per 1 vol point. Purpose: tail hedge for a vol spike. 30 days pass with VIX unchanged at 14, no vol event. Vega per contract decayed via veta to 0.028. Total vega: 1,400 USD per vol point, 38% reduction. The fund still has 30 days of "tail protection" on paper, but vega has shrunk by more than a third. A 5 point VIX vol spike on day 35 produces 5 × 1,400 = 7,000 USD profit instead of the 5 × 2,250 = 11,250 USD at inception. Hedge is 38% weaker. If vol exploded on day 5, vega exposure was still 2,100 USD (only slight bleed). Veta punishes delayed vol events, which is the typical case.

**Simplified:** Vega is not just lost when you sell out of an option. It bleeds away while you hold it. If you bought options as crash insurance and the crash does not happen this month, your insurance is weaker next month even though the option still exists. Roll long vol positions before veta has eroded them. Conversely, if you sold vol, the vega risk you carry decays in your favor, but only if nothing happens in the meantime.

## Key mechanics and formulas

**Veta for a vanilla call or put (Black Scholes):**

`Veta = -S × e^(-qT) × N'(d1) × sqrt(T) × [q + (r - q) × d1 / (σ × sqrt(T)) - (1 + d1 × d2) / (2T)]`

N'() = standard normal PDF, q = dividend yield (or foreign rate for FX), r = risk free rate. Dominant term for typical options is -N'(d1) × d1 × d2 / (2 × sqrt(T) × σ), the time scaling component.

**Useful intuition:**
- Veta is ~zero for deep ITM and deep OTM options (vega already near zero)
- Veta is largest in magnitude for ATM options
- Veta scales roughly as 1/sqrt(T): a 30 day ATM option has veta ~1.7x that of a 90 day
- For [[0DTE]] options, veta per hour can exceed total vega within 2 to 3 hours

**Useful approximation for ATM options:**

`Vega_ATM ≈ S × N'(0) × sqrt(T) / σ_annualized`

Differentiating: `Veta_ATM ≈ - S × N'(0) / (2 × sqrt(T) × σ_annualized)`

Vega decays as 1/sqrt(T); veta scales as 1/sqrt(T) inversely. Shorter dated options have proportionally more vega bleed per unit of time remaining.

**Calendar spread P&L decomposition:**

For long back month vega / short front month vega:
- Front month vega bleeds faster via veta
- Total book vega grows over time (long survives, short bleeds)
- This is the structural P&L of the calendar even if vol is unchanged

**Aggregation:** Veta is additive at the book level. Institutional greek reports show veta alongside theta as "time greeks."

## Prerequisites
- [[Vega]]
- [[Theta]]
- [[Option]]
- [[Greeks]]
- [[Black Scholes Model]]

## Related concepts (learn next)
- [[Vega]] - veta is the time derivative of vega.
- [[Theta]] - theta and veta are the two time greeks. Theta is the cost of holding; veta is the decay of vol sensitivity.
- [[Charm]] - delta analog. Both are time bleeds of first order greeks.
- [[Color]] - gamma analog. The full set of time bleed greeks.
- [[Volga]] - veta interacts with volga in determining how second order vol exposure evolves over time.
- [[VIX]] and [[VVIX]] - VIX options used as tail hedges are dominated by veta as primary risk decay channel.
- [[0DTE]] - extreme veta in the final hours means vega protection collapses inside a single session.

## Common misconceptions

**"Vega is constant for the life of the option."** False. Vega is highest for ATM options around T = 0.25 years (3 months), and decays both ways: T → 0 sends vega to zero, deep OTM/ITM vega also goes to zero. Veta captures this decay.

**"Theta is the only time greek I need."** Theta tells you cost of holding. Veta tells you how vol sensitivity itself erodes. Ignoring veta on long vol books means thinking your hedge is intact when it has bled out.

**"Veta only matters near expiry."** Close to true for short dated. For long dated vol books (1Y+), veta is also material because absolute vega values are large. A 2Y vega book bleeds vega measurably even at long horizons; the bleed looks slow in percentage terms.

**"Veta and theta move together."** Related but distinct. Theta is cost of holding in dollars per day. Veta is rate of change of vega in dollars of vega exposure per day. A position can have low theta (spot far from strikes) but meaningful veta if it holds ATM like vega.

**"Calendar spreads are pure vega trades."** No. Calendars are primarily veta trades with secondary vega and theta. "Front vega bleeds faster than back vega" IS the veta thesis. Vol level changes affect both legs roughly equally; differential decay creates the P&L pattern.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form veta and other second order time greeks.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. Treatment of vega term structure and veta in FX vol books.
- Sinclair, Euan. *Volatility Trading*, 2nd ed. Practical discussion of vega decay and tail hedge rolling.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. Discussion of vega term structure dynamics.
- Hull, John. *Options, Futures, and Other Derivatives*. Standard treatment of greek decomposition.
