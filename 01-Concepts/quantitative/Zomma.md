---
aliases: [zomma, DgammaDvol, dGamma/dVol, gamma vol sensitivity, third order vanna]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Zomma

## Definition

Zomma is the third order greek that measures the rate at which [[Gamma]] changes as implied volatility changes. Plain English: gamma is not constant when vol moves. As implied vol shifts, the gamma profile changes shape. Zomma tells you how fast. Mathematically, zomma = d(Gamma) / d(σ) = d(Vanna) / d(S) = d³(Option price) / d²(S) × d(σ).

Zomma is the cross greek between spot convexity (gamma) and vol. It is related to [[Vanna]] (which is dDelta/dVol) but at one order higher: where vanna tells you how delta changes with vol, zomma tells you how gamma changes with vol.

The intuitive picture: when vol rises, the gamma profile across strikes broadens out. The peak gamma at ATM decreases, but gamma at OTM and ITM strikes increases. Zomma describes this redistribution. For ATM options zomma is typically negative (gamma decreases as vol rises). For OTM options zomma is typically positive (gamma increases as vol rises).

Zomma matters for any book with significant OTM option exposure during periods of vol regime change.

## Why it matters (commodities and FX)

Zomma is the greek that explains why "vol spikes hurt short OTM option positions more than the vega P&L alone predicts":

- **Short wing positions in vol spikes.** A trader short OTM puts on [[SPX]] or [[Brent Crude]] takes a hit from vega when vol rises. But zomma also raises the gamma of those puts, meaning their delta will respond more violently to subsequent spot moves. Vega measures the first order vol P&L. Zomma is what makes the SUBSEQUENT spot move worse than expected.
- **[[Butterfly]] and [[Strangle]] pricing.** OTM strike gamma changes with vol via zomma. This affects how butterflies reprice during vol regime shifts. A long butterfly position benefits from zomma when vol rises (the wings gain gamma relative to the body).
- **Tail hedge effectiveness.** A fund holding long deep OTM puts as crash protection sees those puts gain gamma from zomma when vol begins rising. The "tail hedge" therefore becomes more responsive to subsequent spot crashes than a static gamma calculation would suggest. This is one reason long volatility tail hedges work even when initial vega exposure looks small.
- **Skew dynamics.** Zomma is part of what produces the vol skew dynamics: as vol rises, OTM put gamma grows faster than ATM, pushing implied vol for those strikes higher, steepening the skew. Skew traders implicitly trade zomma.

In commodity markets, zomma is most visible during supply shock events. When [[Henry Hub Natural Gas]] vol jumps from 40% to 100% on a polar vortex forecast, OTM call gamma explodes via zomma, creating a positive feedback loop where dealers short those calls must buy futures aggressively to hedge the suddenly large gamma exposure.

## Concrete example

A dealer is short 500 contracts of a 30 day [[Henry Hub Natural Gas]] $4.50 call (currently OTM). Spot natgas: $3.20. Implied vol: 50%. Initial gamma per contract: 0.018 per dollar move (small because the option is OTM).

Total initial short gamma at $4.50 strike: -9.

If spot moves to $4.00, the gamma at this OTM strike is moderate. Hedging is manageable.

Polar vortex forecast hits. Implied vol jumps from 50% to 90% in 2 days. Spot still at $3.20 (vol rose before spot did, common in commodity supply shocks).

Vega P&L on the short call: roughly -$25,000 (lost from vega expansion alone).

Now check gamma at the $4.50 strike. Zomma was positive on this OTM call. New gamma per contract: 0.041 per dollar. Total short gamma at $4.50: now -20.5.

The dealer's short gamma exposure more than doubled, purely from vol rising. They have not yet seen a spot move.

Then spot jumps from $3.20 to $3.90 the next day on continued cold weather forecasts. Each $1 of additional spot adds 20 lots of delta to hedge (vs the 9 it would have added before the vol move). Hedging cost: bid ask through wider markets, slippage, the works.

Total P&L decomposition:
- Vega: -$25,000 (from vol up)
- Vanna: -$15,000 (delta shifted from vol move)
- Spot move delta P&L: variable depending on hedge
- Gamma P&L from spot move at new (higher) gamma: -$40,000
- Of which roughly half is attributable to zomma having raised gamma before the spot move

