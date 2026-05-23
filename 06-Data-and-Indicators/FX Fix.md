---
aliases: [WMR fix, London fix, 4PM fix, FX fixing]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# FX Fix

## Definition
The FX Fix, formally the WM/Reuters (WMR) benchmark, is a set of FX reference rates published at 4PM London each trading day. It is the median of trades and quotes observed in a 5 minute window (3:57:30 to 4:02:30 PM London) across major FX platforms. Asset managers, pension funds, and index providers use the fix as their official conversion rate for portfolio rebalancing, [[NAV]] calculations, and index tracking. Because trillions in assets are benchmarked to this single rate, directional flows cluster around the window. The fix is the most important recurring microstructure event in global FX. Understanding fix dynamics is critical for FX traders and cross border portfolio managers.

## Why it matters (commodities and FX)
The fix generates predictable, large scale flows that move major pairs and, by extension, dollar denominated [[commodities]]. At month and quarter ends, equity index rebalancing forces asset managers to buy or sell currencies to match new weights. These flows are partially predictable from public index changes and fund flows. Commodity producers and consumers benchmark FX hedges to the fix, adding volume. For systematic FX traders, the window is both opportunity (predictable flow) and risk (volatility, [[slippage]]). Banks that execute fix orders earn significant revenue but face regulatory scrutiny after the 2013 to 2015 manipulation scandals.

## Concrete example
**Concrete:** Month end. US pension fund must rebalance international equity. European stocks outperformed US stocks by 3%, so the fund sells $2B USD and buys EUR. Custodian executes at the 4PM London fix. Bank pre positions from 3:45 PM buying EUR interbank. EUR/USD rises 15 pips before the window, then spikes another 10 pips within the 5 minute window. After 4:02:30 PM, EUR/USD reverses 12 pips as flow pressure dissipates. A systematic trader bought EUR/USD 50M at 3:50 PM and sold at 4:05 PM, capturing 13 pips = $65,000. A trader who sold at 3:55 PM unaware of the fix suffered a 25 pip adverse move = $125,000 mark.

**Simplified:** Once a day at 4PM London, banks compute a benchmark price by taking the median of all FX trades in a 5 minute window. Pension funds and index funds use that price to convert currencies for their rebalancing. Because they all execute at the same minute and often in the same direction, you get a predictable surge of buying or selling. Trade with the flow and you make money; trade against without knowing it and you get run over.

## Key mechanics and formulas
- **Fix window:** 3:57:30 to 4:02:30 PM London (5 minute median)
- **Fix flow prediction:** Direction = sign of (foreign equity return − domestic equity return) since last rebalance
- **Month end signal strength:** Stronger when equity return differentials are large and passive AUM is high
- **Fix impact estimate:** Impact (pips) = (net fix flow USD) / (avg daily volume in pair) × scaling factor
- **Key dates:** Month and quarter end fixes are 3 to 5x more volatile than mid month
- **Post fix reversal:** 40 to 60% of the pre fix move reverses within 30 minutes of the window closing

## Prerequisites
- [[FX Market Hours]]
- [[Bid-Ask Spread]]
- [[Market Impact]]
- [[NAV]]
- [[Index Rebalancing]]

## Related concepts (learn next)
- [[FX Market Hours]]: the fix occurs during the London/NY overlap.
- [[Flow Signals]]: fix related flow is the most studied predictable flow pattern in FX.
- [[TWAP]]: banks typically execute fix orders via time weighted algorithms in and around the window.
- [[Internalization]]: banks may internalize fix flow against their own book.
- [[Positioning Signal]]: extreme positioning into the fix can cause the post fix reversal to overshoot.
- [[Carry Cross Asset]]: carry trades rebalancing at the fix create additional predictable flow.
- [[ECN]]: fix window volume on [[EBS]] and [[Reuters Matching]] spikes 5 to 10x normal.

## Common misconceptions

**"The fix is a single price set by banks."** Since the 2015 reforms it is a transparent median of observed market transactions in a 5 minute window, not a panel rate. The old methodology was vulnerable to manipulation.

**"Fix flow is always predictable."** Month end equity rebalancing creates a directional bias, but idiosyncratic flows (sovereign wealth, M&A hedging) can dominate any given fix and are not publicly visible.

**"Trading around the fix is front running."** Legitimate pre positioning by banks executing client fix orders is legal. The illegal conduct in 2013 to 2015 involved collusion between dealers sharing client information and coordinating trades.

## Sources
- Evans, Martin D.D., "FX Trading and Exchange Rate Dynamics," Journal of Finance (2002)
- Melvin, Michael and Shand, Duncan, "Active Currency Trading and the London Fix," Journal of Financial Economics (2017)
- Financial Stability Board, "Foreign Exchange Benchmarks: Final Report" (2014)
- Bank of England, "Fair and Effective Markets Review" (2015)
