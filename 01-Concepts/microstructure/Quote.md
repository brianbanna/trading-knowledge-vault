---
aliases: [quote, market quote, price quote, quotation]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Quote

## Definition
A quote is a price that I show to the market, indicating my willingness to buy or sell at that level. When I quote, I am publishing a bid (my buying price) and/or an ask (my selling price), usually with an associated size. Quoting is the fundamental act of market making: I advertise prices and wait for counterparties to trade against them. The quality of my quote depends on how accurately it reflects my view of [[Mid Price|fair value]], how tight the [[Bid-Ask Spread|spread]] is, and how quickly I update it when conditions change. In electronic markets, quotes are continuously streamed and can be updated hundreds of times per second.

## Why it matters (commodities and FX)
In FX, quoting is the core business of dealers on [[Single Dealer Platform|single dealer platforms]] like Barclays BARX or Citi Velocity. A dealer streams personalized quotes to each client based on [[Client Tiering|tiering]] and flow toxicity. In commodities, brokers on ICE or CME quote two way prices on futures and options. The ability to quote tight and update fast directly determines profitability. If my quotes are too wide, I lose flow to competitors. If they are too tight without adequate [[Adverse Selection]] protection, I get picked off by informed traders. Quoting is where microstructure theory meets actual P&L.

## Concrete example
I am a EUR/USD market maker on an [[ECN]]. My fair value model says the mid is 1.10010. I decide to quote a 2 pip spread: 1.10000 bid, 1.10020 offer, in 5 million EUR.

**Win scenario:** A corporate hedger sells 5 million EUR at my 1.10000 bid. The mid does not move. 30 seconds later, another client buys 5 million EUR at my 1.10020 offer. I have earned the full spread: 2 pips on 5 million EUR = $1000 profit. My [[Markout]] is flat because the mid did not move against me.

**Fail scenario:** I quote the same 1.10000 / 1.10020. A hedge fund algorithm hits my 1.10000 bid for 5 million just before a weak US payroll number. EUR/USD jumps to 1.1020 within 1 second. My [[Markout]] at 1 second is negative 18 pips. The quote I showed was [[Stale Quote|stale]] relative to the information the hedge fund already had. I lost $9000 on a single fill because the counterparty was [[Toxic Flow|informed]].

## Key mechanics and formulas
- **Quoted spread** = Ask minus Bid
- **Quote mid** = (Bid + Ask) / 2
- **Edge per trade** = [[Half Spread]] minus expected [[Adverse Selection]] cost
- **Quote refresh rate** = how often I update my prices (milliseconds in electronic FX, seconds in voice commodity markets)
- **Fill rate** = trades executed / quotes shown, a measure of how competitive my pricing is
- A quote becomes a [[Stale Quote]] when the market has moved but the quote has not been refreshed

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Two Way Price]] , quoting both bid and ask simultaneously, which is a market maker's obligation
- [[Stale Quote]] , a quote that has not been updated and creates [[Sniping]] risk
- [[Last Look]] , an FX specific mechanism where the quoter can reject a trade after seeing the fill request
- [[Client Tiering]] , adjusting quoted spreads per client based on flow quality
- [[Adverse Selection]] , the risk embedded in every quote that the taker knows more than I do
- [[Internalization]] , matching client flow internally rather than quoting it to the market
- [[Firm Quote]] , a quote that cannot be withdrawn, common in regulated futures markets
- [[Indicative Quote]] , a non binding price shown for information, common in OTC commodities

## Common misconceptions
1. **"A quote is a commitment to trade."** Not always. In OTC FX, many quotes are indicative or subject to [[Last Look]]. The quoter can reject the fill if the market has moved. In exchange traded futures, resting limit orders are firm quotes and are binding.
2. **"Tighter quotes always win more business."** Tighter quotes attract more fills, but they also attract more [[Toxic Flow]]. The optimal spread balances fill rate against adverse selection. Quoting 0.1 pip in EUR/USD will win every flow, including every toxic fill.
3. **"Quoting is passive."** Quoting requires active management. A good market maker adjusts quotes based on inventory, volatility, news, time of day, and client identity. Passive quoting with static spreads is a recipe for losing money.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- CME Group, "Market Making Programs and Obligations"
