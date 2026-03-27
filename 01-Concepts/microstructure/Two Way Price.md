---
aliases: [two way price, two-way quote, bid-offer quote, two-sided market]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Two Way Price

## Definition
A two way price is a simultaneous bid and ask shown together. When I say "I am showing 1.1499 at 1.1501," I mean I will buy at 1.1499 and sell at 1.1501. The left number is always the bid (lower), and the right is the offer (higher). Two way pricing is the foundation of market making: by continuously showing both sides, I provide [[Liquidity]] and earn the [[Bid-Ask Spread]] when both sides get filled. In voice markets, a trader may ask "Where is cable?" and the market maker responds with a two way price, forcing the requester to declare direction.

## Why it matters (commodities and FX)
In FX interdealer markets, showing a two way price is how dealers prove they are making markets, not just cherry picking direction. On voice commodity desks, when a broker says "Gold is 2340 at 2341," both sides are live and the client must choose. This convention prevents the client from seeing the dealer's bias. Two way pricing is also the standard on [[ECN|ECNs]] like EBS and Refinitiv Matching, where resting orders form a two way book. Understanding two way prices is essential for reading any order book, calculating [[Mid Price]], and evaluating [[Bid-Ask Spread|spread]] tightness.

## Concrete example
A copper broker on the LME shows a two way price for 3 month copper: $8,420 at $8,425. The spread is $5 per metric ton.

**Win scenario:** I am the market maker. A producer sells 100 tons at my $8,420 bid. 2 minutes later, a fabricator buys 100 tons at my $8,425 offer. I earned $5 per ton x 100 tons = $500. Both sides of my two way price were hit, and the [[Mid Price]] ($8,422.50) did not move. This is the textbook market making profit.

**Fail scenario:** I show $8,420 at $8,425. A trading house lifts my $8,425 offer for 500 tons right before LME warehouse data shows a large drawdown. Copper jumps to $8,480. I am short 500 tons at $8,425 and the market is now $55 against me. Loss: 500 x $55 = $27,500. My two way price gave the informed trader a cheap option to trade against me. The ask side was effectively a [[Stale Quote]] relative to the warehouse data the counterparty had already seen.

## Key mechanics and formulas
- **Two way price** = Bid / Offer (always Bid < Offer)
- **Spread** = Offer minus Bid
- **Mid** = (Bid + Offer) / 2
- **Convention in FX:** "1.1499 / 1.1501" or "99 / 01" in shorthand (the big figure 1.14 is implied)
- **Convention in commodities:** "$8,420 at $8,425" or "420 at 425" when the thousands are obvious
- **Market maker obligation:** Many exchanges require designated market makers to show two way prices within a maximum spread for a minimum percentage of the trading day

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Quote]]

## Related concepts (learn next)
- [[Half Spread]] , the cost of transacting on one side of a two way price
- [[Round Trip]] , buying at the offer and selling at the bid, paying the full spread
- [[Top of Book]] , the best two way price available in the order book
- [[Depth of Book]] , all the two way prices at various levels, not just the best
- [[Last Look]] , an FX mechanism that lets the quoter reject fills on a two way price
- [[Firm Quote]] , a two way price that is binding once shown
- [[Client Tiering]] , adjusting the two way price per client based on flow quality

## Common misconceptions
1. **"The two way price is always symmetric around fair value."** Market makers skew quotes. If I am long inventory, I shift my two way price lower to attract sellers and discourage buyers. The mid of my two way price is not my fair value; it is my fair value adjusted for [[Skew Microstructure|inventory skew]].
2. **"Both sides carry equal risk."** In a trending market, one side of the two way price gets hit repeatedly while the other goes untouched. During a crude oil selloff, my bid gets hammered while my offer sits idle. The risk is asymmetric even though the price looks symmetric.
3. **"A tighter two way price is always better for the client."** A tight two way price with [[Last Look]] rejection may be worse than a wider firm price. The client sees a tight quote but gets rejected on favorable fills, so the effective spread is wider than it appears.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- King, M., Osler, C., Rime, D. "Foreign Exchange Market Structure, Players, and Evolution," *Handbook of Exchange Rates*
- LME, "Trading and Pricing Guide"
