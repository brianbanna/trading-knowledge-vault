---
aliases: [position limit, position cap, exposure limit, holding limit]
tags:
  - "#risk"
date-added: "2026-03-27"
---

# Position Limit

## Definition
A position limit is the maximum number of contracts or units a trader or firm is allowed to hold, either long or short, in a given instrument. Position limits exist at multiple levels: exchange imposed limits set by CME, ICE, or LME; regulatory limits set by the CFTC or FCA; clearing firm limits set by the FCM; and internal firm limits set by the risk team. The binding constraint is whichever is smallest. Position limits prevent any single participant from accumulating enough size to manipulate the market or pose systemic risk, and they protect the firm from outsized losses on a single bet.

## Why it matters (commodities and FX)
Commodity markets are particularly sensitive to position limits because physical delivery is involved. If a trader holds more contracts than the deliverable supply of the underlying, they can create an artificial [[Squeeze]], distorting prices for real producers and consumers. The CFTC sets federal speculative position limits on 25 core agricultural and energy contracts including [[WTI]] crude oil, [[Natural Gas]], [[Corn]], and [[Gold]]. In FX, there are no exchange level position limits because most FX trades OTC, but banks and prop firms impose strict internal limits. A junior trader at a bank FX desk might have a [[EURUSD]] limit of $50 million notional, while a senior trader might have $500 million.

## Concrete example
A speculative commodity fund trades NYMEX WTI crude oil futures. The CFTC spot month position limit for WTI is 6,000 contracts (6 million barrels). The fund's internal limit is 2,000 contracts.

**Win scenario:** The fund is long 1,800 contracts at $76.00 when they get a bullish signal to add 500 more. The risk system blocks the order because 1,800 + 500 = 2,300 exceeds the 2,000 contract internal limit. The trader adds only 200 to reach the cap. Price rallies to $79.00. Profit: 2,000 x 3.00 x 1,000 = $6,000,000. The limit prevented the trader from taking a larger position, but the discipline is the point.

**Fail scenario:** The same fund has no internal limit and builds to 5,500 contracts (near the CFTC limit). A surprise SPR release announcement sends WTI from $76.00 to $71.00. Loss: 5,500 x 5.00 x 1,000 = $27,500,000. The position is so large that liquidating it causes further [[Market Impact]], and the actual loss is $32 million after [[Slippage]]. The fund faces redemptions and a CFTC investigation.

## Key mechanics and formulas
**Position limit utilization:** U = |Q| / L
Where U = utilization (0 to 1), Q = current net position (contracts), L = position limit. Firms typically set [[Soft Limit]] at U = 0.75 and [[Hard Limit]] at U = 1.0.

**Notional exposure:** N = Q x contract_size x P
Where N = notional value, Q = contracts, contract_size = units per contract (e.g., 1,000 barrels for WTI), P = current price.

**CFTC spot month limits (selected):**
- WTI crude oil: 6,000 contracts
- NYMEX natural gas: 2,000 contracts
- COMEX gold: 6,000 contracts
- CBOT corn: 1,200 contracts
- ICE cocoa: 4,900 contracts

## Prerequisites
- [[Margin]]
- [[PnL]]
- [[Liquidity Risk]]

## Related concepts (learn next)
- [[Soft Limit]] — a warning threshold (typically 75% of the position limit) where the trader should begin reducing exposure.
- [[Hard Limit]] — the absolute cap where the system blocks new orders that would increase exposure.
- [[Accountability Level]] — a CFTC threshold below the hard limit where the exchange may ask a trader to explain their position.
- [[Daily Loss Limit]] — a complementary risk control that limits PnL drawdown rather than position size.
- [[Margin]] — the capital required to hold the position, which can act as a de facto position limit.
- [[Squeeze]] — the market manipulation that position limits are designed to prevent.
- [[Value at Risk]] — converts the position limit into a dollar risk number for the risk team.

## Common misconceptions
1. **"Exchange position limits apply to everyone."** Bona fide hedgers (producers, refiners, merchants) can apply for hedge exemptions that allow positions above speculative limits. A physical crude oil trader hedging pipeline inventory may hold 20,000 WTI contracts with a valid exemption.
2. **"I only need to worry about my position in 1 contract month."** The CFTC imposes both spot month limits and all months combined limits. A trader spread across 12 monthly contracts can still breach the aggregate limit.
3. **"Position limits and margin are the same thing."** [[Margin]] limits how much capital is required; position limits cap the number of contracts regardless of available capital. A well capitalized fund can afford the margin on 10,000 WTI contracts but is still legally capped at 6,000.

## Sources
- CFTC. "Speculative Position Limits." cftc.gov.
- CME Group. "Position Limits." cmegroup.com.
- ICE. "Position Limit, Position Management and Accountability Levels." ice.com.
