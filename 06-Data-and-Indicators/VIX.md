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

VIX is the CBOE Volatility Index. It measures the market's expected 30 day forward [[Realized Volatility]] of the S&P 500, derived from SPX option prices. Plain English: a single number that says how big option traders think SPX moves will be over the next month, annualized. VIX 16 prices ~16% annualized vol, or ~1% daily standard deviation. VIX 40 prices panic, ~2.5% daily moves. It measures magnitude, not direction. Called the "fear gauge" because it spikes in equity crashes when investors pay up for [[SPX Put]] protection.

VIX is computed via a model free formula that integrates across all OTM SPX puts and calls in the front 2 option expiries, weighted by 1/strike². This gives the risk neutral expected variance, then square rooted and annualized. It is NOT the Black Scholes implied vol of a single option.

## Why it matters (commodities and FX)

VIX is the single most watched [[Risk-On Risk-Off]] thermometer in global markets. Even a pure commodities or FX trader needs to track it because cross asset flows are driven by it:

- VIX above 25 triggers [[Carry Trade|carry]] unwinds in [[USDMXN]], [[USDBRL]], [[USDZAR]]. Funding currencies ([[USDJPY]], EUR short legs) rally hard.
- Commodity vol indices ([[OVX]] for [[WTI Crude Oil]], GVZ for [[Gold Futures]]) are highly correlated with VIX. When VIX moves, cross commodity implied vol moves.
- High VIX = liquidity withdrawal across assets. [[Bid-Ask Spread|Bid ask spreads]] widen in [[FX]], [[LME]] metals, [[Brent Crude]] futures.
- Risk managers cut position sizes when VIX is elevated. A copper trader who ignores VIX carries the same notional while the firm cuts the risk budget.

VIX also has a clean term structure. VX futures trade in [[Contango]] ~80% of the time, which is why short vol products like SVXY exist and why [[Volmageddon]] (Feb 2018) wiped them out when the curve inverted.

## Concrete example

**Concrete:** VIX at 14 on a quiet Tuesday in February. Trader is long $5M [[USDMXN]] short MXN earning ~8% annual carry. Wednesday: hawkish Fed minutes. SPX drops 2.5%, VIX jumps from 14 to 23. MXN sells off 1.8% = $90,000 mark to market loss. Same day, [[Brent Crude]] implied vol jumps from 24% to 31%; a short Brent straddle on the trader's book loses $40,000 on vega. With a rule "cut EM carry 50% when VIX > 20," the MXN loss is $45,000 instead, saving $45,000 across the book.

**Simplified:** VIX is the global temperature reading for risk. When it is low, money flows into carry, EM, and short vol trades. When it spikes, all of those unwind at once. A commodities or FX trader who watches only their own market gets blindsided by cross asset flows triggered by a VIX move. Hard rule: cut carry and short vol when VIX crosses a threshold. The trigger is mechanical, not discretionary.

## Key mechanics and formulas

**Generalized variance formula (simplified):**

`VIX² = (2/T) × Σ (ΔK_i / K_i²) × e^(rT) × Q(K_i) − (1/T) × (F/K_0 − 1)²`

Where T = time to expiry (30 day blend of front 2 SPX series), K_i = strike, ΔK_i = strike spacing, Q(K_i) = midprice of OTM option at K_i, F = forward, r = risk free rate. VIX = 100 × sqrt(annualized variance).

**Daily move implied by VIX:**

`Daily σ ≈ VIX / 16` (since sqrt(252) ≈ 15.87)

VIX 16 → ~1.0% daily. VIX 32 → ~2.0%. VIX 80 (2008 peak, March 2020 peak) → ~5.0%.

**VIX term structure:**

VIX is spot. VX futures trade further out. Curve shape:
- [[Contango]] (front < back): normal regime, ~80% of time, short vol positive carry
- [[Backwardation]] (front > back): stress regime, vol spike priced as transient

**Variance Risk Premium (VRP):**

`VRP = VIX − subsequent realized vol of SPX`

Historically positive (VIX overestimates future realized by 2 to 4 vol points). The structural edge for systematic short vol, paid for in tail risk.

**Notable VIX levels:**
- <12: extreme complacency
- 12 to 16: low vol regime
- 16 to 22: normal
- 22 to 30: stress emerging
- 30 to 50: crisis
- >50: panic (2008 Lehman, March 2020 COVID)

## Prerequisites
- [[Volatility]]
- [[Implied Volatility]]
- [[Realized Volatility]]
- [[Option]]
- [[Forward Curve]]

## Related concepts (learn next)
- [[VVIX]] - vol of vol. When VIX is 18 but VVIX is 130, the market expects vol of vol to expand, often preceding a VIX spike.
- [[Vol of Vol]] - the conceptual framework behind VVIX and tail hedging.
- [[Risk-On Risk-Off]] - VIX is the canonical RORO signal. Levels and rate of change both matter.
- [[Carry Unwind]] - VIX spikes trigger carry unwinds across FX and EM.
- [[Vol Surface]] - VIX summarizes the surface; the skew (SKEW index) captures asymmetry VIX misses.
- [[0DTE]] - 0DTE volume does not enter VIX directly but affects underlying flows.
- [[Volmageddon]] - February 2018 short vol blowup is the canonical case study of VIX term inversion and ETP feedback loops.

## Common misconceptions

**"VIX is a leading indicator."** VIX is contemporaneous. It moves WITH equity selloffs, not before. Exception: elevated VVIX or skew while VIX is calm can signal building tail risk.

**"You can trade VIX directly."** You cannot. No spot VIX exposure exists for retail or most institutions. You trade VX futures, VIX options, or ETPs (UVXY, SVXY, VXX), all subject to [[Roll Yield|roll yield]] drag in normal [[Contango]]. VXX has lost >99% of value since inception from roll decay, not from vol falling.

**"VIX measures stock market volatility."** It measures the implied vol of SPX options, the risk neutral expectation of future SPX vol. Not the same as historical realized, and it carries a [[Variance Risk Premium|risk premium]].

**"High VIX means stocks will fall."** VIX measures magnitude not direction. After VIX peaks above 40, forward equity returns are historically POSITIVE on average. The trade is to buy when VIX is panicked, not sell.

## Sources

- CBOE: VIX White Paper (2003, revised 2014). Definitive source on the calculation methodology.
- Whaley, Robert E. "Understanding the VIX." Journal of Portfolio Management, 2009.
- Carr and Wu, "Variance Risk Premiums." Review of Financial Studies, 2009.
- Sinclair, Euan. "Volatility Trading," 2nd ed. Wiley.
