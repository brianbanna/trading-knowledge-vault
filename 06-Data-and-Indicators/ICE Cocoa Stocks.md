---
aliases: [ICE cocoa stocks, ICE certified cocoa, cocoa warehouse stocks, exchange cocoa inventory, cocoa certified stocks, deliverable cocoa stocks]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# ICE Cocoa Stocks

## Definition

ICE cocoa stocks are quantities of cocoa beans held in ICE (Intercontinental Exchange) approved warehouses, graded and certified as deliverable against the cocoa futures contract. They are the visible, immediately available cocoa backing the futures market. A short held to expiry delivers certified stock from these warehouses. ICE reports daily for both ICE US (New York) and ICE Europe (London). Data includes total certified stock, pending grading (submitted but not yet certified), and pending delivery (allocated against expiring contracts).

## Why it matters (commodities and FX)

Certified stocks are the tightest measure of immediately available cocoa. [[ICCO]] tracks global balance, [[West African Port Arrivals]] tracks harvest pace, but ICE stocks tell you what sits in a warehouse graded and ready to deliver now. The front month converges to physical at expiry. When certified stocks are low, the cost of buying physical for delivery is high, supporting front month prices and [[Backwardation]]. When stocks are abundant, carry costs (storage, insurance, financing) push the curve into [[Contango]].

During the 2024 to 2025 cocoa crisis, ICE US certified stocks fell below 1.5 million bags (~90,000 tonnes) from over 5 million bags (300,000 tonnes) a few years earlier. The collapse in deliverable supply was the mechanical driver behind front month prices above $10,000/tonne and backwardation of $2,000+/tonne between front and deferred.

## Concrete example

**Concrete:** ICE US certified stocks are at 2.0 million bags (~120,000 tonnes). Over 8 weeks stocks fell by 400,000 bags as physical absorbed warehouse inventory. Pending grading is only 50,000 bags (minimal new supply entering). May contract expires in 3 weeks. Trader buys May/July spread (long May, short July) at $150 premium expecting tightness to widen the spread. Stocks continue to 1.7 million bags by expiry. May premium widens to $350. Profit: $200/tonne × 10 tonnes × 10 spreads = $20,000.

**Simplified:** A short who holds futures into expiry must deliver real beans from an ICE approved warehouse. If those warehouses are nearly empty, shorts pay a premium to acquire physical or close out, which pushes the near contract above later contracts. Watching warehouse stock trajectory in the weeks before expiry tells you which way that pressure runs. Falling stocks plus a near expiry plus low pending grading is the classic setup for a backwardation widener.

## Key mechanics and formulas

### Data Publication

| Data Point | Frequency | Source |
|-----------|-----------|--------|
| Certified stock (US) | Daily | ICE US exchange report |
| Certified stock (Europe) | Daily | ICE Europe exchange report |
| Pending grading | Daily | Exchange report |
| Pending delivery | Near expiry | Exchange delivery notices |
| Port stocks (non certified) | Irregular | Industry estimates, customs data |

### Cocoa Stock Units

ICE US reports in bags. 1 bag = 60 kg. 1 lot = 10 metric tonnes ≈ 167 bags.

**Conversions:**
- 1 million bags ≈ 60,000 tonnes
- 200,000 lots OI = 2,000,000 tonnes notional
- Stocks/OI = Certified stock (tonnes) / Total OI (tonnes) × 100%

### What to Watch

**Absolute level:** Below 2 million bags (120,000 tonnes) ICE US = tight. Above 4 million bags (240,000 tonnes) = comfortable. 10 year average ~3 to 4 million bags.

**Rate of change:** More important than level. Falling at 50,000+ bags/week is strongly bullish. Rising at similar rates signals oversupply.

**Pending grading:** Surge means new beans arriving for certification. Leading indicator that stocks will rise. Low pending grading means an empty pipeline and continued drawdowns.

**Delivery notices:** Near expiry, watch first notice day (FND) volumes. Heavy notices = longs want physical (bullish). Few notices = longs rolling rather than taking delivery.

**ICE US vs ICE Europe:** Compare exchanges. Tight US stocks vs comfortable London stocks widens the [[Cocoa NY-London Spread]].

### Stocks and Curve Shape

| Stock Level | Curve Shape | Implication |
|-------------|-------------|-------------|
| Very low (<1.5M bags) | Steep [[Backwardation]] | Physical scramble, [[Convenience Yield]] dominates |
| Low (1.5 to 2.5M) | Mild backwardation | Tight but manageable |
| Normal (2.5 to 4M) | Flat to mild [[Contango]] | Carry costs dominate |
| High (>4M) | Contango | Storage costs push deferred above spot |

## Prerequisites

- [[Cocoa Futures]]
- [[Forward Curve]]
- [[Backwardation]]
- [[Contango]]

## Related concepts (learn next)

- [[West African Port Arrivals]] because port arrivals feed exchange stocks with a weeks to months lag (shipping, grading, certification).
- [[ICCO]] because ICCO stocks include off exchange inventory, the broader picture beyond certified.
- [[Convenience Yield]] because low certified stocks directly raise the premium for holding physical vs futures.
- [[Cocoa NY-London Spread]] because relative stock levels drive the inter exchange spread.
- [[LME Warehouse Stocks]] because the mechanism is identical for base metals.
- [[COT Positioning]] because commercial activity often corresponds to changes in certified stock as producers deliver and consumers take delivery.

## Common misconceptions

**"ICE stocks are total global cocoa inventory."** Certified stocks are a fraction. Beans in transit, origin warehouses, non certified destinations, and factory pipelines are not included. Total global stocks can be 3 to 5x certified.

**"Rising stocks are always bearish."** New certifications can reflect strategic builds by producers ahead of favorable futures delivery, or a quality downgrade (beans failing direct sale standards). Context matters.

**"Certified stocks tell you about demand."** Stocks reflect the balance between deliverable supply and delivery demand. To separate, you need [[West African Port Arrivals]] and [[ICCO]] grindings.

**"Exchange stocks are high quality."** ICE meets minimum spec (bean count, moisture, defects). The best beans go to premium chocolate makers via direct contracts. Exchange stocks are the residual.

## Sources

- ICE Futures US: Daily Certified Stock Report (Cocoa)
- ICE Futures Europe: Daily Certified Stock Report (Cocoa)
- Bloomberg: ICE cocoa warehouse stock data
- Reuters: Exchange stock commentary and analysis
