---
aliases: [VIX, CBOE Volatility Index, fear gauge, fear index, SPX implied vol index]
tags:
  - "#equities/indices"
  - "#risk"
  - "#macro"
date-added: "2026-05-23"
---

# VIX

## Definition

The VIX is the CBOE Volatility Index. It measures the market's expectation of 30 day forward [[Realized Volatility]] of the S&P 500, derived from the prices of S&P 500 (SPX) options. Plain English: it is a single number that says "how big do option traders think SPX moves will be over the next month, annualized." A VIX of 16 means the market is pricing roughly 16% annualized vol, or about 1% daily standard deviation. A VIX of 40 means panic, with implied daily moves around 2.5%. It is not a forecast of direction, only of magnitude. It is called the "fear gauge" because it tends to spike when equities crash, since investors pay up for downside [[SPX Put]] protection.

The VIX is computed via a model free formula that integrates across all out of the money SPX puts and calls in the front two option expiries, weighted by 1/strike². This gives the risk neutral expected variance, then square rooted and annualized. It is NOT a Black Scholes implied vol of a single option.

## Why it matters (commodities and FX)

VIX is the single most watched [[Risk-On Risk-Off]] thermometer in global markets. Even a pure commodities or FX trader needs to track it because cross asset flows are driven by it:

- When VIX spikes above 25, [[Carry Trade|carry trades]] in [[USDMXN]], [[USDBRL]], [[USDZAR]] unwind. Funding currencies ([[USDJPY]], [[EURUSD]] short EUR) rally violently.
- Commodity vol indices ([[OVX]] for [[WTI Crude Oil]], GVZ for [[Gold Futures]]) are highly correlated with VIX. When VIX moves, so does cross commodity implied vol.
- High VIX = liquidity withdrawal across all assets. [[Bid-Ask Spread|Bid ask spreads]] widen in [[FX]], in [[LME]] metals, in [[Brent Crude]] futures.
- Risk managers cut position sizes when VIX is elevated. A copper trader who ignores VIX may be carrying the same notional while the firm cuts overall risk budget.

VIX also has a clean term structure. The VIX [[Forward Curve]] (VX futures) trades in [[Contango]] roughly 80% of the time, which is why short vol products like SVXY exist and why [[Volmageddon]] (February 2018) wiped them out when the curve inverted.

## Concrete example

VIX trades at 14 on a quiet Tuesday in February. A trader is long [[USDMXN]] short MXN (a classic carry trade earning around 8% annual carry). Position is 5 million USD notional.

Wednesday morning: surprise hawkish Fed minutes. SPX drops 2.5%, VIX jumps from 14 to 23. The MXN sells off 1.8%, costing the carry trader 90,000 USD. Why? VIX up = global risk off = carry unwind = USD demand vs EM currencies.

Same day, [[Brent Crude]] front month implied vol (the OVX equivalent) jumps from 24% to 31%. A short straddle position the trader had on Brent loses 40,000 USD because vega exposure is now repricing.

If the trader had a rule "cut EM carry by 50% when VIX > 20," the MXN loss would have been 45,000 USD. The single VIX print saved 45,000 USD across the book.

What if instead VIX collapsed from 14 to 11? Carry trade gains an extra 30,000 USD as MXN rallies, short Brent straddle gains 25,000 USD as vol crushes. Low VIX is friendly to short vol and carry.

## Key mechanics and formulas

**Generalized variance formula (simplified):**

`VIX² = (2/T) × Σ (ΔK_i / K_i²) × e^(rT) × Q(K_i) - (1/T) × (F/K_0 - 1)²`

Where T = time to expiry (30 day blend of front two SPX option series), K_i = strike, ΔK_i = strike spacing, Q(K_i) = midprice of OTM option at K_i, F = forward, r = risk free rate. VIX = 100 × sqrt(annualized variance).

**Daily move implied by VIX:**

`Daily σ ≈ VIX / 16` (since sqrt(252) ≈ 15.87)

VIX 16 → ~1.0% daily SPX move expected. VIX 32 → ~2.0% daily move. VIX 80 (2008 peak, March 2020 peak) → ~5.0% daily moves.

**VIX term structure:**

VIX is spot. VX futures trade further out. Curve shape:
- [[Contango]] (front < back): normal regime, ~80% of time, short vol positive carry
- [[Backwardation]] (front > back): stress regime, vol spike priced as transient

**Variance Risk Premium (VRP):**

`VRP = VIX - subsequent realized vol of SPX`

Historically positive (VIX overestimates future realized by 2 to 4 vol points on average). This is the structural edge for systematic short vol strategies, paid for in tail risk.

**Notable VIX levels:**
- < 12: extreme complacency
- 12 to 16: low vol regime
- 16 to 22: normal
- 22 to 30: stress emerging
- 30 to 50: crisis
- > 50: panic (2008 Lehman, March 2020 COVID)

## Prerequisites
- [[Volatility]]
- [[Implied Volatility]]
- [[Realized Volatility]]
- [[Option]]
- [[Forward Curve]]

## Related concepts (learn next)
- [[VVIX]] - vol of vol of the VIX itself. When VIX is at 18 but VVIX is at 130, the market expects vol of vol to expand, often preceding a VIX spike.
- [[Vol of Vol]] - the conceptual framework behind why VVIX exists and why it matters for tail hedging.
- [[Risk-On Risk-Off]] - VIX is the canonical RORO signal. Levels and rate of change matter equally.
- [[Carry Unwind]] - VIX spikes are the trigger for most carry unwinds across FX and EM.
- [[Vol Surface]] - VIX is one number summarizing an entire surface. The skew (SKEW index) captures the asymmetry VIX misses.
- [[0DTE]] - the explosion of 0DTE SPX options has changed how VIX behaves, since 0DTE volume does not enter the VIX calculation directly but affects underlying flows.
- [[Volmageddon]] - the February 2018 short vol blowup is the canonical case study of VIX term structure inversion and ETP feedback loops.

## Common misconceptions

**"VIX is a leading indicator."** VIX is a contemporaneous measure of fear. It moves WITH equity selloffs, not before. The exception is when VVIX or skew is elevated while VIX is calm, which can signal building tail risk.

**"You can trade the VIX directly."** You cannot. There is no spot VIX exposure available to retail or most institutions. You trade VX futures, VIX options, or ETPs (UVXY, SVXY, VXX), all of which have significant [[Roll Yield|roll yield]] drag in normal [[Contango]] regimes. VXX has lost more than 99% of its value since inception due to roll decay, not because vol fell.

**"VIX measures stock market volatility."** It measures the implied vol of SPX options, which is the market's risk neutral expectation of future SPX vol. This is not the same as historical realized vol, and it carries a [[Variance Risk Premium|risk premium]].

**"High VIX means stocks will fall."** VIX measures magnitude not direction. After VIX peaks at extreme levels (>40), forward equity returns are historically POSITIVE on average. The trade is to be a buyer of equities when VIX is panicked, not a seller.

## Sources

- CBOE: VIX White Paper (2003, revised 2014). Definitive source on the calculation methodology.
- Whaley, Robert E. "Understanding the VIX." Journal of Portfolio Management, 2009.
- Carr and Wu, "Variance Risk Premiums." Review of Financial Studies, 2009.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley.
