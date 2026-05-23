---
aliases: [expiry pinning, pin risk, options pinning, strike gravity]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Expiry Pinning

## Definition
Expiry pinning is the gravitation of spot toward a large option [[strike price]] as [[expiry]] approaches. [[Delta]] hedging by dealers creates a self reinforcing loop. When dealers are long [[Gamma]] at a strike, their hedging stabilizes spot near it: they sell as spot rises above and buy as spot falls below. Short gamma reverses the effect and amplifies moves away from the strike. The pull is strongest in the final 24 to 48 hours before expiry, when gamma peaks and hedging frequency rises. Pinning happens in all option markets but is most pronounced in FX due to the concentration of large notional options at round number strikes.

## Why it matters (commodities and FX)
In FX, trillions of dollars of options expire at the 10 AM New York cut daily. When a disproportionately large notional sits at a single strike (EUR/USD 1.1000), the delta hedging flow can dominate all other activity in the hours around the fix. Traders who know the location and size of major strikes anticipate spot behavior near expiry. In commodities, pinning is visible around [[WTI Crude Oil]] and [[Gold Futures]] option expiries on NYMEX and COMEX, where open interest at round strikes creates measurable pull. Pinning creates opportunities (trading toward the pin) and risks (being trapped in a position that cannot escape the magnet).

## Concrete example

**Concrete:** EUR/USD spot at 1.0985 at 8 AM NY. Market intel: EUR 3 billion notional expiring at 1.1000 at the 10 AM cut, dealers net long gamma. Trader buys at 1.0985, expecting pull toward 1.1000. Over 90 minutes spot drifts to 1.0998 as dealer hedging (buying on dips, selling on rallies) stabilizes near the strike. Trader sells at 1.0997 for 12 pips. Failure mirror: trader short at 1.1010 expecting a break lower. Despite bearish fundamentals, the option expiry holds spot between 1.0990 and 1.1010. After 10 AM the options roll off and the magnet disappears. Spot drops to 1.0950, but the trader covered at 1.1005 for 5 pip loss, missing the post expiry move.

**Simplified:** Around a major option expiry, dealers must continuously rebalance hedges as spot moves. If they are long options at a strike, they buy when spot falls and sell when spot rises, pinning spot near the strike. The bigger the option notional, the stronger the magnet. Right after expiry, the options roll off and the magnet vanishes, often releasing a fast move that was suppressed for hours.

## Key mechanics and formulas
- **Dealer gamma hedging**: long gamma at strike K means sell as spot > K (caps upside), buy as spot < K (supports downside). Creates mean reversion toward K.
- **Pinning strength** is proportional to: net gamma notional at strike × (1 / time to expiry) × (1 / distance from strike).
- **Critical mass**: pinning is observable only when notional at a single strike significantly exceeds normal turnover in the relevant window. For EUR/USD, typically EUR 2 billion+ at one strike.
- **Breakout threshold**: macro events or data exceeding hedging capacity break the pin; spot can gap as dealers chase.
- **Post expiry release**: after expiry, gamma disappears and spot moves freely. Post expiry often sees rapid directional moves.
- **Gamma imbalance**: short gamma at a strike reverses the effect, amplifying moves away from the strike, creating instability.

## Prerequisites
- [[Gamma]]
- [[Delta]]
- [[Vanilla Option]]
- [[ATM]]
- [[Market Impact]]

## Related concepts (learn next)
- [[Gamma]]: fundamental driver; magnitude and sign of dealer gamma at each strike determines flow.
- [[Delta]]: hedging is the mechanism through which gamma creates spot flow.
- [[Digital Option]]: digitals create extreme gamma near strike at expiry, amplifying pinning or whipsaw.
- [[Barrier Option]]: barrier hedging near triggers creates similar magnet or repellent dynamics.
- [[Vanna]]: vanna flows interact with pinning, especially when vol shifts as expiry approaches.
- [[Theta]]: rapid decay near expiry mirrors extreme gamma buildup.
- [[Liquidity]]: pinning is strongest in liquid markets where dealers can rehedge; illiquid markets gap and break the pin.

## Common misconceptions

**"Expiry pinning always works."** Requires gamma concentration and absence of competing macro flows. A strong release or intervention overwhelms even a massive gamma position.

**"You can always see the pin coming."** Position data is not publicly available. Traders rely on intelligence, broker commentary, and inference. Estimated strike concentrations are often wrong.

**"Pinning only affects spot at the exact strike."** The pull creates a range, typically 20 to 30 pips in EUR/USD, where spot oscillates. Weakens with distance.

**"Short gamma always causes instability."** Short gamma amplifies moves only if a move starts. In a quiet market, short gamma has no effect because there is no move to amplify.

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Garleanu, Nicolae, Pedersen, Lasse, and Poteshman, Allen. "Demand Based Option Pricing," *Review of Financial Studies*, 2009.
- Ni, Sophie, Pearson, Neil, and Poteshman, Allen. "Stock Price Clustering on Option Expiration Dates," *Journal of Financial Economics*, 2005.
- Avellaneda, Marco and Lipkin, Michael. "A Market Induced Mechanism for Stock Pinning," *Quantitative Finance*, 2003.
