---
aliases: [matching engine, trade matching, order matching, match engine]
tags:
  - "#microstructure"
  - "#infrastructure"
date-added: "2026-03-27"
---

# Matching Engine

## Definition
A matching engine is the software at an exchange that receives orders and pairs them with compatible resting orders, most commonly by price time priority. When a buy price meets or exceeds a sell price, the engine executes the trade. Modern engines process orders in microseconds, and exchanges invest heavily to reduce latency. The engine enforces all order types ([[IOC]], [[FOK]], [[limit order]], [[stop order]]) and manages the [[Central Limit Order Book]]. Every electronic venue from [[CME]] Globex to [[LME]]select to ICE depends on a matching engine as core infrastructure.

## Why it matters (commodities and FX)
The matching engine decides who fills and at what price. On CME Globex, the difference between getting filled and missing comes down to microseconds in the queue. Understanding engine behavior is essential for algos that earn the [[bid-ask spread]] by posting passive. In FX, matching engines on [[EBS]] and [[Reuters Matching]] set reference prices that propagate to every [[Multi Dealer Platform]] and [[Single Dealer Platform]]. Engine speed, fairness mechanisms (randomized batching, speed bumps), and priority rules directly drive [[execution]] quality and strategy profitability.

## Concrete example

**Concrete:** At 14:30:00.000 UTC on CME Globex, Brent has 2 resting sells at $83.10: 50 lots in queue from 14:29:58.100, 30 lots from 14:29:59.200. A market buy for 60 lots hits. Under price time priority, the engine fills 50 lots against the first seller at $83.10, then 10 lots against the second. The second retains 20 lots resting. Adversarial case: a co located HFT consistently reaches the engine 50 microseconds faster than a traditional trader. When both submit at the same price, the HFT wins. Over thousands of trades, the latency edge compounds into real PnL. That is why exchanges have introduced batch auctions and speed bumps to neutralize raw speed.

**Simplified:** The engine is the referee. Orders queue up by price, then by who arrived first. When a buy and sell meet, trade happens. Everything else (latency racing, queue position, pro rata rules) is detail layered on top of that core matching logic.

## Key mechanics and formulas
- **Price time priority (FIFO):** most common. Best price wins; ties broken by time. CME, ICE, most FX ECNs.
- **Pro rata matching:** some CME products (Eurodollar, Treasury futures). Same price orders fill proportional to size. Fill proportion = order size / total resting at that price.
- **Latency:** time from submission to acknowledgement. Modern engines: 1 to 10 microseconds. Co location reduces network latency below 100 microseconds.
- **Throughput:** orders processed per second. CME Globex handles millions of messages per second.
- **Determinism:** the engine produces the same output given the same input sequence. Critical for audit and compliance.

## Prerequisites
- [[Central Limit Order Book]]
- [[Limit Order]]
- [[Bid-Ask Spread]]
- [[Price Discovery]]

## Related concepts (learn next)
- [[Central Limit Order Book]]: the data structure the engine operates on
- [[IOC]]: order type processed by attempting immediate fill, cancelling remainder
- [[FOK]]: fill everything or cancel everything
- [[Co-location]]: trading servers physically near the engine to minimize network latency
- [[Latency Arbitrage]]: strategy exploiting speed advantages
- [[Price Discovery]]: engine output (trades, book changes) is the primary source
- [[Fair Queuing]]: batch auctions or speed bumps to reduce pure speed advantage

## Common misconceptions
1. **"All engines work the same."** FIFO and pro rata are fundamentally different. On pro rata, time matters less and posting size matters more. Strategy design must match the venue.
2. **"Faster is always better."** Many exchanges added fairness mechanisms. CME batching, EBS randomized hold times, IEX speed bump all reduce raw speed value. Account for venue specific fairness.
3. **"The engine only matters for HFT."** Even a manual trader benefits. Knowing your limit has 500 lots ahead in the queue (low fill probability) changes whether to post passive or cross.

## Sources
- CME Group, "CME Globex: Matching Algorithms" technical reference
- Harris, Larry, "Trading and Exchanges: Market Microstructure for Practitioners" (2003), Chapter 5
- Hasbrouck, Joel, "Empirical Market Microstructure" (2007)
- ICE, "Trading Platform Technical Specifications"
