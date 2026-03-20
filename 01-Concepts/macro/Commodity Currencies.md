---
aliases: [commodity currencies, commodity FX, petrocurrencies, resource currencies, CAD oil, AUD metals]
tags:
  - "#fx/g10"
  - "#fx/em"
  - "#macro"
date-added: "2026-03-20"
---

# Commodity Currencies

## Definition

Commodity currencies are the exchange rates of countries whose economies and export revenues are dominated by commodity production. The currency value is structurally linked to commodity prices because higher commodity prices improve the country's terms of trade, current account, fiscal balance, and economic growth. The primary G10 commodity currencies are CAD (oil, lumber), AUD (iron ore, coal, copper, LNG), NOK (oil, gas), and NZD (dairy, agriculture). Key EM commodity currencies include BRL (soybeans, coffee, sugar, iron ore), ZAR (gold, platinum, coal), CLP (copper), RUB (oil, gas), MXN (oil), and COP (oil, coffee).

## Why it matters (commodities and FX)

Commodity currencies are the bridge between commodity markets and FX markets. They allow a commodity trader to express a commodity view through FX, and they allow an FX trader to understand why certain currencies move. If you are long [[Brent Crude]] and also long CAD or NOK, you have concentrated commodity exposure. If you are long crude and short AUD/CAD, you are expressing a relative commodity view (energy vs metals/China). Understanding these linkages is essential for portfolio construction, [[Hedging]], and identifying hidden [[Correlation]] exposures.

The relationship also runs in reverse: a strong USD (driven by Fed policy, [[Real Interest Rates]]) weighs on ALL commodity currencies and commodity prices simultaneously, because most commodities are priced in USD.

## Concrete example

**AUD/USD and iron ore:** Australia is the world's largest iron ore exporter. Iron ore is Australia's largest export (~35% of goods exports). When Chinese steel production booms and iron ore prices rise from $80/tonne to $130/tonne, Australian terms of trade improve, export revenue grows, and the RBA may face inflationary pressure. AUD/USD typically rises in tandem. The rolling 12 month [[Correlation]] between AUD/USD and iron ore prices has averaged 0.60 to 0.75 over the past decade.

Trade expression: if you believe Chinese construction will slow and iron ore will fall from $120 to $90, you can express this view by shorting AUD/USD rather than directly shorting iron ore futures. Advantages: AUD/USD is extremely liquid (top 5 global FX pair), 24 hour market, no expiry or roll. Disadvantage: AUD/USD also reflects interest rate differentials, risk sentiment, and other factors, so it is a noisy proxy.

**USD/CAD and WTI:** Canada is the 4th largest oil producer. Oil and gas represent ~20% of exports. When WTI rises, CAD strengthens (USD/CAD falls). The correlation is approximately 0.50 to 0.65. A common trade: long WTI / long USD/CAD as a hedge (offsetting the commodity exposure with currency exposure). Or: long NOK/CAD as a pure Brent vs WTI expression through FX.

## Key mechanics and formulas

**Terms of trade effect:**
`Terms of Trade = Export Prices / Import Prices`

When commodity prices rise, a commodity exporter's terms of trade improve, attracting capital inflows and strengthening the currency.

**Key commodity/currency linkages:**

| Currency | Primary Commodity | Correlation (approx) |
|----------|------------------|---------------------|
| AUD | Iron ore, copper | 0.60 to 0.75 |
| CAD | WTI crude oil | 0.50 to 0.65 |
| NOK | Brent crude oil | 0.55 to 0.70 |
| NZD | Dairy (GDT auction) | 0.40 to 0.55 |
| BRL | Soybeans, iron ore | 0.30 to 0.50 |
| ZAR | Gold, platinum | 0.30 to 0.50 |
| CLP | Copper | 0.50 to 0.65 |

**Commodity beta of FX:**
`ΔFX ≈ α + β x ΔCommodity + ε`

The beta tells you how many basis points the currency moves per 1% change in the commodity. AUD/USD beta to iron ore is approximately 0.3 to 0.4 (a 10% iron ore rally = 3 to 4% AUD appreciation).

## Prerequisites
- [[Carry Trade]]
- [[Correlation]]
- [[Brent Crude]]
- [[Gold Futures]]

## Related concepts (learn next)
- [[Brent-WTI Spread]] - different crude benchmarks link to different currencies. Brent drives NOK, WTI drives CAD. Trading NOK/CAD is an FX expression of the Brent/WTI spread.
- [[Risk-On Risk-Off]] - commodity currencies are pro cyclical. They strengthen in risk on and weaken in risk off, amplifying commodity exposure.
- [[Real Interest Rates]] - commodity currencies are sensitive to both commodity prices AND real rate differentials. Decomposing what is driving the currency is essential.
- [[Safe Haven Assets]] - commodity currencies are the opposite of safe havens. In a crisis, AUD and CAD weaken while JPY and CHF strengthen.
- [[Carry Trade]] - many commodity currencies offer high nominal yields (BRL, ZAR, MXN), making them carry trade destinations. This creates a dual driver: carry + commodity.
- [[Inter-Commodity Spread]] - cross commodity views can be expressed through FX pairs (AUD/CAD = metals vs oil).

## Common misconceptions

**"AUD is a China proxy."** Partially true (China buys ~60% of Australian iron ore), but AUD also reflects domestic rates, global risk sentiment, and other exports. AUD weakened in 2022 despite strong iron ore prices because the Fed hiked faster than the RBA.

**"Commodity currencies perfectly track commodity prices."** The correlation is strong but not 1:1. Central bank policy, fiscal dynamics, political risk, and positioning all create divergences. Use the commodity linkage as a guide, not a rule.

**"EM commodity currencies behave like G10 commodity currencies."** EM currencies carry additional risks: capital controls, convertibility risk, political instability, and balance of payments crises. BRL can collapse 20% even if soybeans are rallying, if fiscal concerns trigger capital flight.

## Sources

- Chen and Rogoff, "Commodity Currencies" (Journal of International Economics, 2003)
- BIS Quarterly Review: commodity currencies and terms of trade analysis
- RBA (Reserve Bank of Australia): research papers on AUD and commodity prices
- Bank of Canada: "The Canadian Dollar and Oil Prices" research notes
