---
aliases: [0DTE, zero days to expiration, zero DTE, same day expiry options, daily expirations, 0 DTE options]
tags:
  - "#microstructure"
  - "#equities/indices"
  - "#risk"
date-added: "2026-05-23"
---

# 0DTE

## Definition

0DTE stands for "zero days to expiration." It refers to listed options that expire on the same trading day they are traded. The term is most commonly used for SPX, SPY, QQQ, and increasingly XSP options on US equity indices, but daily expiries now exist on individual mega cap names, on the VIX (Wednesday weekly cycle), and on some commodity products (GLD, USO).

Plain English: an option that lives for hours, not weeks. Buying a 0DTE call at 10:00 AM that expires at 4:00 PM ET means you have 6 hours of [[Theta]] decay collapsing to zero. The option's behavior is dominated by [[Gamma]] (extremely high near the money), [[Theta]] (catastrophic decay rate), and order flow into expiry.

0DTE products grew from a niche to a dominant market structure feature between 2022 and 2024. By 2024, 0DTE options accounted for roughly 50% of total SPX option volume on many days, the largest single change to US equity option market microstructure in two decades. The proliferation is enabled by the CBOE adding Tuesday and Thursday SPX expiries (2022), giving every business day a same day expiry contract.

## Why it matters (commodities and FX)

0DTE is primarily an SPX equity options story, but it materially affects commodities and FX through second order channels:

- **Intraday equity moves are amplified or dampened by dealer 0DTE gamma hedging.** When dealers are short 0DTE puts (retail buying downside), they must sell futures into weakness, accelerating selloffs. When dealers are short 0DTE calls (institutional overwriting), they must buy into rallies, suppressing them. This changes intraday cross asset correlation patterns, particularly between SPX and [[USDJPY]] (a classic carry/risk proxy).
- **VIX behavior has changed.** Because 0DTE options are not in the [[VIX]] calculation (VIX uses 23 to 37 day SPX options), large 0DTE driven moves can occur without VIX moving. This means [[VIX]] increasingly understates true intraday realized vol. Commodity traders using VIX as a [[Risk-On Risk-Off]] gauge get a distorted signal in 0DTE dominant regimes.
- **End of day flow predictability changed.** Before 0DTE, the close was driven by index rebalancing and MOC orders. Now, large 0DTE positions expiring in the money or pinning at strikes create predictable flow into the last 30 minutes that propagates to [[USDJPY]], [[Gold Futures]], and US Treasuries via cross asset arbitrage desks.
- **Vol selling regime change.** 0DTE has absorbed much of the systematic short vol flow that used to live in 1 week to 1 month options. This compresses term structure differently than pre 2022 and changes how [[Volmageddon]] style unwinds would propagate.

For commodities traders, the most actionable takeaway: when SPX moves 1% in 30 minutes on no news, suspect a 0DTE driven gamma cascade. Do not chase the cross asset move; it may reverse the same session.

## Concrete example

It is Wednesday, 2:15 PM ET. SPX is at 5,400. No scheduled data. A copper trader is long [[Copper Futures]] with a stop at $4.60 (current price $4.65). [[USDMXN]] is quiet.

Suddenly SPX drops from 5,400 to 5,360 in 18 minutes. Copper drops from $4.65 to $4.605, almost triggering the stop. [[USDMXN]] spikes from 17.20 to 17.34. VIX moves from 13.5 to only 14.2 (barely).

What happened? At 2:00 PM, a large institutional client bought 50,000 SPX 5,390 puts expiring at 4:00 PM (0DTE). Dealer was short the puts. As SPX drifted toward 5,390, dealer gamma exposure exploded (gamma of a near ATM 2 hour option is enormous). Dealer hedge: sell SPX futures aggressively to stay neutral. The futures selling spilled into [[ES Futures]], which spilled into cross asset risk off via algorithmic correlation models. MXN sold off (risk currency), copper dropped (risk metal).

By 3:30 PM, SPX recovered to 5,395 as the gamma squeeze reversed (dealer now needs to buy back hedges). Copper recovered to $4.64. The trader who held through the move was fine. The trader who got stopped at $4.60 lost money on a move that had nothing to do with copper fundamentals or even broad risk sentiment, only 0DTE dealer hedging.

What if the trader had recognized the pattern? Rule: "On any sub 30 minute SPX move > 0.6% with VIX move < 1 point, treat as likely 0DTE gamma. Do not stop out cross asset positions on the first leg; reassess at the close." This kind of rule would have saved the stop out.

What about the opposite scenario: institutional call buyer at 11:00 AM into a rally? Dealer short gamma forces them to buy SPX into strength, accelerating the rally. Cross asset: [[Gold Futures]] often sells off ("risk on"), [[USDJPY]] rallies, [[Copper Futures]] catches a bid. A copper short would get squeezed.

## Key mechanics and formulas

