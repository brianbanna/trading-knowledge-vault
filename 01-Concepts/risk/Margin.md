---
aliases: [margin, initial margin, variation margin, maintenance margin, margin call]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Margin

## Definition
Margin in futures trading is the collateral (cash or eligible securities) that a trader must deposit with the clearinghouse to guarantee performance on a [[Futures Contract]] position. Initial margin is the amount required to open a position, typically set at 5 to 15% of the contract's notional value. Maintenance margin is the minimum account balance required to keep the position open, usually 70 to 80% of initial margin. When the account balance falls below maintenance margin due to adverse price moves, the trader receives a margin call and must deposit additional funds (back to the initial margin level) within a specified timeframe, often by the next morning's opening. If the margin call is not met, the broker or clearinghouse liquidates the position to limit further losses. Variation margin is the daily cash flow from mark to market settlement: at the end of each trading day, gains are credited and losses are debited. Exchanges set margin levels using statistical models (SPAN, PRISMA) that estimate the maximum expected 1 day loss at a specified confidence level, typically 99%.

## Why it matters (commodities and FX)
Margin is the mechanism that makes futures leveraged instruments, which amplifies both gains and losses. A 10% margin requirement implies 10x leverage: a 5% price move creates a 50% change in account equity. During volatile periods, exchanges raise margin requirements (sometimes intraday), forcing traders to either post more collateral or reduce positions. This forced deleveraging can create cascading selling pressure that amplifies price moves beyond what fundamentals would justify. The April 2020 WTI negative price event, the March 2022 LME nickel squeeze ($100,000/tonne), and the 2022 European natural gas spike all involved massive margin calls that forced liquidations worth billions of dollars. Understanding margin dynamics is essential for position sizing, risk management, and recognizing when market moves are driven by margin mechanics rather than fundamentals.

## Concrete example
**Success case:** A trader buys 5 COMEX gold contracts at $2,400/oz. Notional: 5 x 100 oz x $2,400 = $1,200,000. Initial margin: ~$11,000 per contract x 5 = $55,000 (4.6% of notional). Gold rallies to $2,500/oz. Profit: 5 x 100 x $100 = $50,000, a 91% return on the $55,000 margin posted. The leverage transformed a 4.2% spot move into a 91% return on capital.

**Failure case:** The same trader buys 5 COMEX gold contracts at $2,400/oz with $55,000 margin. Gold drops to $2,350/oz (down $50). Loss: 5 x 100 x $50 = $25,000. Account balance falls to $30,000. Maintenance margin is ~$10,000 x 5 = $50,000. The account is $20,000 below maintenance, triggering a margin call for $25,000 (back to initial margin level). If the trader cannot post funds by the deadline, the broker liquidates all 5 contracts at the current $2,350 price, crystallizing the $25,000 loss. If gold gaps lower on a weekend, the trader's losses could exceed the total margin posted.

## Key mechanics and formulas
- **Leverage = Notional value / Initial margin.** A $6,000 margin on an $80,000 WTI contract = 13.3x leverage.
- **Margin call trigger:** Account balance < Maintenance margin
- **Margin call amount = Initial margin - Current account balance** (restores to initial margin level)
- **Typical initial margins:** WTI crude ~$7,000 (8 to 9% of notional); Gold ~$11,000 (4 to 5%); Corn ~$1,500 (6 to 7%); E mini S&P ~$12,000 (4 to 5%)
- **SPAN margining:** CME's Standard Portfolio Analysis of Risk system estimates margin based on a range of price scenarios, volatility shifts, and time decay. Spread positions receive margin credits recognizing their offsetting risk.
- **Intraday margin calls:** During extreme volatility, exchanges can issue intraday margin calls requiring immediate funding, compressing the timeframe for deleveraging decisions.

## Prerequisites
- [[Futures Contract]]

## Related concepts (learn next)
- [[Futures Contract]] is the instrument for which margin serves as the core risk management mechanism.
- [[Spread Trade]] positions receive reduced margin requirements because the exchange recognizes the offsetting risk between legs.
- [[Implied Volatility]] increases typically lead exchanges to raise margin requirements, creating a feedback loop.
- [[Delivery]] approaching expiry often triggers increased margin requirements to ensure only qualified participants hold positions.
- [[Basis Risk]] means that margin on a hedge position does not guarantee the hedge will fully protect the underlying exposure.
- [[Option]] sellers post margin (since they have open ended risk), while option buyers pay the full premium upfront and do not face margin calls.
- [[Contango Roll Cost]] and [[Backwardation Roll Gain]] do not directly affect margin, but the roll process creates brief periods of doubled margin when both old and new positions are open.

## Common misconceptions
- **"Margin is like a down payment."** Margin is performance collateral, not a partial purchase. The trader is responsible for the full P&L of the position, which can far exceed the margin posted.
- **"You can only lose what you put up."** In extreme cases (overnight gaps, limit moves, illiquid markets), losses can exceed the entire margin balance, leaving the trader owing the broker additional funds.
- **"Margin calls only happen to small retail traders."** The 2022 European energy margin call crisis required major utilities (Uniper, EDF) and trading houses to post billions in additional collateral within days, threatening corporate solvency.
- **"Higher margin means the exchange thinks the market will crash."** Margin reflects expected volatility in both directions, not a directional view. Exchanges raise margins to protect clearinghouse integrity, not to signal market direction.

## Sources
- CME Group, "Understanding Margin in Futures Trading"
- CME SPAN: Standard Portfolio Analysis of Risk methodology
- John Hull, "Options, Futures, and Other Derivatives"
- Pirrong, C., "The Economics of Central Counterparty Clearing"
