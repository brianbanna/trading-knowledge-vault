---
aliases: [zomma, DgammaDvol, dGamma/dVol, gamma vol sensitivity, third order vanna]
tags:
  - "#quant"
date-added: "2026-05-23"
---

# Zomma

## Definition

Zomma is the rate at which [[Gamma]] changes as implied volatility changes. Gamma is not constant when vol moves: as implied vol shifts, the gamma profile changes shape. Zomma = d(Gamma) / d(σ) = d(Vanna) / d(S) = d³(Option price) / d²(S) × d(σ).

Zomma is the cross greek between spot convexity (gamma) and vol. Related to [[Vanna]] (dDelta/dVol) at one order higher: vanna tells you how delta changes with vol; zomma tells you how gamma changes with vol.

The picture: when vol rises, the gamma profile across strikes broadens. The peak gamma at ATM decreases, but gamma at OTM and ITM strikes increases. Zomma describes this redistribution. For ATM options zomma is typically negative (gamma decreases as vol rises). For OTM options zomma is typically positive (gamma increases as vol rises).

Zomma matters for any book with significant OTM option exposure during vol regime changes.

## Why it matters (commodities and FX)

Zomma explains why "vol spikes hurt short OTM positions more than the vega P&L alone predicts":

- **Short wing positions in vol spikes.** A trader short OTM puts on [[SPX]] or [[Brent Crude]] takes a vega hit when vol rises. Zomma also raises the gamma of those puts, meaning their delta will respond more violently to subsequent spot moves. Vega measures the first order vol P&L. Zomma is what makes the SUBSEQUENT spot move worse than expected.
- **[[Butterfly]] and [[Strangle]] pricing.** OTM strike gamma changes with vol via zomma. Affects how butterflies reprice during vol regime shifts. Long butterfly benefits from zomma when vol rises (wings gain gamma relative to body).
- **Tail hedge effectiveness.** A fund holding long deep OTM puts sees them gain gamma from zomma when vol begins rising. The tail hedge becomes more responsive to subsequent spot crashes than a static gamma calculation suggests. This is one reason long vol tail hedges work even when initial vega looks small.
- **Skew dynamics.** Zomma is part of what produces vol skew dynamics: as vol rises, OTM put gamma grows faster than ATM, pushing implied vol for those strikes higher, steepening the skew. Skew traders implicitly trade zomma.

In commodity markets, zomma is most visible during supply shocks. When [[Henry Hub Natural Gas]] vol jumps 40% to 100% on a polar vortex forecast, OTM call gamma explodes via zomma, creating a positive feedback loop where dealers short those calls must buy futures aggressively to hedge the suddenly large gamma exposure.

## Concrete example

**Concrete:** Dealer short 500 contracts of a 30 day [[Henry Hub Natural Gas]] $4.50 call (OTM). Spot $3.20, implied vol 50%. Initial gamma per contract 0.018 per dollar (small, OTM). Total initial short gamma at $4.50: -9. Polar vortex forecast hits. Implied vol jumps 50% to 90% in 2 days. Spot still $3.20 (vol rose before spot in commodity supply shocks). Vega P&L: -$25,000. New gamma at $4.50 strike: zomma was positive on this OTM call. Gamma per contract: 0.041. Total short gamma now -20.5. Short gamma exposure more than doubled purely from vol rising, with no spot move yet. Then spot jumps $3.20 to $3.90 the next day. Each $1 of additional spot adds 20 lots of delta to hedge (vs 9 it would have added before the vol move). Total decomposition: vega -$25,000, vanna -$15,000, spot gamma at new (higher) gamma -$40,000, of which half is attributable to zomma having raised gamma before the spot move.

**Simplified:** When vol rises, gamma moves from ATM strikes to OTM strikes. If you sold OTM options, your gamma exposure grew silently while vol was rising, before any spot move. Then when spot moves, it hits a bigger gamma than you had on the books at the start. The two punches compound: vega loss from vol up, then magnified gamma loss from spot move. Zomma is the channel that ties them together.

## Key mechanics and formulas

**Zomma for a vanilla option (Black Scholes):**

`Zomma = Gamma × (d1 × d2 - 1) / σ`

