---
aliases: [gap risk, jump risk, discontinuous risk, overnight gap]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Gap Risk

## Definition
Gap risk is the risk that the price of an instrument jumps discontinuously from one level to another, skipping through intermediate prices where a trader's stop loss or limit order would have been filled. Unlike smooth price movements where a stop loss at $75.00 guarantees an exit near $75.00, a gap means the market can close at $76.00 and open at $72.00, with no trades occurring in between. Gaps occur at market opens after weekends and holidays, around major data releases (NFP, CPI, FOMC), during geopolitical shocks, and in illiquid markets where the [[Order Book]] is thin. Gap risk cannot be hedged with simple stop losses because the stop triggers at the gap price, not the intended price.

## Why it matters (commodities and FX)
Commodities are especially prone to gap risk because supply shocks are discrete events. An OPEC emergency meeting can cut production by 1 million barrels per day over a weekend, causing [[WTI]] to gap $5 at the Sunday evening open. Hurricane landfall on the US Gulf Coast can gap [[Natural Gas]] by 10%+ as production shuts in. In FX, central bank surprises are the primary gap risk driver. The Bank of Japan's unscheduled yield curve control adjustment in December 2022 gapped [[USDJPY]] 400 pips in minutes. For any trader holding positions through these events, the actual loss can be multiples of what their stop loss implied.

## Concrete example
A trader is short 100 lots of NYMEX [[WTI]] crude oil at $80.00 with a stop loss at $81.00 (risk = 100 x $1.00 x 1,000 = $100,000).

**Normal scenario (no gap):** Price rises gradually. The stop loss triggers at $81.02 (2 ticks of [[Slippage]]). Loss: 100 x $1.02 x 1,000 = $102,000. Close to the expected $100,000.

**Gap scenario:** On Saturday, Iran attacks Saudi oil infrastructure. Sunday evening, WTI opens at $87.50, a $7.50 gap from Friday's $80.00 close. The stop loss at $81.00 triggers, but the first available price is $87.50. Loss: 100 x $7.50 x 1,000 = $750,000. The trader expected to risk $100,000 but lost 7.5x that amount. The stop loss was effectively meaningless.

## Key mechanics and formulas
**Gap magnitude estimation:**
G = P_open - P_close_prev
Where G = gap size, P_open = next session opening price, P_close_prev = previous session closing price.

**True risk with gap allowance:**
Risk_true = Q x (S + G_expected)
Where Q = position size, S = intended stop distance, G_expected = estimated maximum gap. Using [[Value at Risk]] with jump diffusion models captures gap risk better than standard normal models.

**Gap frequency by event type (approximate for energy futures):**
- Weekend gaps > 1%: roughly 10 per year
- OPEC meeting gaps > 2%: 2 to 4 per year
- Geopolitical shock gaps > 5%: 1 to 2 per year
- Black swan gaps > 10%: less than 1 per year

**Options as gap protection:**
Put_payoff = max(K - P_gap, 0) x Q
Where K = put strike. Unlike a stop loss, an [[Options]] put pays off at any gap level. The cost is the premium.

## Prerequisites
- [[Volatility]]
- [[Liquidity Risk]]
- [[Overnight Risk]]
- [[Slippage]]

## Related concepts (learn next)
- [[Overnight Risk]] — gap risk is the primary component of overnight risk, since gaps occur between sessions.
- [[Tail Risk]] — gaps are a physical manifestation of fat tailed return distributions.
- [[Expected Shortfall]] — captures the average loss in gap scenarios better than [[Value at Risk]].
- [[Options]] — the only instrument that provides guaranteed gap protection (via puts or calls).
- [[Circuit Breaker]] — exchange mechanisms that limit the size of intraday gaps by halting trading.
- [[Kill Switch]] — must be designed to handle gap scenarios where the system comes online to an already breached limit.
- [[Margin]] — exchanges increase margin requirements before known event risks to protect against gaps.

## Common misconceptions
1. **"My stop loss protects me from gaps."** Stop losses become market orders when triggered. If the market gaps through the stop level, the fill price will be at or near the gap level, not the stop level. Stops protect against gradual moves, not jumps.
2. **"Gaps only happen over weekends."** Intraday gaps occur during flash crashes, surprise data releases, and breaking news. The May 2010 flash crash gapped the S&P 500 and correlated commodities by 5%+ in minutes during the trading session.
3. **"Reducing position size eliminates gap risk."** Smaller positions reduce the dollar impact of a gap but do not reduce the probability or magnitude of the gap itself. A 1 lot position with a $5 gap still loses $5,000 on WTI, proportionally the same as a larger position. The correct tool for eliminating gap risk is either not holding through the event or buying [[Options]] protection.

## Sources
- Taleb, N.N. (2007). *The Black Swan*. Random House.
- CME Group. "Price Limits and Circuit Breakers." cmegroup.com.
- Cont, R. and Tankov, P. (2004). *Financial Modelling with Jump Processes*. Chapman & Hall.
