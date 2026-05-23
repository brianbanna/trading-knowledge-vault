---
aliases: [margin, initial margin, variation margin, maintenance margin, margin call]
tags:
  - "#risk"
date-added: "2026-03-20"
---

# Margin

## Definition
Margin is the collateral (cash or eligible securities) a trader must deposit with the clearinghouse to guarantee performance on a [[Futures Contract]] position. Initial margin is the amount to open a position, typically 5 to 15% of notional. Maintenance margin is the minimum balance to keep the position open, usually 70 to 80% of initial. When the balance falls below maintenance due to adverse moves, the trader receives a margin call and must deposit additional funds (back to initial margin) within a deadline, often by the next morning's open. If unmet, the broker liquidates the position. Variation margin is the daily cash flow from mark to market: gains credit, losses debit. Exchanges set margin via statistical models (SPAN, PRISMA) estimating the maximum expected 1 day loss at 99% confidence.

## Why it matters (commodities and FX)
Margin is the mechanism that makes futures leveraged. A 10% margin requirement implies 10x leverage: a 5% price move creates a 50% change in account equity. In volatile periods, exchanges raise margin (sometimes intraday), forcing traders to post collateral or reduce positions. Forced deleveraging creates cascading selling that amplifies moves beyond fundamentals. The April 2020 WTI negative price event, the March 2022 LME nickel squeeze ($100,000/tonne), and the 2022 European natural gas spike all involved massive margin calls forcing liquidations worth billions. Understanding margin dynamics is essential for sizing, risk management, and recognizing when moves are driven by margin mechanics rather than fundamentals.

## Concrete example
**Concrete:** A trader buys 5 COMEX gold contracts at $2,400/oz with $55,000 initial margin (4.6% of $1.2M notional). Gold drops to $2,350/oz. Loss: 5 × 100 × $50 = $25,000. Balance falls to $30,000. Maintenance margin is ~$50,000. The account is $20,000 below maintenance, triggering a $25,000 call to restore initial margin. If the trader cannot post by the deadline, the broker liquidates all 5 contracts at $2,350, crystallizing the loss. If gold gaps lower on a weekend, losses can exceed total margin posted, leaving the trader owing additional funds.

**Simplified:** Margin is not a down payment. It is collateral that guarantees you can pay your losses. You are responsible for the full P&L of the contract, which can be many times what you posted. Each day, the exchange credits or debits your account based on the day's price move. If your balance falls too low, you get a call demanding more money. Miss it and you get liquidated. In a violent move, the price can run past your collateral, leaving you with negative equity.

## Key mechanics and formulas
- **Leverage = Notional / Initial margin.** $6,000 margin on an $80,000 WTI contract = 13.3x leverage.
- **Margin call trigger:** Balance < Maintenance margin
- **Call amount = Initial − Current balance**
- **Typical initial margins:** WTI ~$7,000 (8 to 9% of notional), Gold ~$11,000 (4 to 5%), Corn ~$1,500 (6 to 7%), E mini S&P ~$12,000 (4 to 5%)
- **SPAN:** CME's Standard Portfolio Analysis of Risk estimates margin across a range of price scenarios, vol shifts, and time decay. Spread positions receive margin credits for offsetting risk.
- **Intraday calls:** During extreme vol, exchanges can issue intraday calls requiring immediate funding, compressing deleveraging decisions.

## Prerequisites
- [[Futures Contract]]

## Related concepts (learn next)
- [[Futures Contract]] is the instrument margin serves as the core risk mechanism for.
- [[Spread Trade]] positions get reduced margin because the exchange recognizes offsetting risk.
- [[Implied Volatility]] increases lead exchanges to raise margin, creating a feedback loop.
- [[Delivery]] approaching expiry often triggers higher margin to ensure only qualified participants hold positions.
- [[Basis Risk]] means margin on a hedge does not guarantee full protection of the underlying exposure.
- [[Option]] sellers post margin (open ended risk); buyers pay premium upfront and face no margin calls.
- [[Contango Roll Cost]] and [[Backwardation Roll Gain]] do not directly affect margin, but the roll briefly doubles margin when both positions are open.

## Common misconceptions
- **"Margin is like a down payment."** Margin is performance collateral, not a partial purchase. The trader owes the full P&L, which can far exceed margin posted.
- **"You can only lose what you put up."** In extreme cases (overnight gaps, limit moves, illiquid markets), losses exceed total margin, leaving the trader owing the broker.
- **"Margin calls only happen to retail."** The 2022 European energy crisis forced major utilities (Uniper, EDF) and trading houses to post billions in additional collateral within days, threatening corporate solvency.
- **"Higher margin means the exchange expects a crash."** Margin reflects expected vol in both directions, not a directional view. Exchanges raise margin to protect clearinghouse integrity, not to signal direction.

## Sources
- CME Group, "Understanding Margin in Futures Trading"
- CME SPAN: Standard Portfolio Analysis of Risk methodology
- John Hull, "Options, Futures, and Other Derivatives"
- Pirrong, C., "The Economics of Central Counterparty Clearing"
