---
aliases: [big figure, big fig, handle]
tags:
  - "#fx"
date-added: "2026-03-20"
---

# Big Figure

## Definition
The big figure (also called the "handle") is the integer or large round number portion of an exchange rate that traders typically omit when quoting prices. In EUR/USD at 1.0853, the big figure is 1.08. Dealers on the interbank market assume both parties know the big figure and quote only the last 2 digits (and fractional [[Pip|pips]]): "53" or "53 offered at 55." A move from 1.08 to 1.09 is described as "EUR/USD moved 1 big figure." For USD/JPY at 150.50, the big figure is 150, and a move to 151 represents 1 big figure or 100 pips. Big figures act as psychological levels where significant option barriers, stop losses, and order clusters tend to accumulate.

## Why it matters (commodities and FX)
Big figures serve as natural support and resistance levels because market participants anchor on round numbers. Option dealers frequently set barrier and knockout strikes at big figures (e.g., a 1.1000 EUR/USD barrier), creating hedging flows that cause price to gravitate toward or repel from these levels. For commodity hedgers executing large FX transactions, knowing the current big figure context helps set realistic limit orders and avoid the adverse selection that occurs when price approaches a contested handle. In fast markets, miscommunication about the big figure can lead to costly trade errors.

## Concrete example
EUR/USD is trading at 1.0850 and approaches the 1.0900 handle. A cluster of stop loss orders from short sellers sits above 1.0900, while option dealers have sold 1.0900 call options and need to hedge by buying EUR as spot approaches. Price accelerates through 1.0900 as stops trigger, overshoots to 1.0935, then pulls back to 1.0910. A trader who placed a buy limit at 1.0905, just above the big figure, captured the breakout. Conversely, a trader who bought at 1.0935, chasing the breakout above the big figure, was caught in the pullback and stopped out at 1.0895, a 40 pip loss.

## Key mechanics and formulas
- **Big figure for EUR/USD at 1.0853**: 1.08. The "small figure" or dealing price is 53.
- **Big figure for USD/JPY at 150.50**: 150. The dealing price is 50.
- **1 big figure** = 100 [[Pip|pips]] for most pairs. EUR/USD from 1.0800 to 1.0900 = 1 big figure = 100 pips.
- **1 big figure for JPY pairs** = 100 pips = 1.00. USD/JPY from 150.00 to 151.00 = 1 big figure.
- **Psychological levels**: Double zeros (1.1000, 150.00) and half figures (1.0850, 150.50) attract the most order flow and options activity.
- **Dealer quoting convention**: Only the last 2 digits are quoted voice. "The euro is 50/53" means EUR/USD bid 1.0850, offer 1.0853.

## Prerequisites
- [[Currency Pair]]
- [[Pip]]
- [[Spot Rate]]

## Related concepts (learn next)
- [[Pip]]: the smallest standard unit of price change, with 100 pips making up 1 big figure.
- [[Spot Rate]]: the full exchange rate from which the big figure is extracted.
- [[Major Pairs]]: the most commonly traded pairs where big figure conventions are most standardized.
- [[Bid-Ask Spread]]: quoted in the small figure portion, with the big figure assumed known by both parties.
- [[Option Barrier]]: barriers and knockouts frequently placed at big figures, creating predictable hedging flows.
- [[Order Flow]]: big figures attract stop losses and limit orders, concentrating flow at round numbers.

## Common misconceptions
1. **Big figures only matter psychologically**: They have real mechanical effects. Option barriers at big figures force dealers to hedge dynamically, creating measurable price magnetism or repulsion documented in academic research.
2. **Every big figure is equally important**: Double zero levels (1.1000, 1.2000) carry far more significance than intermediate handles (1.0800, 1.0900) because they attract larger option notionals and more media attention.
3. **The big figure convention is universal**: In EM pairs with large numbers (USD/KRW at 1,350), the "big figure" concept breaks down. Traders use percentage moves or specific levels rather than the traditional big figure shorthand.

## Sources
- Osler, Carol, "Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis," Journal of Finance, 2003.
- Lyons, Richard K., *The Microstructure Approach to Exchange Rates*, MIT Press, 2001.
- Lien, Kathy, *Day Trading and Swing Trading the Currency Market*, 3rd ed.
