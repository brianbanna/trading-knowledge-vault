---
aliases: [ICE cocoa stocks, ICE certified cocoa, cocoa warehouse stocks, exchange cocoa inventory, cocoa certified stocks, deliverable cocoa stocks]
tags:
  - "#agri/softs/cocoa"
date-added: "2026-03-24"
---

# ICE Cocoa Stocks

## Definition

ICE cocoa stocks are the quantities of cocoa beans held in ICE (Intercontinental Exchange) approved warehouses that have been graded and certified as deliverable against the cocoa futures contract. Think of it as the visible, immediately available cocoa that backs up the futures market. When someone holds a short futures position to expiry and must deliver, they deliver certified stock from these warehouses. ICE reports certified stock levels daily for both ICE US (New York) and ICE Europe (London) cocoa contracts. The data includes total certified stock, pending grading (beans submitted but not yet certified), and pending delivery (beans allocated against expiring contracts).

## Why it matters (commodities and FX)

Certified stocks are the tightest measure of immediately available cocoa supply. While [[ICCO]] data tells you about the global balance and [[West African Port Arrivals]] tell you about the harvest pace, ICE stocks tell you what is actually sitting in a warehouse, graded and ready to deliver right now. This matters because the front month futures price converges to the physical market at expiry. When certified stocks are low, the cost of buying physical cocoa for delivery is high, supporting front month prices and [[Backwardation]]. When stocks are abundant, the cost of carry (storage, insurance, financing) pushes the curve into [[Contango]].

During the 2024 to 2025 cocoa crisis, ICE US certified stocks fell below 1.5 million bags (approximately 90,000 tonnes) from over 5 million bags (300,000 tonnes) a few years earlier. This collapse in deliverable supply was the mechanical driver behind front month prices exceeding $10,000/tonne and backwardation reaching $2,000+/tonne between front and deferred months.

## Concrete example

ICE US certified cocoa stocks stand at 2.0 million bags (approximately 120,000 tonnes). Over the past 8 weeks, stocks have declined by 400,000 bags as physical demand has absorbed warehouse inventory. Pending grading is only 50,000 bags (minimal new supply entering the system). The May contract expires in 3 weeks.

A trader recognizes that the declining stock trajectory means deliverable supply will be tight at May expiry. They buy the May/July spread (long May, short July), expecting May to strengthen relative to July as physical tightness intensifies into expiry. May is already at a $150 premium to July. As stocks continue drawing down to 1.7 million bags by expiry, the May premium widens to $350. Profit: $200/tonne x 10 tonnes = $2,000 per spread.

If instead new certified stock had been graded and stocks rebounded to 2.5 million bags, the May premium would have compressed and the spread trade would have lost.

## Key mechanics and formulas

### Data Publication

| Data Point | Frequency | Source |
|-----------|-----------|--------|
| Certified stock (US) | Daily | ICE US exchange report |
| Certified stock (Europe) | Daily | ICE Europe exchange report |
| Pending grading | Daily | Included in exchange report |
| Pending delivery | Near contract expiry | Exchange delivery notices |
| Port stocks (non certified) | Irregular | Industry estimates, customs data |

### Cocoa Stock Units

ICE US reports in bags. 1 bag = 60 kg. 1 lot = 10 metric tonnes = approximately 167 bags.

**Conversions:**
- 1 million bags = approximately 60,000 tonnes
- Open interest of 200,000 lots = 2,000,000 tonnes of notional cocoa
- Stocks to open interest ratio = Certified stock (tonnes) / Total open interest (tonnes) x 100%

### What to Watch

**Absolute level:** Below 2 million bags (120,000 tonnes) on ICE US = tight. Above 4 million bags (240,000 tonnes) = comfortable. The 10 year average is approximately 3 to 4 million bags.

**Rate of change:** More important than the level. Falling stocks at 50,000+ bags/week is a strong bullish signal. Rising stocks at similar rates signals physical oversupply.

**Pending grading:** A surge in pending grading means new beans are arriving at warehouses for certification. This is a leading indicator that stocks will increase. Low pending grading means the pipeline is empty and stocks will continue declining.

**Delivery notices:** Near contract expiry, watch first notice day (FND) delivery volumes. If a large number of delivery notices are issued, it signals that longs want physical cocoa (bullish for tightness). If few notices are issued, longs are rolling rather than taking delivery.

**ICE US vs ICE Europe stocks:** Compare the 2 exchanges. If US stocks are tight but London stocks are comfortable, the [[Cocoa NY-London Spread]] will widen as NY commands a premium for scarce deliverable supply.

### Stocks and Curve Shape

| Stock Level | Curve Shape | Implication |
|-------------|-------------|-------------|
| Very low (below 1.5M bags) | Steep [[Backwardation]] | Physical scramble, [[Convenience Yield]] dominates |
| Low (1.5 to 2.5M bags) | Mild backwardation | Tight but manageable |
| Normal (2.5 to 4M bags) | Flat to mild [[Contango]] | Carry costs dominate |
| High (above 4M bags) | Contango | Storage costs push deferred above spot |

## Prerequisites

- [[Cocoa Futures]]
- [[Forward Curve]]
- [[Backwardation]]
- [[Contango]]

## Related concepts (learn next)

- [[West African Port Arrivals]] because port arrivals feed into exchange stocks with a lag of weeks to months (shipping, grading, certification).
- [[ICCO]] because ICCO stock estimates include off exchange stocks, providing the full picture beyond just certified inventory.
- [[Convenience Yield]] because low certified stocks directly translate to high convenience yield, the premium for holding physical cocoa vs futures.
- [[Cocoa NY-London Spread]] because relative stock levels between ICE US and ICE Europe drive the inter exchange spread.
- [[LME Warehouse Stocks]] because the concept is identical for base metals. Comparing the 2 systems helps understand exchange stock mechanics more broadly.
- [[COT Positioning]] because commercial (hedger) activity in the COT report often corresponds to changes in certified stock levels, as producers deliver and consumers take delivery.

## Common misconceptions

**"ICE stocks are total global cocoa inventory."** Certified stocks are a fraction of global inventory. Beans in transit, in origin country warehouses, in non certified destination warehouses, and in chocolate factory pipelines are not included. Total global stocks could be 3 to 5x the ICE certified figure.

**"Rising stocks are always bearish."** New certifications could reflect strategic stock builds by producers who plan to deliver against futures at favorable prices. It could also reflect a quality downgrade (beans that failed to meet direct sale standards being certified for exchange delivery as a last resort). Context matters.

**"Certified stock levels tell you about demand."** Stocks tell you about the balance between deliverable supply and delivery demand. High stocks could mean weak demand or strong supply. Low stocks could mean strong demand or blocked supply. You need [[West African Port Arrivals]] and [[ICCO]] grindings data to distinguish.

**"Exchange stocks are always high quality."** ICE delivery standards specify minimum requirements (bean count, moisture, defects), but exchange deliverable cocoa is generally considered lower quality than directly traded physical cocoa. The best beans go to premium chocolate makers via direct contracts. Exchange stocks are the "residual" supply.

## Sources

- ICE Futures US: Daily Certified Stock Report (Cocoa)
- ICE Futures Europe: Daily Certified Stock Report (Cocoa)
- Bloomberg: ICE cocoa warehouse stock data
- Reuters: Exchange stock commentary and analysis
