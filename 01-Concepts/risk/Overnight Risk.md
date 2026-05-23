---
aliases: [overnight risk, overnight exposure, carry risk, holding risk]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Overnight Risk

## Definition
Overnight risk is the risk of holding a position when the market is closed or during low liquidity hours, exposing the trader to adverse moves they cannot react to in real time. This includes gap risk at the open, surprise news during off hours, and events in other time zones that affect the position. Overnight risk encompasses [[Gap Risk]], event risk, and [[Liquidity Risk]] during thin hours. For futures and FX, overnight can mean brief maintenance windows on near 24 hour markets or the full Friday afternoon to Sunday evening weekend closure. The critical difference from intraday risk: ability to exit or adjust is severely limited.

## Why it matters (commodities and FX)
Commodity markets are driven by physical events that ignore trading hours. A pipeline explosion in the Permian at 2 AM, a typhoon hitting Australian iron ore ports on Saturday, or a Middle East escalation over the weekend all create overnight risk for anyone holding [[WTI]], [[Iron Ore]], or [[Brent]]. In FX, the 3 major sessions (Tokyo, London, New York) mean holding [[EURUSD]] overnight in New York exposes the position to Asian and European data, central bank comments, and geopolitical events while the NY desk sleeps. Many prop firms force traders to flatten or sharply reduce positions before leaving for the day specifically because overnight risk is unmanageable.

## Concrete example
**Concrete:** A London prop trader runs a mean reversion strategy on CME [[Natural Gas]]. At 5 PM London (noon NY), the trader is long 50 lots at $2.850. The firm requires overnight positions to be no more than 25% of intraday limit. The trader reduces to 12 lots before leaving. Overnight, a warm forecast for the US Northeast sends gas down $0.15. Loss on 12 lots: 12 × $0.15 × 10,000 = $18,000. Manageable. The trader who kept all 50 lots, plus a surprise LNG cargo diversion to Europe hitting Reuters at 3 AM London, sees gas gap down $0.30. Loss: $150,000. Daily limit breached before they wake.

**Simplified:** When the market closes or thins out, you cannot reach out and exit. News flows continue. Other time zones trade. The next time you can transact at a real price, the price may be far from where you left it. Stops do not save you because they fill at whatever price exists when the market opens. The only real protection is to hold less, hedge with options, or flatten before the bell. Sizing for intraday risk and then holding overnight is one of the most common ways accounts get wiped out.

## Key mechanics and formulas
**Overnight VaR scaling:**
VaR_overnight = VaR_intraday × √(T_overnight / T_intraday) × λ
T_overnight = closed/illiquid hours, T_intraday = active hours, λ = gap risk multiplier (1.5 to 3.0) for non-normal overnight returns.

**Weekend scaling:**
For commodities (closed Sat and Sun):
VaR_weekend = VaR_daily × √(3) × λ
The √(3) reflects 3 calendar days of exposure. λ is higher because event probability rises with time.

**Overnight position limit:**
Q_overnight ≤ α × Q_intraday
α = 0.25 to 0.50 depending on firm risk appetite and instrument vol.

**Carry cost:**
C = Q × P × r / 365
r = financing rate. For leveraged positions, overnight cost includes funding.

## Prerequisites
- [[Gap Risk]]
- [[Volatility]]
- [[Liquidity Risk]]
- [[Value at Risk]]

## Related concepts (learn next)
- [[Gap Risk]] — the primary mechanism through which overnight risk materializes as losses.
- [[Daily Loss Limit]] — overnight losses hit the next day's limit, starting the day already in a hole.
- [[Margin]] — exchanges may charge higher overnight margin than intraday.
- [[Carry]] — cost or benefit of holding overnight, including financing and roll costs.
- [[Tail Risk]] — overnight returns have fatter tails than intraday due to information accumulation.
- [[Kill Switch]] — must be configured to trigger even when the primary desk is offline.
- [[Options]] — buying puts or calls before an overnight hold provides defined risk protection against gaps.
- [[Expected Shortfall]] — better than [[Value at Risk]] for overnight risk because it captures tail severity.

## Common misconceptions
1. **"FX trades 24 hours so there is no overnight risk."** FX [[Liquidity Risk]] varies by session. [[EURUSD]] during Tokyo lunch has spreads 3 to 5x wider than London. A major event in thin liquidity is effectively the same as an overnight gap.
2. **"I can set a stop loss and sleep safely."** Stops during low liquidity fill at worse prices due to wide spreads and thin books. A 1.0800 stop on EURUSD during Asia might fill at 1.0785 or worse after a surprise ECB comment.
3. **"Overnight risk is just gaps at the open."** It also covers funding costs, margin calls arriving before the trader is at their desk, and counterparty risk (especially OTC FX where the prime broker can pull credit overnight).

## Sources
- CME Group. "Margin Handbook." cmegroup.com.
- Dacorogna, M. et al. (2001). *An Introduction to High-Frequency Finance*. Academic Press.
- Hull, J. (2022). *Options, Futures, and Other Derivatives*. Pearson.
