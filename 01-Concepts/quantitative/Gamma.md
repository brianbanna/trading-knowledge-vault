---
aliases: [gamma, option gamma, convexity exposure]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Gamma

## Definition
Gamma is the rate of change of an option's [[Delta]] with respect to a change in the [[underlying]] price. It measures the curvature (or [[Convexity]]) of the option's payoff: a high gamma position sees its delta shift rapidly as spot moves. Long options always have positive gamma, meaning delta increases as the market moves in the profitable direction and decreases as it moves against. Short gamma positions experience the opposite, a self reinforcing loss dynamic. Gamma is highest for [[ATM]] options near [[expiry]] and diminishes for deep in the money or deep out of the money options. In practical terms, gamma determines how often and how aggressively a delta hedged position must be rebalanced.

## Why it matters (commodities and FX)
Gamma is the mechanism through which options traders monetize [[Realized Volatility]]. A delta hedged long gamma position profits when spot moves more than [[implied volatility]] predicted, because each rehedge locks in a small gain from the delta shift. Conversely, short gamma is the primary risk in options market making: dealers who sell options to clients are short gamma and exposed to losses from large moves. In FX, the distribution of gamma across strikes near expiry creates [[Expiry Pinning]] effects as dealers' delta hedging flow acts as a stabilizing or destabilizing force. In commodities, short gamma positions on [[WTI Crude Oil]] near delivery can amplify price moves as market makers scramble to rehedge.

## Concrete example
**Success:** A trader buys a 1 week EUR/USD ATM [[Straddle]] at 8% implied vol and delta hedges. Spot is 1.0800 and gamma is 0.15 per 100 pip move (delta shifts by 15 for a 100 pip move). Over 5 days, spot oscillates: up 80 pips, down 120 pips, up 90 pips. Each rehedge captures a small gain. Total gamma P&L from hedging is 45 pips. [[Theta]] cost for the week is 32 pips. Net profit is 13 pips. Realized vol came in at 9.5%, above the 8% implied.

**Failure:** A dealer is short GBP/USD 1 day gamma from expiring options (strike 1.2700, spot 1.2690). Gamma is extremely high because expiry is hours away. A surprise UK data release pushes spot from 1.2690 to 1.2750 in 5 minutes. Delta swings from 0.45 to 0.95 almost instantaneously. The dealer must buy GBP 50 million at 1.2750 to rehedge, but the fill is at 1.2755 due to [[Slippage]]. The gap move generates a 40 pip loss that cannot be recovered through hedging.

## Key mechanics and formulas
- **Gamma** = N'(d1) / (spot × vol × sqrt(time)), where N'(d1) is the standard normal density
- **Gamma peaks at ATM**: when d1 = 0, N'(d1) is maximized
- **Gamma increases as expiry approaches**: the 1 / sqrt(time) term means gamma explodes for very short dated ATM options
- **Dollar gamma** = 0.5 × gamma × spot² × (move size)²; the P&L from a spot move for a delta hedged position
- **Gamma P&L per day** = 0.5 × gamma × spot² × (daily return)², summed across all moves
- **Gamma theta relationship**: for a delta hedged position, daily theta = 0.5 × gamma × spot² × implied vol² / 252 (annualized), showing that theta is the "cost" of gamma
- **Long gamma**: profits from large moves, pays theta; **Short gamma**: collects theta, suffers from large moves

## Prerequisites
- [[Delta]]
- [[Vanilla Option]]
- [[ATM]]
- [[Implied Volatility]]
- [[Hedging]]

## Related concepts (learn next)
- [[Theta]]: the direct tradeoff with gamma; long gamma = short theta, always
- [[Vega]]: while gamma captures spot move sensitivity, vega captures vol move sensitivity; both are long for option buyers
- [[Realized Volatility]]: gamma P&L is a function of realized vol relative to implied; this is the core of delta hedged options trading
- [[Expiry Pinning]]: extreme gamma near expiry concentrates hedging flow and can pin spot to strikes
- [[Vanna]]: gamma's cousin; measures how delta changes with vol rather than with spot
- [[Straddle]]: the maximum gamma structure at any tenor
- [[Convexity]]: gamma is the options equivalent of convexity in fixed income

## Common misconceptions
1. **"Long gamma is always profitable."** Long gamma profits only if [[Realized Volatility]] exceeds the [[implied volatility]] at which the options were purchased. In quiet markets, [[Theta]] decay exceeds gamma rehedge gains every day.
2. **"Gamma is only relevant for delta hedgers."** Even unhedged option holders benefit from understanding gamma: it determines how quickly an OTM option picks up delta (and becomes valuable) as spot moves toward the strike.
3. **"Short gamma risk is manageable."** In continuous markets, short gamma can be managed through frequent rehedging. In gapping markets (interventions, flash crashes, weekend gaps), short gamma produces discontinuous losses that no hedging strategy can prevent.
4. **"Gamma is stable."** Gamma itself changes with spot, vol, and time. Near expiry, gamma can swing from near zero to extreme values as spot crosses a strike, creating "gamma whipsaw" for dealers.

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed.
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