**Time decay rate:** Theta of a 0DTE ATM option is not linear. With T → 0:
`Theta_ATM ≈ - S × σ / (2 × sqrt(2π × T))`

As T approaches zero, theta approaches negative infinity. A 5,400 strike SPX 0DTE call worth $15 at 10:00 AM may be worth $0.10 at 3:55 PM if SPX is still at 5,400.

**Gamma concentration:** Gamma of a 0DTE ATM option is enormous:
`Gamma_ATM ≈ 1 / (S × σ × sqrt(2π × T))`

With T = 1 hour ≈ 0.0001 years, gamma is orders of magnitude higher than a 30 day ATM option. A 0.1% spot move causes 30 to 50 delta swings on a 0DTE option that would cause 1 to 2 delta swings on a 30 day option.

**Dealer gamma profile:** Aggregate market maker gamma can be estimated from open interest weighted strike distribution. When dealer gamma is large and negative (dealers short gamma), market is unstable: small moves amplify. When large and positive, market is stable: small moves dampened.

`GEX (Gamma Exposure) ≈ Σ (gamma_i × OI_i × 100 × spot)`

**Pin risk:** 0DTE options expiring near a high open interest strike create [[Expiry Pinning]] dynamics, where spot tends to gravitate to the strike into the close. Major round number strikes (5,400 SPX, 600 SPY) are common pin candidates.

**Charm (delta decay):** Charm is the change in delta per unit time. For 0DTE options it dominates the morning to afternoon delta drift, creating predictable flow patterns dealers must hedge.

**Volume distribution:** 0DTE volume in SPX is now concentrated 9:30 to 10:00 AM (overnight position adjustment), 1:00 to 2:00 PM (lunchtime risk on/off), and 3:00 to 4:00 PM (closing gamma resolution).

## Prerequisites
- [[Option]]
- [[Theta]]
- [[Gamma]]
- [[Delta]]
- [[Implied Volatility]]
- [[Expiry Pinning]]

## Related concepts (learn next)
- [[Expiry Pinning]] - 0DTE has made pinning a daily event for major round number strikes, not just a monthly expiry phenomenon.
- [[Gamma]] - the dominant greek for 0DTE. Understanding gamma dynamics is non negotiable for trading near expiry options or for anticipating dealer flow.
- [[VIX]] - 0DTE flow does not enter the VIX calculation, creating a systematic divergence between intraday realized vol and the VIX print.
- [[VVIX]] - the vol of vol metric is increasingly poor at predicting 0DTE driven intraday moves, since 0DTE behavior is not stochastic vol but order flow driven.
- [[Vol Surface]] - 0DTE has created a "T < 1 day" extension to the surface that does not behave like the rest of the term structure.
- [[Volmageddon]] - the 2018 short vol blowup involved 1 month VIX products. A 0DTE driven analog has not yet occurred at scale; many practitioners worry it is coming.
- [[Volatility]] - 0DTE has structurally changed the relationship between option implied vol at different tenors and realized intraday vol.

## Common misconceptions

**"0DTE options are just lottery tickets."** Retail uses them this way, but institutional usage is dominated by sophisticated overwriting strategies, dealer hedging, and intraday gamma scalping. The total notional traded in 0DTE SPX exceeds the GDP of medium sized countries on a daily basis.

**"0DTE is a US equity only phenomenon."** Most active today, but daily expiry products are expanding to single stocks (TSLA, NVDA), to ETFs (GLD, USO), and to overseas indices (KOSPI 200, Nikkei weekly). The market structure consequences will follow.

**"0DTE will cause the next market crash."** Possible but unproven. The 2024 August 5 yen carry unwind tested 0DTE infrastructure (VIX spiked to 65 intraday) and the system held. Risk is real but should not be assumed catastrophic.

**"0DTE volume is mostly speculation."** Significant portion is institutional hedge replacement: instead of holding a 30 day put hedge, a fund rolls 0DTE puts daily. This is more capital efficient but creates different gamma dynamics for the dealer ecosystem.

**"You can't use 0DTE for cross asset signals."** You can. Tracking SPX 0DTE open interest concentration, dealer GEX estimates, and 0DTE volume spikes provides predictive signal for intraday FX and commodity moves. Several macro funds use SpotGamma or SqueezeMetrics data feeds specifically for this purpose.

## Sources

- CBOE: SPX Weeklys and Daily Expiry documentation.
- Brogaard, Han, Won. "Does the Tail Wag the Dog? The Effect of 0DTE Options on Underlying Returns." Working paper series 2024.
- JPMorgan Marko Kolanovic notes on 0DTE flow and dealer positioning, 2022 to 2024.
- SpotGamma and SqueezeMetrics: practitioner research on gamma exposure modeling.
- Sinclair, Euan. "Positional Option Trading," Wiley, 2020. Chapter on short dated options.
- BIS Quarterly Review, March 2024: "The market microstructure impact of 0DTE options."
