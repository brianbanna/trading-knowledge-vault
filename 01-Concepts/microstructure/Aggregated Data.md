---
aliases: [aggregated data, OHLC bars, bar data, time bars]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-20"
---

# Aggregated Data

## Definition
Aggregated data refers to market data that has been compressed from individual [[Tick Data|tick-level]] events into summary statistics over fixed intervals, most commonly Open-High-Low-Close-Volume (OHLCV) bars. A 5 minute OHLC bar, for example, records the first trade price (Open), highest trade price (High), lowest trade price (Low), last trade price (Close), and total volume within that 5 minute window. Aggregation makes data dramatically more manageable: a full day of EURUSD tick data (millions of records) compresses to 288 five-minute bars or 1,440 one-minute bars. Most medium-frequency systematic strategies (holding periods of minutes to days) are researched and executed using aggregated data, typically at 1 minute, 5 minute, 15 minute, or 1 hour intervals. The tradeoff is information loss: the precise sequence of trades, [[Depth of Book|order book]] dynamics, and intra-bar volatility patterns are discarded during aggregation.

## Why it matters (commodities and FX)
For FX and commodity traders operating at medium frequency, aggregated data is the practical workhorse. A [[CTA]] running trend-following strategies across 50 futures markets uses daily or hourly bars, not tick data, because the signal-to-noise ratio at their holding period (days to weeks) does not benefit from sub-second granularity. Commodity markets with lower tick frequency (e.g., agricultural futures, some metals) produce clean OHLC bars because there are fewer microstructure artifacts. In FX, 1 to 5 minute bars from [[ECN]]s are the standard input for intraday momentum, mean-reversion, and [[carry]] strategies. However, aggregated data introduces specific biases: the choice of bar boundary (e.g., bars aligned to the hour vs. offset by 30 minutes) can change the apparent performance of a strategy, and volume bars or dollar bars sometimes outperform time bars because they normalize for varying activity levels.

## Concrete example
A systematic FX fund backtests a EURUSD mean-reversion strategy on 5 minute bars from 2015 to 2025. The strategy sells when the price exceeds the 20 bar upper Bollinger Band and buys when it drops below the lower band. Using 5 minute bars, the strategy generates a Sharpe ratio of 1.8 in backtesting. The fund then runs the same logic on 1 minute bars and finds the Sharpe drops to 0.9 because the higher noise at 1 minute frequency generates many more false signals. On daily bars, the Sharpe is only 0.6 because the signal is too slow to capture intraday mean reversion. The optimal aggregation window depends on the strategy's holding period and the market's mean-reversion time scale. In a cautionary case, a researcher tests momentum on hourly bars for USDJPY but aligns all bars to the UTC hour. Since the Tokyo session open does not align with UTC hour boundaries, the strategy misses session-open patterns that are visible when bars are aligned to Tokyo local time.

## Key mechanics and formulas
- **OHLCV construction**: Open = first tick price in interval; High = max tick price; Low = min tick price; Close = last tick price; Volume = sum of all tick volumes
- **Time bars**: fixed calendar intervals (1 min, 5 min, 1 hr, 1 day)
- **Volume bars**: each bar contains a fixed number of contracts or units traded; bar duration varies
- **Dollar bars**: each bar contains a fixed dollar amount of trading activity; normalizes for price changes
- **Tick bars**: each bar contains a fixed number of trades; normalizes for varying trade frequency
- **Bar return**: R = (Close - Open) / Open; or log return = ln(Close / Open)
- **Realized volatility from bars**: RV = sqrt((252 / n) x sum of (close-to-close returns)^2) for n bars per day; this underestimates true volatility compared to tick-based RV
- **Information loss**: Intra-bar path information (e.g., did the price hit the high before the low?) is lost in standard OHLCV aggregation

## Prerequisites
- [[Tick Data]]
- [[Time Series]]
- [[Volatility]]

## Related concepts (learn next)
- [[Tick Data]]: the raw input from which aggregated data is constructed; preserves all information.
- [[Top of Book]]: OHLC bars typically use trade prices, not quote mid-prices; the distinction matters for spread-sensitive analysis.
- [[Flow Signals]]: some flow information (e.g., buyer vs. seller initiated volume) can be partially preserved in aggregated data using trade classification algorithms.
- [[Momentum Cross Asset]]: most trend-following models use daily or weekly aggregated data.
- [[Value Cross Asset]]: value signals typically use daily or monthly closing prices.
- [[Carry Cross Asset]]: carry calculations use daily closing rates and published interest rate data.
- [[Skew Microstructure]]: book skew information is entirely lost in standard OHLCV aggregation.

## Common misconceptions
1. **"Daily bars are sufficient for all strategy research"**: Many profitable patterns exist only at intraday frequencies (e.g., session-open momentum, [[FX Fix]] effects, inventory-based mean reversion). Researchers who only use daily data miss these opportunities entirely.
2. **"All 5 minute bar data is equivalent"**: Bars from different vendors may use different price sources (mid vs. last trade), different time zone alignments, and different handling of gaps or illiquid periods. These differences can change backtest results significantly.
3. **"Volume bars solve all aggregation problems"**: While volume bars normalize for activity variation, they introduce their own issues: bar boundaries become random in clock time, making multi-asset synchronization difficult, and volume bar construction is path-dependent, making it sensitive to data vendor differences.
4. **"Bars capture all the information a medium-frequency trader needs"**: Even for strategies with 1 hour holding periods, tick-level features (e.g., sweep frequency, depth dynamics) aggregated into bar-level summary statistics can add predictive power that OHLCV alone cannot provide.

## Sources
- de Prado, Marcos Lopez, "Advances in Financial Machine Learning," Wiley (2018)
- Dacorogna, Michel et al., "An Introduction to High-Frequency Finance," Academic Press (2001)
- Easley, David, de Prado, Marcos Lopez, O'Hara, Maureen, "The Volume Clock," Journal of Portfolio Management (2012)
