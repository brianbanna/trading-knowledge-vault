---
aliases: [two way price, two-way quote, bid-offer quote, two-sided market]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Two Way Price

## Definition
A two way price is a simultaneous bid and ask shown together. Saying "I am showing 1.1499 at 1.1501" means I will buy at 1.1499 and sell at 1.1501. The left number is the bid (lower), the right is the offer (higher). Two way pricing is the foundation of market making: continuously showing both sides provides [[Liquidity]] and earns the [[Bid-Ask Spread]] when both sides fill. In voice markets, a trader asks "Where is cable?" and the maker responds with a two way price, forcing the requester to declare direction.

## Why it matters (commodities and FX)
In FX interdealer markets, showing a two way price proves the dealer is making markets, not cherry picking direction. On voice commodity desks, when a broker says "Gold is 2340 at 2341," both sides are live and the client must choose. The convention prevents the client from seeing the dealer's bias. Two way pricing is the standard on [[ECN|ECNs]] like EBS and Refinitiv Matching, where resting orders form a two way book. Essential for reading any order book, calculating [[Mid Price]], and evaluating [[Bid-Ask Spread|spread]] tightness.

## Concrete example

**Concrete:** Copper broker on LME shows two way for 3 month copper: $8,420 at $8,425. Spread $5/ton. Win: market maker. Producer sells 100 tons at $8,420 bid. 2 minutes later, fabricator buys 100 tons at $8,425 offer. Earned $5/ton x 100 = $500. Both sides hit, [[Mid Price]] ($8,422.50) did not move. Textbook market making profit. Failure: $8,420 at $8,425. Trading house lifts $8,425 offer for 500 tons right before LME warehouse data shows a large drawdown. Copper jumps to $8,480. Now short 500 tons at $8,425, market is $55 against me. Loss 500 x $55 = $27,500. The two way price gave the informed trader a cheap option. The ask was effectively a [[Stale Quote]] relative to the warehouse data the counterparty had seen.

**Simplified:** A two way price shows both buy and sell at once. The dealer cannot pick direction; the client picks. If both sides eventually trade, the dealer earns the spread. If only one side trades and the market then moves, the dealer is stuck on that side and loses money.

## Key mechanics and formulas
- **Two way price** = Bid / Offer (Bid < Offer)
- **Spread** = Offer - Bid
- **Mid** = (Bid + Offer) / 2
- **FX convention:** "1.1499 / 1.1501" or "99 / 01" in shorthand (big figure 1.14 implied)
- **Commodity convention:** "$8,420 at $8,425" or "420 at 425" when thousands are obvious
- **Maker obligation:** many exchanges require designated makers to show two way prices within a max spread for a min percentage of the trading day

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Quote]]

## Related concepts (learn next)
- [[Half Spread]] , cost of transacting on one side
- [[Round Trip]] , buying at the offer and selling at the bid, paying full spread
- [[Top of Book]] , the best two way price in the book
- [[Depth of Book]] , all two way prices at various levels, not just the best
- [[Last Look]] , FX mechanism letting the quoter reject fills
- [[Firm Quote]] , a binding two way price once shown
- [[Client Tiering]] , adjusting two way prices per client based on flow quality

## Common misconceptions
1. **"The two way price is always symmetric around fair value."** Makers skew quotes. Long inventory: shift the two way lower to attract sellers and discourage buyers. The mid of the two way is not fair value; it is fair value adjusted for [[Skew Microstructure|inventory skew]].
2. **"Both sides carry equal risk."** In a trending market, one side gets hit repeatedly while the other sits. During a crude selloff, the bid gets hammered while the offer is idle. Risk is asymmetric even though the price looks symmetric.
3. **"A tighter two way is always better for the client."** A tight two way with [[Last Look]] rejection can be worse than a wider firm price. The client sees the tight quote but gets rejected on favorable fills, so effective spread is wider than it looks.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- King, M., Osler, C., Rime, D. "Foreign Exchange Market Structure, Players, and Evolution," *Handbook of Exchange Rates*
- LME, "Trading and Pricing Guide"
