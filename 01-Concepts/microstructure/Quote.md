---
aliases: [quote, market quote, price quote, quotation]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Quote

## Definition
A quote is a price I show to the market, indicating willingness to buy or sell at that level. Quoting publishes a bid (buying price) and/or ask (selling price), usually with a size. It is the fundamental act of market making: advertise prices and wait for counterparties to trade. Quality depends on how accurately the quote reflects [[Mid Price|fair value]], how tight the [[Bid-Ask Spread|spread]] is, and how quickly I update when conditions change. In electronic markets, quotes stream continuously and update hundreds of times per second.

## Why it matters (commodities and FX)
In FX, quoting is the core business on [[Single Dealer Platform|SDPs]] like Barclays BARX or Citi Velocity. A dealer streams personalized quotes by [[Client Tiering|tier]] and flow toxicity. In commodities, brokers on ICE or CME quote two way prices on futures and options. Tight quoting and fast updating directly determine profitability. Too wide and I lose flow to competitors. Too tight without [[Adverse Selection]] protection and I get picked off. Quoting is where microstructure theory meets actual P&L.

## Concrete example

**Concrete:** EUR/USD maker on [[ECN]]. Fair value mid 1.10010. Quote a 2 pip spread: 1.10000 / 1.10020 in 5M EUR. Win: corporate hedger sells 5M EUR at 1.10000. Mid does not move. 30s later another client buys 5M at 1.10020. Earned full spread: 2 pips on 5M EUR = $1000. [[Markout]] flat because mid did not move. Failure: same quote 1.10000 / 1.10020. Hedge fund algo hits 1.10000 bid for 5M just before weak US payrolls. EUR/USD jumps to 1.1020 in 1 second. 1s [[Markout]] is -18 pips. The quote was [[Stale Quote|stale]] to the information the fund already had. Lost $9000 on a single fill because the counterparty was [[Toxic Flow|informed]].

**Simplified:** A quote is a public commitment to trade at a price. Show a bid and you will buy from anyone who sells. Show an ask and you will sell to anyone who buys. The art is showing tight prices to attract flow while not being so tight that faster, better informed counterparties pick you off.

## Key mechanics and formulas
- **Quoted spread** = Ask - Bid
- **Quote mid** = (Bid + Ask) / 2
- **Edge per trade** = [[Half Spread]] - expected [[Adverse Selection]] cost
- **Quote refresh rate** = how often prices update (ms in electronic FX, seconds in voice commodities)
- **Fill rate** = trades executed / quotes shown, measures how competitive my pricing is
- A quote becomes a [[Stale Quote]] when the market moved but the quote did not refresh

## Prerequisites
- [[Bid-Ask Spread]]
- [[Mid Price]]
- [[Top of Book]]

## Related concepts (learn next)
- [[Two Way Price]] , showing bid and ask simultaneously, a market maker's obligation
- [[Stale Quote]] , a quote that has not updated, creating [[Sniping]] risk
- [[Last Look]] , FX mechanism where the quoter can reject after seeing the request
- [[Client Tiering]] , adjusting spreads per client based on flow quality
- [[Adverse Selection]] , the risk in every quote that the taker knows more
- [[Internalization]] , matching client flow internally instead of quoting it externally
- [[Firm Quote]] , a quote that cannot be withdrawn, common in regulated futures
- [[Indicative Quote]] , a non binding price shown for information, common in OTC commodities

## Common misconceptions
1. **"A quote is a commitment to trade."** Not always. In OTC FX, many quotes are indicative or subject to [[Last Look]]. The quoter can reject the fill if the market moved. In exchange traded futures, resting limit orders are firm.
2. **"Tighter quotes always win more business."** Tighter quotes attract more fills and more [[Toxic Flow]]. Optimal spread balances fill rate against adverse selection. Quoting 0.1 pip in EUR/USD wins every flow including every toxic fill.
3. **"Quoting is passive."** Quoting needs active management. A good maker adjusts to inventory, volatility, news, time of day, and client identity. Static spreads lose money.

## Sources
- Harris, L. *Trading and Exchanges: Market Microstructure for Practitioners*, Oxford University Press
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- CME Group, "Market Making Programs and Obligations"
