---
aliases: [forward contract, forward, OTC forward]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Forward Contract

## Definition
A forward contract is a private, over the counter (OTC) agreement between 2 parties to buy or sell an asset at a specified price on a future date. Unlike a [[Futures Contract]] (standardized and exchange traded), forwards are fully customizable: the parties can negotiate the exact quantity, quality grade, delivery location, settlement date, and reference price index. Forwards carry bilateral counterparty credit risk because there is no clearinghouse guarantee standing between buyer and seller, though post 2008 regulations have pushed many standardized forwards toward central clearing. They are the workhorse of physical commodity markets where traders need delivery terms that do not match exchange contract specifications. FX forwards are the most actively traded forward instruments globally, with daily turnover exceeding $3 trillion. Settlement typically occurs at maturity (rather than daily mark to market as in futures), although variation margin agreements are increasingly common for credit risk management.

## Why it matters (commodities and FX)
Forwards are essential for physical commodity trading because real world delivery needs almost never align perfectly with standardized futures specifications. A jet fuel buyer in Singapore needs delivery at Changi airport on specific dates in specific quantities, which no exchange contract offers. In FX, forward contracts allow corporations to hedge future foreign currency cash flows at known rates, locking in budget certainty for international operations. The forward price embeds the [[interest rate differential]] (in FX) or the cost of carry including storage and convenience yield (in commodities), making forwards a fundamental building block for understanding pricing theory and arbitrage relationships.

## Concrete example
**Success case:** An airline negotiates a 6 month forward contract with a bank to buy 1 million gallons of jet fuel at $2.50/gallon for delivery in December. Jet fuel rises to $3.00/gallon by December. The airline saves $500,000 versus buying at the spot market price, and has had cost certainty for its route planning and ticket pricing since the forward was booked.

**Failure case:** Using the same forward at $2.50/gallon, jet fuel falls to $2.00/gallon by December. The airline is locked in at $0.50/gallon above market, an opportunity cost of $500,000. Meanwhile, competitors who did not hedge can buy fuel cheaper. Additionally, the bank that sold the forward faces credit risk: if the airline enters financial distress and cannot pay, the bank is exposed. The lesson: forwards lock in both upside and downside, and counterparty risk is real in OTC markets.

## Key mechanics and formulas
- **Forward price (commodities):** F = S x e^((r + c - y) x T), where S = spot price, r = risk free rate, c = storage cost rate, y = convenience yield rate, T = time to maturity
- **Forward price (FX):** F = S x (1 + r_domestic x T) / (1 + r_foreign x T). This reflects [[covered interest parity]].
- **Key differences from [[Futures Contract|futures]]:**
  - Customizable terms vs. standardized
  - OTC vs. exchange traded
  - Counterparty risk vs. clearinghouse guarantee
  - Settled at maturity vs. daily mark to market
  - Less liquid (harder to exit) vs. continuous secondary market
- **Credit risk mitigation:** ISDA master agreements, margin posting (CSA), netting, and post crisis central clearing mandates

## Prerequisites
- [[Futures Contract]]
- [[Margin]]

## Related concepts (learn next)
- [[Futures Contract]] is the standardized, exchange traded version that eliminates counterparty risk through central clearing.
- [[Swap]] can be understood as a series of forward contracts with periodic settlements against a floating index.
- [[Cash Settlement]] is the method used when forwards settle financially rather than with physical delivery.
- [[Basis Risk]] arises when a forward hedge does not perfectly match the exposure in timing, location, or quality.
- [[Delivery]] in physically settled forwards requires coordination of logistics, quality inspection, and documentation.
- [[Option]] on a forward (a "swaption" or "forward option") adds asymmetric payoff to the linear forward structure.
- [[Implied Volatility]] is relevant when pricing options on forwards and assessing the cost of optionality versus a linear hedge.

## Common misconceptions
- **"Forwards and futures are the same thing."** They differ in standardization, counterparty risk, margining, settlement timing, and liquidity. These differences affect pricing, exit flexibility, and risk management.
- **"Forwards are always cheaper than futures."** OTC forwards can have wider bid/ask spreads due to lower liquidity and the embedded credit risk premium. The customization benefit comes at a cost.
- **"You can easily exit a forward position."** Forwards are bilateral agreements. To exit before maturity, you typically must negotiate an unwind with the original counterparty (at their quoted price) or enter an offsetting forward with a 3rd party, which introduces additional [[Basis Risk]].

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- BIS Triennial Central Bank Survey, OTC Derivatives Statistics
- CME Group, "Forwards vs Futures Comparison"
- ISDA, "2002 Master Agreement" documentation framework
