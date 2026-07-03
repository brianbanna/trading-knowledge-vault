---
aliases: [variance swap, var swap, realized variance swap]
tags:
  - "#energy"
  - "#quant"
  - "#risk"
date-added: "2026-07-03"
---

# Variance Swap

## Definition
A variance swap is a bet on how much the price moves over a period, with no bet on which way it moves and no option to babysit. You and a dealer agree today on a strike, a number for how volatile the underlying will be. At the end you measure how volatile it actually was, the [[Realized Volatility]]. Whoever was right gets paid the gap. One number settled against one number. No [[strike price]] to pick for a payoff shape, no [[Delta]] to hedge, no [[Theta]] bleeding you. It is the cleanest instrument to express a pure [[Volatility]] view. Under the hood it is a fixed basket of options across every strike weighted by 1/K², and that specific weighting is what holds the vol exposure constant no matter where the price goes. You do not need the replication to trade it, you need the result: constant, pure exposure to how much the market moved, path be damned.

## Why it matters (commodities and FX)
Honest read: this is a vol desk instrument with near zero relevance as a trade on a physical commodity or [[Freight]] desk. Users are institutional vol sellers and macro vol funds, not treasuries. It is kept here for the tail mechanic, which is the same mathematics as the [[Value at Risk]] and [[Expected Shortfall]] work: variance sums squared returns, so one shock dominates the window, which is exactly why a 99% VaR quantile is blind to how bad the tail gets. Liquidity is real only in deep energy, [[Brent Crude|Brent]], [[WTI Crude|WTI]], [[Henry Hub]], [[TTF]], thin in gold and copper, effectively absent in agriculturals where vol exposure stays in [[Straddle]] form. Short variance is the textbook case of a position that looks like a steady premium and is secretly short the tail: collect 50k in a quiet month, lose 1.24m in a day. Selling variance, selling deep [[OTM]] puts, and picking up pennies in front of a steamroller are the same shape.

## Concrete example
**Concrete:** Brent, 1 month swap, 21 trading days. You and the bank agree a strike of 30% annualized vol. The dealer quotes a vega notional of $10,000 per vol point.

Near the strike the P&L feels like a clean linear vol bet. If crude moves like 35% realized vol, the long side makes roughly 10,000 × 5 = $50,000. If it moves like 25%, the long side loses roughly $50,000. Simple, linear, feels like trading vol directly. Hold onto the word "roughly," it is where the instrument bites.

Now the tail. 20 days are normal, contributing at the 30% baseline. On 1 day crude moves 25%, a 2020 type or geopolitical spike. That single day contributes 0.25² = 0.0625 to the sum of squared returns, which swamps everything around it. Annualized realized vol for the month comes out near 91%, not 30. One day did that.

Price the short. Near the strike he was thinking in vol, expecting to collect maybe $50,000 for a quiet month. But the swap settles on variance, vol squared, not on vol. Realized variance blew from 900 to about 8,360 in vol point terms. His loss is not 10,000 × (91 − 30). It is the variance notional times the variance gap: (10,000 / (2 × 30)) × (8,360 − 900) ≈ $1.24 million. On a position sized to earn 50k, one day cost 25 times that. Long variance is the mirror: downside capped near the premium paid, windfall when the tail hits. That is [[Convexity]]: long variance is long convexity, short variance is short it.

**Simplified:** You agree on a number for how much crude will wiggle this month. At month end you measure how much it actually wiggled and settle the difference. Because the settlement squares each day's move, one giant day counts far more than its share, so the seller can collect small money for months and then get destroyed by a single shock.

## Key mechanics and formulas
- **Realized variance (annualized)** = (A / N) × Σ r_i², where r_i is the daily log return, N is the number of returns, and A is the annualization factor (252). Worked: (252 / 21) × (0.25² + 20 × 0.30²/252) = 0.836, so realized vol = sqrt(0.836) = 91.4%.
- **Long variance P&L** = Variance Notional × (realized variance − strike variance), with variance quoted in vol points squared (so 30% strike → strike variance = 900).
- **Variance notional** = Vega Notional / (2 × strike vol). Worked: 10,000 / (2 × 30) = $166.67 per variance point.
- **Vega notional** = P&L per 1 vol point of realized vs strike, but only near the strike. The relationship is linear in vol only locally; far from the strike the variance settlement makes P&L convex in vol.
- **Why 1/K² weighting** = a static portfolio of options weighted by 1/strike² replicates variance, giving vol exposure that stays constant as spot moves, unlike a single [[Straddle]] whose [[Gamma]] shrinks the exposure as spot walks away.

## Prerequisites
- [[Realized Volatility]]
- [[Implied Volatility]]
- [[Volatility]]
- [[Straddle]]
- [[Vega]]

## Related concepts (learn next)
- [[Straddle]]: the option based way to trade vol, contaminated by strike choice, gamma, theta, and hedging cost that the variance swap strips out
- [[Strangle]]: the OTM cousin of the straddle, same contamination, sits next to this note in the volatility cluster
- [[Vega]]: the exposure a variance swap delivers in pure form, quoted as vega notional near the strike
- [[Tail Risk]]: squaring returns is what makes short variance a short tail position, blowing past any normal expectation
- [[Expected Shortfall]]: the average loss beyond the VaR quantile, the metric that captures the variance tail that VaR misses
- [[Value at Risk]]: the quantile risk number that understates short variance because it does not see how deep the tail goes
- [[Convexity]]: long variance is long convexity, the reason its downside is capped and its upside is not
- [[Freight Options]]: FFA optionality exists on Baltic routes, but no real variance swap market, so route vol stays in option form

## Common misconceptions
1. **"It is a clean linear vol bet."** True only near the strike. The swap settles on variance, vol squared, so once a large move hits, the squared term dominates and the payoff is sharply convex in vol. The short who reasoned in vol points massively understates the loss.
2. **"Long and short are symmetric."** Long variance is long convexity: downside capped near the premium, upside unbounded when the tail hits. Short variance is the reverse, a steady premium hiding an unbounded single day loss. The purity that makes it clean is exactly what makes it lethal short, nothing else in the P&L, no theta collected, no offsetting leg, to dilute one catastrophic day.
3. **"It removes the risk of options."** It removes the hedging noise and strike selection, not the vol risk. It concentrates the tail. 2020 crude and the 2022 European gas dislocation handed variance sellers losses far past anything a normal distribution allowed for.
4. **"Corporates can use it to hedge."** Rarely. The operational complexity exceeds the benefit for a treasury. The structure exists for the trading floor, not the treasury floor.

## Sources
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives. Chapter on variance swaps and the 1/K² replication.
- Demeterfi, Derman, Kamal, Zou. *More Than You Ever Wanted to Know About Volatility Swaps*, Goldman Sachs Quantitative Strategies, 1999.
- Carr, Peter, and Dilip Madan. *Towards a Theory of Volatility Trading*.
- CBOE. *VIX White Paper* (the variance replication logic behind the index).
