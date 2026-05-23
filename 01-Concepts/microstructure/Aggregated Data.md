---
aliases: [aggregated data, OHLC bars, bar data, time bars]
tags:
  - "#microstructure"
  - "#quant"
date-added: "2026-03-20"
---

# Aggregated Data

## Definition
Aggregated data is market data compressed from individual [[Tick Data|tick]] events into summary statistics over fixed intervals, usually Open High Low Close Volume (OHLCV) bars. A 5 minute bar records the first trade price (Open), highest (High), lowest (Low), last (Close), and total volume in that window. A full day of EURUSD ticks (millions of records) compresses to 288 five minute bars or 1,440 one minute bars. Most medium frequency strategies (minutes to days) are researched and executed on aggregated data at 1, 5, 15, or 60 minute intervals. The cost is information loss: trade sequence, [[Depth of Book|order book]] dynamics, and intra bar volatility patterns are discarded.

## Why it matters (commodities and FX)
For medium frequency FX and commodity traders, aggregated data is the practical workhorse. A [[CTA]] running trend following across 50 futures uses daily or hourly bars, not ticks, because signal to noise at days to weeks horizons does not gain from sub second granularity. Commodity markets with low tick frequency (ag futures, some metals) produce clean OHLC bars because there are fewer microstructure artifacts. In FX, 1 to 5 minute bars from [[ECN]]s are the standard input for intraday momentum, mean reversion, and [[carry]] strategies. Aggregated data introduces biases: bar boundary choice (hour aligned vs offset 30 minutes) changes apparent performance, and volume or dollar bars sometimes beat time bars by normalizing for activity.

## Concrete example

**Concrete:** Systematic FX fund backtests EURUSD mean reversion on 5 minute bars from 2015 to 2025. Sell above 20 bar upper Bollinger, buy below lower band. 5 minute bars: Sharpe 1.8. Drop to 1 minute bars: Sharpe falls to 0.9 from noise generating false signals. Daily bars: Sharpe 0.6, signal too slow to capture intraday reversion. Optimal aggregation depends on holding period and market reversion timescale. Separately, USDJPY hourly momentum aligned to UTC misses Tokyo session open patterns visible when bars align to Tokyo local time. Bar boundary choice changes results.

**Simplified:** Ticks record every trade. Bars summarize many ticks into open, high, low, close, volume over a fixed window. You lose the order of events inside the bar but the data becomes tractable. Pick the bar size to match your holding period: too small and you trade noise, too big and you miss the move.

## Key mechanics and formulas
- **OHLCV construction**: Open = first tick price; High = max; Low = min; Close = last; Volume = sum
- **Time bars**: fixed calendar intervals (1 min, 5 min, 1 hr, 1 day)
- **Volume bars**: fixed volume per bar; duration varies
- **Dollar bars**: fixed dollar amount per bar; normalizes for price changes
- **Tick bars**: fixed number of trades per bar
- **Bar return**: R = (Close - Open) / Open; or log return = ln(Close / Open)
- **Realized vol from bars**: RV = sqrt((252 / n) x sum of close to close returns^2); underestimates true vol vs tick based RV
- **Information loss**: intra bar path (did price hit high before low?) is gone in standard OHLCV

## Prerequisites
- [[Tick Data]]
- [[Time Series]]
- [[Volatility]]

## Related concepts (learn next)
- [[Tick Data]]: raw input preserving all information
- [[Top of Book]]: OHLC bars use trade prices, not quote mids; matters for spread sensitive analysis
- [[Flow Signals]]: signed flow can be partially preserved via trade classification
- [[Momentum Cross Asset]]: most trend models use daily or weekly bars
- [[Value Cross Asset]]: value signals use daily or monthly closes
- [[Carry Cross Asset]]: carry uses daily closes and published rates
- [[Skew Microstructure]]: book skew is fully lost in OHLCV

## Common misconceptions
1. **"Daily bars are enough for all research"**: many profitable patterns live only at intraday frequencies (session opens, [[FX Fix]] effects, inventory reversion). Daily only researchers miss them.
2. **"All 5 minute bars are equivalent"**: vendors differ on price source (mid vs last), time zone alignment, and gap handling. Differences shift backtests.
3. **"Volume bars solve all aggregation problems"**: they normalize activity but make bar boundaries random in clock time, hurting multi asset sync. Construction is path dependent.
4. **"Bars capture all a medium frequency trader needs"**: even at 1 hour holding, tick level features (sweep frequency, depth dynamics) aggregated as features can add predictive power that OHLCV alone cannot.

## Sources
- de Prado, Marcos Lopez, "Advances in Financial Machine Learning," Wiley (2018)
- Dacorogna, Michel et al., "An Introduction to High-Frequency Finance," Academic Press (2001)
- Easley, David, de Prado, Marcos Lopez, O'Hara, Maureen, "The Volume Clock," Journal of Portfolio Management (2012)
