---
aliases: [coffee, KC, Arabica coffee, ICE coffee, Robusta]
tags:
  - "#agri/softs/coffee"
date-added: "2026-03-20"
---

# Coffee Futures

## Definition

Coffee futures trade in 2 primary contracts: Arabica (ICE US, KC, USD cents/lb) and Robusta (ICE Europe, RC, USD/tonne). Arabica is higher quality, higher priced, used in specialty and premium blends. Robusta is cheaper, higher caffeine, used in instant coffee and as a blending component. Brazil dominates Arabica, Vietnam dominates Robusta.

## Why it matters (commodities and FX)

Coffee is the 2nd most traded commodity by volume after crude oil on some measures. It has extreme weather sensitivity (a single frost in Brazil can move prices 20%+ in a session), making it a prime example of [[Convenience Yield]] dynamics and supply shock trading. The Arabica/Robusta spread is one of the most actively traded [[Relative Value Trade|relative value trades]] in softs. Coffee is also a natural laboratory for how [[Seasonality]], weather risk, and inventory cycles interact.

## Concrete example

**Concrete:** Mid July, SOMAR Meteorologia issues a frost alert for southern Minas Gerais with temperatures forecast at minus 2C across key Arabica zones. KC front month (KCN6) was 205 cents/lb Friday. Trader buys 4 KC contracts at 208 cents on Monday open. Satellite imagery overnight confirms frost damage on roughly 8% of trees. Spot prints 242 cents by Wednesday as roasters scramble for physical and ICE certified stocks draw 12,000 bags. Trader exits at 238 cents. P&L: (238 minus 208) cents × 37,500 lbs × 4 = $45,000 (each cent is $375 per contract). Front month [[Backwardation]] to deferred deepened by 8 cents.

**Simplified:** Coffee Arabica is the price of 1 pound of green coffee beans. Brazil produces about 35% of global supply, so Brazilian weather between June and August (their winter frost window) drives most of the action. A single hard frost can move the price 20% in a day. Traders watch Brazil temperature forecasts, ICE warehouse stocks, and the Brazilian Real. Each contract is 37,500 lbs, so 1 cent per lb equals $375 per contract.

## Contract specifications

| Field | Value |
|-------|-------|
| Exchange | ICE US |
| Ticker | KC (Arabica) |
| Contract size | 37,500 lbs (~250 bags of 60 kg) |
| Tick size | $0.0005/lb |
| Tick value | $18.75 |
| Trading hours | 04:15 to 13:30 ET |
| Settlement | Physical delivery |
| Expiry months | Mar, May, Jul, Sep, Dec |
| Currency | USD |

## Fundamentals

### Supply drivers
- Brazil: ~35 to 40% of global production. Biennial cycle (on year / off year alternation)
- Vietnam: ~18% of production, nearly all Robusta
- Colombia, Honduras, Ethiopia, Uganda: secondary producers
- Frost and drought in Brazil (Jun to Aug): the single biggest price risk factor
- Berry borer beetle and coffee leaf rust: ongoing supply threats
- Brazilian Real (BRL): weaker BRL incentivizes Brazilian farmer selling

### Demand drivers
- Global consumption ~170 million bags/year, growing 2 to 3% annually
- EU is the largest consuming region, then US, Japan, Brazil
- Specialty coffee growth driving Arabica premium
- Short term price elasticity is low (people need their coffee)

### Seasonality
Brazilian Arabica harvest runs Apr to Sep (main). Vietnamese Robusta harvest runs Oct to Mar. Brazil frost window is Jun to Aug (Brazilian winter). Prices build a weather premium into Jun/Jul and release it once the frost window passes without incident.

## Key data and reports

- USDA biannual coffee report: global supply/demand estimates
- ICO (International Coffee Organization): monthly export data
- GCA (Green Coffee Association): US warehouse stocks, monthly
- ICE certified stocks: deliverable inventory
- Brazilian crop agency (CONAB): annual production estimates
- CFTC COT report: managed money positioning in KC
- Brazil weather forecasts: SOMAR Meteorologia

## Curve structure

Arabica shifts between [[Contango]] and [[Backwardation]] depending on certified stocks and harvest expectations. During Brazilian frost scares, the curve inverts violently into backwardation as physical buyers scramble. Between harvests, mild contango is typical if inventories are adequate.

## Key spreads and relative value

- **[[Arabica-Robusta Spread|Arabica/Robusta spread]]:** the core relative value trade in coffee. Widens when Arabica supply tightens or specialty demand grows. Narrows when roasters substitute Robusta into blends due to high Arabica prices.
- **Coffee calendar spreads:** front vs deferred, particularly around Brazilian frost season.
- **Coffee/Cocoa ratio:** both tropical softs, correlated supply risks, different geographic concentration.
- **Coffee/Sugar ratio:** Brazilian farmers can switch land between coffee and sugarcane, creating long run supply substitution.

## Important relationships

- Strong inverse correlation with BRL (weaker Real = more Brazilian selling = lower USD price, all else equal)
- Weather correlation: frost and drought in Minas Gerais (Brazil's largest coffee state) dominate price action
- Positive correlation with [[Cocoa Futures|cocoa]] and [[Sugar Futures|sugar]] during broad soft commodity moves
- ICE certified stocks inversely correlated with price (low stocks = high convenience yield = backwardation)

## Trading notes

*Add personal observations here.*

## Related instruments

- [[Cocoa Futures]]
- [[Sugar Futures]]
- [[Cotton Futures]]
- [[BRL/USD]]

## Related concepts

- [[Backwardation]]
- [[Convenience Yield]]
- [[Seasonality]]
- [[Forward Curve]]
- [[Relative Value Trade]]
- [[Weather Risk]]
