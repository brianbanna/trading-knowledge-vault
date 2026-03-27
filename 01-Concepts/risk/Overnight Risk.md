---
aliases: [overnight risk, overnight exposure, carry risk, holding risk]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Overnight Risk

## Definition
Overnight risk is the risk of holding a position when the market is closed or during low liquidity hours, exposing the trader to adverse price moves that they cannot react to in real time. This includes the risk of price gaps at the open, surprise news during off hours, and events in other time zones that affect the position. Overnight risk encompasses [[Gap Risk]], event risk, and [[Liquidity Risk]] during thin trading hours. For futures and FX, "overnight" can mean the brief maintenance windows on nearly 24 hour markets or the full weekend closure from Friday afternoon to Sunday evening. The critical difference from intraday risk is that the trader's ability to exit or adjust is severely limited.

## Why it matters (commodities and FX)
Commodity markets are driven by physical events that do not respect trading hours. A pipeline explosion in the Permian Basin at 2 AM, a typhoon hitting Australian iron ore ports on Saturday, or a Middle East conflict escalating over the weekend all create overnight risk for anyone holding [[WTI]], [[Iron Ore]], or [[Brent]] positions. In FX, the 3 major sessions (Tokyo, London, New York) mean that holding [[EURUSD]] overnight in New York exposes the position to Asian and European data releases, central bank comments, and geopolitical events while the New York desk is asleep. Many prop firms require traders to flatten or significantly reduce positions before leaving for the day specifically because overnight risk is unmanageable.

## Concrete example
A prop trader in London runs a mean reversion strategy on CME [[Natural Gas]] futures. At 5 PM London time (noon New York), the trader is long 50 lots at $2.850.

**Win scenario (reduced overnight):** The trader's firm requires overnight positions to be no more than 25% of the intraday limit. The trader reduces to 12 lots before leaving. Overnight, a warm weather forecast for the US Northeast sends gas down $0.15. Loss on 12 lots: 12 x $0.15 x 10,000 = $18,000. Manageable.

**Fail scenario (full position overnight):** The trader keeps all 50 lots overnight because they are "certain" gas will rally. Same weather forecast, but also a surprise LNG cargo diversion to Europe hits Reuters at 3 AM London time. Gas gaps down $0.30 at the next liquid trading window. Loss: 50 x $0.30 x 10,000 = $150,000. The [[Daily Loss Limit]] is breached before the trader even wakes up.

## Key mechanics and formulas
**Overnight VaR scaling:**
VaR_overnight = VaR_intraday x √(T_overnight / T_intraday) x λ
Where T_overnight = hours the market is closed or illiquid, T_intraday = hours of active trading, λ = a gap risk multiplier (typically 1.5 to 3.0) to account for the non-normal distribution of overnight returns.

**Weekend scaling factor:**
For commodities (closed Saturday and Sunday):
VaR_weekend = VaR_daily x √(3) x λ
The √(3) comes from 3 calendar days of risk exposure. In practice, λ is higher for weekends because the probability of surprise events increases with time.

**Overnight position limit (typical rule):**
Q_overnight ≤ α x Q_intraday
Where α = 0.25 to 0.50 depending on the firm's risk appetite and the instrument's overnight volatility.

**Carry cost of overnight positions:**
C = Q x P x r / 365
Where r = financing rate. For leveraged positions, the cost of holding overnight includes funding charges.

## Prerequisites
- [[Gap Risk]]
- [[Volatility]]
- [[Liquidity Risk]]
- [[Value at Risk]]

## Related concepts (learn next)
- [[Gap Risk]] — the primary mechanism through which overnight risk materializes as losses.
- [[Daily Loss Limit]] — overnight losses count against the next day's PnL limit, potentially starting the day already in a hole.
- [[Margin]] — exchanges may charge higher overnight or "maintenance" margin than intraday margin.
- [[Carry]] — the cost or benefit of holding a position overnight, including financing and roll costs.
- [[Tail Risk]] — overnight returns have fatter tails than intraday returns due to information accumulation.
- [[Kill Switch]] — must be configured to trigger even when the primary trading desk is offline.
- [[Options]] — buying puts or calls before an overnight hold provides defined risk protection against gaps.
- [[Expected Shortfall]] — a better measure than [[Value at Risk]] for overnight risk because it captures the severity of tail scenarios.

## Common misconceptions
1. **"FX trades 24 hours so there is no overnight risk."** FX [[Liquidity Risk]] varies dramatically by session. [[EURUSD]] during the Tokyo lunch hour has spreads 3 to 5 times wider than London hours. A major event during thin liquidity is effectively the same as an overnight gap.
2. **"I can set a stop loss and sleep safely."** Stop losses during low liquidity hours may fill at significantly worse prices due to wide spreads and thin books. A stop at 1.0800 on EURUSD during Asian hours might fill at 1.0785 or worse after a surprise ECB comment.
3. **"Overnight risk is just about gaps at the open."** Overnight risk also includes funding costs, margin calls that arrive before the trader is at their desk, and counterparty risk (especially in OTC FX where the prime broker might pull credit overnight).

## Sources
- CME Group. "Margin Handbook." cmegroup.com.
- Dacorogna, M. et al. (2001). *An Introduction to High-Frequency Finance*. Academic Press.
- Hull, J. (2022). *Options, Futures, and Other Derivatives*. Pearson.
