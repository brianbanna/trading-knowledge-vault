---
aliases: [position limit, position cap, exposure limit, holding limit]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Position Limit

## Definition
A position limit is the maximum number of contracts or units a trader or firm can hold, long or short, in a given instrument. Limits exist at multiple levels: exchange limits (CME, ICE, LME), regulatory limits (CFTC, FCA), clearing firm limits (FCM), and internal firm limits. The binding constraint is whichever is smallest. Position limits prevent any single participant from accumulating enough size to manipulate the market or pose systemic risk, and they protect the firm from outsized losses on a single bet.

## Why it matters (commodities and FX)
Commodity markets are exposed because physical delivery is involved. If a trader holds more contracts than the deliverable supply, they can create an artificial [[Squeeze]], distorting prices for real producers and consumers. The CFTC sets federal speculative limits on 25 core agricultural and energy contracts including [[WTI]], [[Natural Gas]], [[Corn]], and [[Gold]]. In FX, there are no exchange level limits since most trades OTC, but banks and prop firms enforce strict internal limits. A junior bank FX trader might have a [[EURUSD]] limit of $50M notional; a senior trader $500M.

## Concrete example
**Concrete:** A speculative fund trades NYMEX WTI futures. CFTC spot month limit is 6,000 contracts. Fund internal limit is 2,000. The fund is long 1,800 at $76.00 when a bullish signal appears to add 500. The risk system blocks the order because 1,800 + 500 = 2,300 exceeds the 2,000 cap. The trader adds 200 to reach the limit. Price rallies to $79.00. Profit: 2,000 × $3 × 1,000 = $6M. The limit prevented a larger position; the discipline is the point. A larger position might have moved more on the way up, but on the way down would have crushed the fund.

**Simplified:** Position limits cap how big you can go. Exchanges and regulators set them to prevent any one player from cornering a market. Firms set tighter internal limits to cap how badly a single bet can hurt them. The limit is enforced by the risk system: orders that would breach get blocked. Soft and hard tiers usually exist (warning at 75% of the cap, hard block at 100%). The cap is dollars at risk, not just contracts: notional exposure is what really matters.

## Key mechanics and formulas
**Utilization:** U = |Q| / L
U = utilization (0 to 1), Q = current net position, L = limit. Firms set [[Soft Limit]] at U = 0.75 and [[Hard Limit]] at U = 1.0.

**Notional exposure:** N = Q × contract_size × P
contract_size = units per contract (e.g., 1,000 barrels WTI), P = current price.

**CFTC spot month limits (selected):**
- WTI crude: 6,000 contracts
- NYMEX natural gas: 2,000
- COMEX gold: 6,000
- CBOT corn: 1,200
- ICE cocoa: 4,900

## Prerequisites
- [[Margin]]
- [[PnL]]
- [[Liquidity Risk]]

## Related concepts (learn next)
- [[Soft Limit]] — warning threshold (75% of the position limit) where the trader should reduce exposure.
- [[Hard Limit]] — absolute cap where the system blocks new orders.
- [[Accountability Level]] — CFTC threshold below the hard limit where the exchange may ask a trader to explain a position.
- [[Daily Loss Limit]] — complementary control limiting P&L drawdown rather than size.
- [[Margin]] — capital required to hold the position, which can act as a de facto limit.
- [[Squeeze]] — the manipulation that position limits are designed to prevent.
- [[Value at Risk]] — converts the position limit into a dollar risk number.

## Common misconceptions
1. **"Exchange limits apply to everyone."** Bona fide hedgers (producers, refiners, merchants) can apply for hedge exemptions allowing positions above speculative limits. A physical crude trader hedging pipeline inventory may hold 20,000 WTI with a valid exemption.
2. **"I only need to worry about one contract month."** The CFTC imposes both spot month and all-months-combined limits. A trader spread across 12 months can breach the aggregate cap.
3. **"Limits and margin are the same thing."** [[Margin]] limits capital required; position limits cap contracts regardless of capital. A well capitalized fund can afford margin on 10,000 WTI but is legally capped at 6,000.

## Sources
- CFTC. "Speculative Position Limits." cftc.gov.
- CME Group. "Position Limits." cmegroup.com.
- ICE. "Position Limit, Position Management and Accountability Levels." ice.com.
