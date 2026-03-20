---
aliases: [expiry pinning, pin risk, options pinning, strike gravity]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Expiry Pinning

## Definition
Expiry pinning is the phenomenon where the spot price of an asset gravitates toward a large option [[strike price]] as [[expiry]] approaches. This occurs because the [[Delta]] hedging activity of options dealers creates a self reinforcing feedback loop. When dealers are long [[Gamma]] at a strike (net long options), their hedging stabilizes spot near the strike: they sell as spot rises above and buy as spot falls below. When dealers are short gamma, the effect reverses and amplifies moves away from the strike. The gravitational pull of large strikes is strongest in the final 24 to 48 hours before expiry, when [[Gamma]] peaks and hedging frequency increases. Pinning is observed across all options markets but is most pronounced in FX due to the concentration of large notional options at round number strikes.

## Why it matters (commodities and FX)
In FX, trillions of dollars of options expire at the 10 AM New York cut each day. When a disproportionately large notional is concentrated at a single strike (e.g., EUR/USD 1.1000), the delta hedging flow can dominate all other market activity in the hours around the fix. Traders who understand the location and size of major option strikes can anticipate spot behavior near expiry. In commodities, pinning effects are visible around [[WTI Crude Oil]] and [[Gold Futures]] option expiries on NYMEX and COMEX, where the concentration of open interest at round strikes creates measurable gravitational pull. Pinning creates both opportunities (trading toward the pin) and risks (being trapped in a position that cannot escape the magnet zone).

## Concrete example
**Success:** EUR/USD spot is at 1.0985 at 8 AM New York, and market intelligence indicates EUR 3 billion notional of options expiring at the 1.1000 strike at the 10 AM cut, with dealers net long gamma. The trader buys EUR/USD at 1.0985, expecting the gravitational pull toward 1.1000. Over the next 90 minutes, spot drifts to 1.0998 as dealer hedging activity (buying EUR on dips, selling on rallies) stabilizes spot near the strike. The trader sells at 1.0997 for a 12 pip profit.

**Failure:** A trader is short EUR/USD at 1.1010, expecting a break lower through 1.1000. Despite bearish fundamentals, the massive option expiry at 1.1000 prevents spot from moving significantly below 1.0990 or above 1.1010. Dealer gamma hedging absorbs every attempt to break the range. After the 10 AM expiry, the options roll off and the gamma magnet disappears. Spot immediately drops to 1.0950, but the trader had already covered at 1.1005 for a 5 pip loss, missing the post expiry move.

## Key mechanics and formulas
- **Dealer gamma hedging**: if dealers are long gamma at strike K, they sell as spot rises above K (capping upside) and buy as spot falls below K (supporting downside), creating mean reversion toward K
- **Pinning strength** is proportional to: net gamma notional at the strike × (1 / time to expiry) × (1 / distance from strike)
- **Critical mass**: pinning is only observable when the notional at a single strike significantly exceeds normal market turnover in the relevant time window. For EUR/USD, this typically means EUR 2 billion+ at a single strike
- **Breakout threshold**: if a macro event or data release generates flow that exceeds the gamma hedging capacity, the pin breaks and spot can gap aggressively as dealers are forced to chase
- **Post expiry release**: after the options expire, the gamma disappears, and spot can move freely. The immediate post expiry period often sees rapid directional moves as the "lid" is removed
- **Gamma imbalance**: if dealers are short gamma at a strike, the effect reverses: their hedging amplifies moves away from the strike, creating instability rather than pinning

## Prerequisites
- [[Gamma]]
- [[Delta]]
- [[Vanilla Option]]
- [[ATM]]
- [[Market Impact]]

## Related concepts (learn next)
- [[Gamma]]: the fundamental driver of pinning; the magnitude and sign of dealer gamma at each strike determines the flow
- [[Delta]]: delta hedging is the mechanism through which gamma creates spot flow
- [[Digital Option]]: digital options create extreme gamma near the strike at expiry, amplifying pinning or whipsaw effects
- [[Barrier Option]]: barrier hedging near trigger levels creates similar "magnet" or "repellent" dynamics to expiry pinning
- [[Vanna]]: vanna flows interact with pinning, especially when vol is changing as expiry approaches
- [[Theta]]: the rapid theta decay near expiry is the mirror image of extreme gamma buildup
- [[Liquidity]]: pinning is strongest in liquid markets where dealers can continuously rehedge; in illiquid markets, gaps break the pin

## Common misconceptions
1. **"Expiry pinning always works."** Pinning requires sufficient gamma concentration and the absence of competing macro flows. A single strong data release or intervention can overwhelm even a massive gamma position.
2. **"You can always see the pin coming."** Precise option position data is not publicly available. Traders rely on market intelligence, broker commentary, and inference from price action. Estimated strike concentrations are often wrong.
3. **"Pinning only affects spot at the exact strike."** The gravitational effect creates a range around the strike, typically within 20 to 30 pips in EUR/USD, where spot oscillates. The effect weakens with distance from the strike.
4. **"Short gamma always causes instability."** Short gamma amplifies moves, but only if the move starts. In a truly quiet market, short gamma has no effect because there is no move to amplify. Pinning and anti pinning require some initial spot movement to trigger the feedback loop.

## Sources
- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options*.
- Garleanu, Nicolae, Pedersen, Lasse, and Poteshman, Allen. "Demand Based Option Pricing," *Review of Financial Studies*, 2009.
- Ni, Sophie, Pearson, Neil, and Poteshman, Allen. "Stock Price Clustering on Option Expiration Dates," *Journal of Financial Economics*, 2005.
- Avellaneda, Marco and Lipkin, Michael. "A Market Induced Mechanism for Stock Pinning," *Quantitative Finance*, 2003.
