---
aliases: [gamma, option gamma, convexity exposure]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Gamma

## Definition
Gamma is the rate of change of [[Delta]] with respect to the [[underlying]] price. It is the curvature ([[Convexity]]) of the option payoff: high gamma means delta shifts rapidly as spot moves. Long options always have positive gamma: delta increases as the market moves in your favor and decreases against. Short gamma positions experience the opposite, a self reinforcing loss dynamic. Gamma is highest for [[ATM]] options near [[expiry]] and falls for deep ITM or OTM options. Gamma determines how often and how aggressively a delta hedged position must be rebalanced.

## Why it matters (commodities and FX)
Gamma is the mechanism through which options traders monetize [[Realized Volatility]]. A delta hedged long gamma position profits when spot moves more than [[implied volatility]] predicted, because each rehedge locks in a small gain from the delta shift. Short gamma is the primary risk in options market making: dealers who sell options are short gamma and exposed to losses from large moves. In FX, the distribution of gamma across strikes near expiry creates [[Expiry Pinning]] effects as dealer delta hedging acts as stabilizing or destabilizing flow. In commodities, short gamma on [[WTI Crude Oil]] near delivery amplifies price moves as market makers scramble to rehedge.

## Concrete example

**Concrete:** Trader buys a 1 week EURUSD ATM [[Straddle]] at 8% implied vol and delta hedges. Spot 1.0800, gamma 0.15 per 100 pip move. Over 5 days spot oscillates: up 80, down 120, up 90. Each rehedge captures a small gain. Gamma P&L from hedging: 45 pips. [[Theta]] cost for the week: 32 pips. Net profit: 13 pips. Realized vol came in at 9.5%, above the 8% implied. Contrast: a dealer short GBPUSD 1 day gamma (strike 1.2700, spot 1.2690) faces a UK data surprise pushing spot from 1.2690 to 1.2750 in 5 minutes. Delta swings from 0.45 to 0.95 almost instantaneously. Rehedge fills at 1.2755 via [[Slippage]]. Gap move produces a 40 pip loss no hedging can recover.

**Simplified:** Gamma is how fast your directional exposure changes when spot moves. If you own an option, you collect that curvature when the market moves. The more the market wiggles, the more you collect by rebalancing. The cost of owning that wiggle harvester is theta. If you sold the option, you collect theta but pay every wiggle. Big sudden moves are what kill short gamma positions because delta moves before you can hedge.

## Key mechanics and formulas
- **Gamma** = N'(d1) / (spot × vol × sqrt(time)), N'(d1) = standard normal density
- **Gamma peaks at ATM**: when d1 = 0, N'(d1) is maximized
- **Gamma grows as expiry approaches**: 1 / sqrt(time) makes gamma explode for very short dated ATM options
- **Dollar gamma** = 0.5 × gamma × spot² × (move size)²; P&L from a spot move for a delta hedged position
- **Gamma P&L per day** = 0.5 × gamma × spot² × (daily return)², summed across all moves
- **Gamma theta identity**: for a delta hedged position, daily theta = 0.5 × gamma × spot² × implied vol² / 252 (annualized). Theta is the cost of gamma.
- **Long gamma**: profits from large moves, pays theta. **Short gamma**: collects theta, suffers from large moves.

## Prerequisites
- [[Delta]]
- [[Vanilla Option]]
- [[ATM]]
- [[Implied Volatility]]
- [[Hedging]]

## Related concepts (learn next)
- [[Theta]]: direct tradeoff. Long gamma = short theta, always.
- [[Vega]]: vol move sensitivity. Both long for option buyers.
- [[Realized Volatility]]: gamma P&L is a function of realized vol vs implied. Core of delta hedged options trading.
- [[Expiry Pinning]]: extreme gamma near expiry concentrates hedging flow.
- [[Vanna]]: gamma's cousin. How delta changes with vol rather than spot.
- [[Straddle]]: maximum gamma structure at any tenor.
- [[Convexity]]: gamma is the options equivalent of fixed income convexity.

## Common misconceptions
1. **"Long gamma is always profitable."** Long gamma profits only if [[Realized Volatility]] exceeds [[implied volatility]] at which the options were bought. In quiet markets, [[Theta]] decay exceeds rehedge gains daily.
2. **"Gamma is only relevant for delta hedgers."** Unhedged option holders also need gamma awareness: it determines how quickly an OTM option picks up delta as spot moves toward the strike.
3. **"Short gamma risk is manageable."** In continuous markets, yes via frequent rehedging. In gapping markets (interventions, flash crashes, weekend gaps), short gamma produces discontinuous losses no hedging prevents.
4. **"Gamma is stable."** Gamma changes with spot, vol, and time. Near expiry, gamma swings from near zero to extreme as spot crosses a strike, creating "gamma whipsaw."

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
