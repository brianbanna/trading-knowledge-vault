---
aliases: [WMR fix, London fix, 4PM fix, FX fixing]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# FX Fix

## Definition
The FX Fix, formally the WM/Reuters (WMR) benchmark rate, is a set of foreign exchange reference rates published at 4PM London time each trading day. It is calculated as the median of trades and quotes observed during a 5 minute window (from 3:57:30 to 4:02:30 PM London time) across major FX platforms. Asset managers, pension funds, and index providers use the fix rate as their official conversion rate for portfolio rebalancing, [[NAV]] calculations, and index tracking. Because trillions of dollars in assets are benchmarked to this single rate, massive directional flows cluster around the fix window. The fix is the single most important recurring microstructure event in global FX markets. Understanding fix dynamics is critical for anyone trading currencies or managing cross-border portfolios.

## Why it matters (commodities and FX)
The fix generates predictable, large-scale flows that move major currency pairs and, by extension, dollar-denominated [[commodities]]. When global equity indices rebalance (particularly at month end and quarter end), asset managers must buy or sell currencies to match new index weights. These flows are partially predictable using publicly available data on index changes and fund flows. Commodity producers and consumers who hedge FX exposure often benchmark to the fix, creating additional volume. For systematic FX traders, the fix window represents both an opportunity (predictable flow) and a risk (extreme short-term volatility and [[slippage]]). Banks that execute fix orders earn significant revenue but face regulatory scrutiny after the 2013 to 2015 fix manipulation scandals.

## Concrete example
At month end, a large US pension fund must rebalance its international equity portfolio. European stocks outperformed US stocks by 3%, so the fund needs to sell approximately 2 billion USD and buy EUR to restore target weights. The fund instructs its custodian bank to execute at the 4PM London fix. The bank begins pre-positioning around 3:45 PM, buying EUR in the interbank market. EURUSD rises 15 pips in the 15 minutes before the fix window, then spikes another 10 pips during the 5 minute window itself. After 4:02:30 PM, the rate reverses 12 pips as the flow pressure dissipates. A systematic trader who predicted the direction of fix flow (using equity return differentials) bought EURUSD at 3:50 PM and sold at 4:05 PM, capturing 13 pips on 50 million notional. Conversely, a trader unaware of the fix who happened to sell EURUSD at 3:55 PM suffered a 25 pip adverse move.

## Key mechanics and formulas
- **Fix window**: 3:57:30 to 4:02:30 PM London time (5 minute median)
- **Fix flow prediction**: Expected fix flow direction = sign of (foreign equity return - domestic equity return) over the period since last rebalance
- **Month-end signal strength**: Stronger when equity return differentials are large and when passive fund AUM is high relative to active
- **Fix impact estimate**: Impact (pips) = (net fix flow in USD) / (average daily volume in pair) x scaling factor
- **Key dates**: Month-end and quarter-end fixes are 3 to 5x more volatile than mid-month fixes
- **Post-fix reversal**: Empirically, 40 to 60% of the pre-fix move reverses within 30 minutes after the fix window closes

## Prerequisites
- [[FX Market Hours]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[NAV]]
- [[Index Rebalancing]]

## Related concepts (learn next)
- [[FX Market Hours]]: the fix occurs during the London/NY overlap, the most liquid window of the day.
- [[Flow Signals]]: fix-related flow is one of the most studied predictable flow patterns in FX.
- [[TWAP]]: banks typically execute fix orders using time-weighted algorithms within and around the fix window.
- [[Internalization]]: banks may internalize fix flow against their own book rather than executing externally.
- [[Positioning Signal]]: extreme positioning ahead of the fix can cause the post-fix reversal to overshoot.
- [[Carry Cross Asset]]: carry trades that rebalance at the fix create additional predictable flow.
- [[ECN]]: fix-window volume on [[EBS]] and [[Reuters Matching]] spikes 5 to 10x above normal.

## Common misconceptions
1. **"The fix is a single price set by banks"**: Since the 2015 reforms, the fix is a transparent median of observed market transactions during a 5 minute window, not a rate set by a panel of dealers. The old methodology was vulnerable to manipulation.
2. **"Fix flow is always predictable"**: While month-end equity rebalancing creates a directional bias, the actual fix can be dominated by idiosyncratic flows (sovereign wealth funds, corporate M&A hedging) that are not publicly predictable.
3. **"Trading around the fix is front-running"**: Legitimate pre-positioning by banks executing client fix orders is legal; the illegal conduct in the 2013 to 2015 scandals involved collusion between dealers sharing client information and coordinating trades.

## Sources
- Evans, Martin D.D., "FX Trading and Exchange Rate Dynamics," Journal of Finance (2002)
- Melvin, Michael and Shand, Duncan, "Active Currency Trading and the London Fix," Journal of Financial Economics (2017)
- Financial Stability Board, "Foreign Exchange Benchmarks: Final Report" (2014)
- Bank of England, "Fair and Effective Markets Review" (2015)
