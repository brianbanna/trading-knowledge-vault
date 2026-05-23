---
aliases: [gap risk, jump risk, discontinuous risk, overnight gap]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Gap Risk

## Definition
Gap risk is the risk that a price jumps discontinuously from one level to another, skipping intermediate prices where a stop loss or limit order would have filled. With smooth movement, a stop at $75.00 fills near $75.00. With a gap, the market closes at $76.00 and opens at $72.00 with no trades between. Gaps occur at opens after weekends and holidays, around major releases (NFP, CPI, FOMC), during geopolitical shocks, and in illiquid markets with thin [[Order Book]]s. Gap risk cannot be hedged with simple stops because the stop triggers at the gap price, not the intended price.

## Why it matters (commodities and FX)
Commodities are exposed to gap risk because supply shocks are discrete. An OPEC emergency meeting cutting 1 million bpd over a weekend gaps [[WTI]] $5 at the Sunday open. Hurricane landfall on the US Gulf gaps [[Natural Gas]] 10%+ as production shuts in. In FX, central bank surprises are the dominant driver. The BOJ's unscheduled YCC adjustment in December 2022 gapped [[USDJPY]] 400 pips in minutes. For anyone holding through these events, the actual loss is multiples of what the stop implied.

## Concrete example
**Concrete:** A trader is short 100 lots of NYMEX [[WTI]] at $80.00 with a stop at $81.00 (intended risk: 100 × $1.00 × 1,000 = $100,000). On Saturday, Iran attacks Saudi oil infrastructure. Sunday evening WTI opens at $87.50, a $7.50 gap from Friday's $80.00 close. The stop at $81.00 triggers but the first available price is $87.50. Loss: 100 × $7.50 × 1,000 = $750,000. The trader expected $100,000 risk and lost 7.5x that. The stop was effectively meaningless. Only an option put or being flat over the weekend would have capped the loss.

**Simplified:** A stop loss is a market order triggered at a price level. If the price never trades through that level (because it jumped past it), the stop fills at whatever is available on the other side of the gap. Your "risk" was an illusion. Real protection against gaps comes from options (which pay off at any post gap level) or not holding the position when a gap is possible. Sizing assuming smooth markets is the most common way leveraged traders blow up.

## Key mechanics and formulas
**Gap magnitude:**
G = P_open − P_close_prev

**True risk with gap allowance:**
Risk_true = Q × (S + G_expected)
where Q = position size, S = intended stop distance, G_expected = max expected gap. Jump diffusion models capture this better than standard normal [[Value at Risk]].

**Gap frequency (energy futures, approximate):**
- Weekend gaps > 1%: ~10/year
- OPEC meeting gaps > 2%: 2 to 4/year
- Geopolitical shock gaps > 5%: 1 to 2/year
- Black swan gaps > 10%: less than 1/year

**Options as gap protection:**
Put_payoff = max(K − P_gap, 0) × Q
Unlike a stop, a put pays at any gap level. Cost is the premium.

## Prerequisites
- [[Volatility]]
- [[Liquidity Risk]]
- [[Overnight Risk]]
- [[Slippage]]

## Related concepts (learn next)
- [[Overnight Risk]] — gap risk is the primary component of overnight risk.
- [[Tail Risk]] — gaps are a physical manifestation of fat tails.
- [[Expected Shortfall]] — captures average loss in gap scenarios better than [[Value at Risk]].
- [[Options]] — only instrument that provides guaranteed gap protection.
- [[Circuit Breaker]] — exchange mechanism that limits intraday gap size by halting trading.
- [[Kill Switch]] — must handle the case of coming online to an already breached limit.
- [[Margin]] — exchanges raise margin before known event risks to protect against gaps.

## Common misconceptions
1. **"My stop loss protects me from gaps."** Stops become market orders when triggered. If the market gaps through, the fill is at the gap level, not the stop level. Stops protect against gradual moves, not jumps.
2. **"Gaps only happen over weekends."** Intraday gaps occur in flash crashes, surprise releases, and breaking news. The May 2010 flash crash gapped the S&P 500 and correlated commodities 5%+ in minutes intraday.
3. **"Reducing size eliminates gap risk."** Smaller positions reduce dollar impact, not gap probability or magnitude. A 1 lot position with a $5 gap loses $5,000 on WTI, proportionally identical to a larger one. The right tool is staying out of the event or buying [[Options]] protection.

## Sources
- Taleb, N.N. (2007). *The Black Swan*. Random House.
- CME Group. "Price Limits and Circuit Breakers." cmegroup.com.
- Cont, R. and Tankov, P. (2004). *Financial Modelling with Jump Processes*. Chapman & Hall.