Without zomma awareness the dealer sees "vega loss + spot move loss" and considers the position unlucky. With zomma awareness they recognize that the vol move PRELOADED the position with extra short gamma, and the spot move that followed was always going to be more damaging than a similar move at lower vol levels.

## Key mechanics and formulas

**Zomma for a vanilla option (Black Scholes):**

`Zomma = Gamma × (d1 × d2 - 1) / σ`

Equivalent to dGamma/dVol.

**Useful intuition:**
- Zomma is negative for ATM options (gamma decreases as vol rises)
- Zomma is positive for moderately OTM options (gamma increases as vol rises)
- Zomma crosses zero somewhere between ATM and the wings
- Zomma magnitude is largest for options with delta around 15 to 25, similar to [[Volga]] peak region
- Zomma scales similarly to [[Vanna]] in terms of d1, d2 dependencies

**Sign convention reading:**

`d1 × d2 > 1` means option is far enough OTM/ITM that vol increases raise gamma
`d1 × d2 < 1` means option is near ATM and vol increases reduce gamma at this strike

The "wings gain gamma when vol rises" phenomenon comes directly from this. Vol does not change total gamma in the book if all strikes are filled (gamma is moved around). It redistributes gamma from ATM toward the wings.

**Relationship to vanna:**

`Zomma = d(Vanna) / d(S)`

This means zomma describes how vanna changes across strikes. A book that is vanna neutral at one spot level develops vanna exposure as spot moves, with zomma quantifying the drift.

**Approximation:**

For a moderately OTM call with delta around 0.20, zomma per 1 vol point is roughly 5 to 15% of gamma at that strike, depending on exact moneyness and time to expiry. This means a 20 point vol move (e.g. 50% to 70%) doubles or triples the gamma at OTM strikes.

## Prerequisites
- [[Gamma]]
- [[Vega]]
- [[Vanna]]
- [[Greeks]]
- [[Option]]
- [[Vol Surface]]

## Related concepts (learn next)
- [[Gamma]] - zomma is the vol derivative of gamma. Understanding gamma is the prerequisite.
- [[Vanna]] - vanna and zomma form the second/third order vol/spot cross greek family.
- [[Volga]] - volga is the vol convexity of price. Zomma is the vol sensitivity of gamma. Together they describe how wing options behave in vol regime changes.
- [[Speed]] - speed is the spot derivative of gamma. Zomma is the vol derivative of gamma. Together they describe full gamma evolution.
- [[Vol Surface]] - skew and smile dynamics are partly driven by zomma redistributing gamma across strikes as vol changes.
- [[Vol of Vol]] - vol of vol amplifies zomma P&L in real markets where vol moves in jumps not smooth drifts.
- [[Butterfly]] - butterflies have zomma exposure because they concentrate gamma at specific strikes, and that gamma profile shifts with vol.

## Common misconceptions

**"Vega captures all the vol risk."** Wrong. Vega is the first order vol P&L. Volga captures the second order (vol moves squared). Zomma captures how vol changes redistribute gamma across the book, which feeds back into subsequent spot move P&L. All three are needed for full vol risk decomposition.

**"Zomma is the same as volga."** Different greeks. Volga = dVega/dVol (price convexity in vol space). Zomma = dGamma/dVol (gamma sensitivity to vol). Both are third order greeks involving second derivatives, but they describe different effects.

**"Higher vol always means higher gamma."** False. Total portfolio gamma can be invariant to vol changes if all strikes are filled. What zomma describes is the REDISTRIBUTION: ATM gamma falls as vol rises, OTM gamma rises. A book concentrated in ATM strikes loses gamma when vol rises (negative zomma at the book level). A book concentrated in OTM strikes gains gamma (positive zomma).

**"Zomma is too high order to matter."** For typical short dated retail option positions, true. For institutional vol books with concentrated OTM exposure, zomma is the channel that connects vol regime shifts to gamma exposure and ultimately to hedging cost.

**"Zomma is only relevant during vol spikes."** Material whenever vol moves materially. Vol regime changes happen frequently in commodities (every few weeks in natgas) and around macro events in FX. Treating zomma as "only crisis time" understates its frequency.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form zomma and related third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of higher order vol greeks and their interaction.
- Castagna, Antonio. *FX Options and Smile Risk*. Treatment of cross greeks in dealer books.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. Discussion of vol surface dynamics and gamma redistribution.
- Wystup, Uwe. *FX Options and Structured Products*. Practical discussion of greek interactions in FX vol books.
