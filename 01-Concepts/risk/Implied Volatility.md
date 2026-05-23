---
aliases: [implied volatility, implied vol, IV]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-20"
---

# Implied Volatility

## Definition
Implied volatility (IV) is the market's forward looking expectation of price variability, extracted from the price of an [[Option]]. It is the vol level that, when input into an option pricing model (Black Scholes, Black 76), reproduces the option's current market price. Unlike [[realized volatility]] (backward looking, computed from historical returns), IV is forward looking and reflects the collective judgment of participants about future uncertainty. High IV means expensive options and large expected moves. Low IV means cheap options and expected calm. The spread between IV and subsequently realized vol — the volatility risk premium — is one of the most persistent risk premia in markets: IV runs 1 to 4 points above realized vol on average, compensating sellers for bearing uncertainty.

## Why it matters (commodities and FX)
IV is the single most important variable in options trading and the key metric distinguishing options from linear instruments like [[Futures Contract|futures]] and [[Swap|swaps]]. Commodity traders track IV to judge whether options are cheap or expensive relative to expected moves and whether to express views by buying or selling vol. IV spikes before scheduled events ([[WASDE]], OPEC, central bank meetings) and collapses after, creating predictable patterns. In agricultural markets, IV is structurally higher in the [[Weather Premium]] window (June to August) when yield uncertainty peaks. In FX, IV reflects uncertainty about monetary policy divergence, geopolitical risk, and global risk sentiment.

## Concrete example
**Concrete:** Corn 1 month ATM IV is at 18% in mid June, below the 10 year average of 24% for that period. A trader sees this as cheap given an emerging La Nina pattern and buys July corn straddles. Over 3 weeks, drought fears emerge and IV jumps to 32%. The straddle appreciates $0.45/bu ($2,250 per contract) from [[Vega]] alone, before any directional move. The trader sells the straddle for a profit. The trade worked because IV was mispriced relative to the imminent supply uncertainty.

**Simplified:** Options have prices. Those prices imply an expected size of future moves. That expected size, annualized, is the implied vol. If a market is calm, options are cheap and IV is low. If the market is nervous, options are expensive and IV is high. Buying options means buying vol; selling options means selling vol. Over time, the actual realized move is usually a bit smaller than what was implied, so sellers tend to win on average and buyers occasionally win big during tail events.

## Key mechanics and formulas
- **IV interpretation:** annualized standard deviation of expected log returns. 20% IV implies roughly a 20% one sigma range over 1 year.
- **Daily move:** Expected daily move ≈ IV / sqrt(252). 16% annual IV → 1.0% daily.
- **Monthly move:** Expected monthly move ≈ IV / sqrt(12). 24% annual IV → 6.9% monthly.
- **Volatility risk premium:** IV − subsequently realized vol. Historically positive (2 to 4 points in FX, 1 to 5 in commodities).
- **IV term structure:** IV varies by expiry. Short dated is more sensitive to near term events; long dated is more stable and mean reverting.
- **IV by strike:** IV varies across strikes, producing the [[Volatility Smile]] or skew.

## Prerequisites
- [[Option]]
- [[Futures Contract]]

## Related concepts (learn next)
- [[Volatility Smile]] shows how IV varies across strikes, revealing directional fear and tail risk pricing.
- [[Option]] pricing models (Black 76, Black Scholes) use IV as the key unobservable input.
- [[Weather Premium]] in grain markets creates seasonally elevated IV during the growing season.
- [[WASDE]] releases cause IV to spike pre report and collapse post report in agricultural options.
- [[Spread Trade]] using options (straddles, strangles, butterflies) is the primary way to trade IV directly.
- [[COT Positioning]] extremes coincide with IV compression, signaling complacency before vol expansion.
- [[Margin]] for option sellers rises with IV, potentially triggering margin calls on short vol positions.
- [[Basis Risk]] between IV on one underlying and realized vol on a correlated underlying is a vega basis.

## Common misconceptions
- **"High IV means prices will move a lot."** IV reflects expectation and risk premium, not certainty. Realized moves can be smaller than IV implies (the norm) or far larger (tail events).
- **"IV is a forecast."** It is a market price, not a statistical forecast. It embeds a risk premium above true expected vol. On average IV exceeds realized vol, which is why systematic option selling exists.
- **"IV is the same for all options on the same underlying."** IV varies by strike ([[Volatility Smile]]) and expiry (term structure). The full picture requires the surface.

## Sources
- Sheldon Natenberg, "Option Volatility and Pricing"
- John Hull, "Options, Futures, and Other Derivatives"
- CME Group, "Understanding Implied Volatility"
- Emanuel Derman, "The Volatility Smile"