Equivalent to dGamma/dVol.

**Useful intuition:**
- Zomma is negative for ATM options (gamma decreases as vol rises)
- Zomma is positive for moderately OTM options (gamma increases as vol rises)
- Zomma crosses zero between ATM and the wings
- Zomma magnitude is largest for options with delta around 15 to 25, similar to [[Volga]] peak
- Zomma scales similarly to [[Vanna]] in d1, d2 dependencies

**Sign convention reading:**

`d1 × d2 > 1`: option is far enough OTM/ITM that vol increases raise gamma
`d1 × d2 < 1`: option is near ATM and vol increases reduce gamma at this strike

The "wings gain gamma when vol rises" effect comes directly from this. Vol does not change total gamma in the book if all strikes are filled (gamma redistributes). It moves gamma from ATM toward the wings.

**Relationship to vanna:**

`Zomma = d(Vanna) / d(S)`

Zomma describes how vanna changes across strikes. A book vanna neutral at one spot develops vanna exposure as spot moves, with zomma quantifying the drift.

**Approximation:**

For a moderately OTM call with delta around 0.20, zomma per 1 vol point is ~5 to 15% of gamma at that strike, depending on moneyness and tenor. A 20 point vol move (50% to 70%) doubles or triples gamma at OTM strikes.

## Prerequisites
- [[Gamma]]
- [[Vega]]
- [[Vanna]]
- [[Greeks]]
- [[Option]]
- [[Vol Surface]]

## Related concepts (learn next)
- [[Gamma]] - zomma is the vol derivative of gamma.
- [[Vanna]] - vanna and zomma form the second/third order vol/spot cross greek family.
- [[Volga]] - volga is the vol convexity of price. Zomma is the vol sensitivity of gamma. Together they describe how wing options behave in vol regime changes.
- [[Speed]] - speed is spot derivative of gamma. Zomma is vol derivative. Together they describe full gamma evolution.
- [[Vol Surface]] - skew and smile dynamics are partly driven by zomma redistributing gamma across strikes as vol changes.
- [[Vol of Vol]] - vol of vol amplifies zomma P&L in real markets where vol moves in jumps, not smooth drifts.
- [[Butterfly]] - butterflies have zomma exposure because they concentrate gamma at specific strikes, and that profile shifts with vol.

## Common misconceptions

**"Vega captures all the vol risk."** Wrong. Vega is the first order vol P&L. Volga captures the second order (vol moves squared). Zomma captures how vol changes redistribute gamma, which feeds back into subsequent spot move P&L. All three are needed for full vol risk decomposition.

**"Zomma is the same as volga."** Different greeks. Volga = dVega/dVol (price convexity in vol space). Zomma = dGamma/dVol (gamma sensitivity to vol). Both are third order with second derivatives, but they describe different effects.

**"Higher vol always means higher gamma."** False. Total portfolio gamma can be invariant to vol changes if all strikes are filled. Zomma describes the REDISTRIBUTION: ATM gamma falls as vol rises, OTM gamma rises. A book concentrated in ATM strikes loses gamma when vol rises (negative book zomma). A book concentrated in OTM gains gamma (positive zomma).

**"Zomma is too high order to matter."** For typical short dated retail positions, true. For institutional vol books with concentrated OTM exposure, zomma connects vol regime shifts to gamma exposure and hedging cost.

**"Zomma is only relevant during vol spikes."** Material whenever vol moves materially. Vol regime changes happen every few weeks in natgas and around macro events in FX. Treating zomma as crisis only understates its frequency.

## Sources

- Haug, Espen Gaarder. *The Complete Guide to Option Pricing Formulas*. Reference for closed form zomma and related third order greeks.
- Taleb, Nassim Nicholas. *Dynamic Hedging*. Discussion of higher order vol greeks and their interaction.
- Castagna, Antonio. *FX Options and Smile Risk*. Treatment of cross greeks in dealer books.
- Bergomi, Lorenzo. *Stochastic Volatility Modeling*. Discussion of vol surface dynamics and gamma redistribution.
- Wystup, Uwe. *FX Options and Structured Products*. Practical discussion of greek interactions in FX vol books.
