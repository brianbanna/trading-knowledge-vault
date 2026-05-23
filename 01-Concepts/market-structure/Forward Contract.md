---
aliases: [forward contract, forward, OTC forward]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Forward Contract

## Definition
A forward contract is a private, over the counter (OTC) agreement between 2 parties to buy or sell an asset at a specified price on a future date. Unlike a [[Futures Contract]] (standardized, exchange traded), forwards are fully customizable: parties negotiate quantity, quality, delivery location, settlement date, and reference index. Forwards carry bilateral counterparty credit risk because no clearinghouse stands between buyer and seller, though post 2008 regulations push standardized forwards toward central clearing. They are the workhorse of physical commodity markets where delivery terms do not match exchange contract specs. FX forwards are the most actively traded forward instruments, daily turnover exceeding $3 trillion. Settlement is at maturity rather than daily mark to market, though variation margin agreements are increasingly common for credit risk management.

## Why it matters (commodities and FX)
Forwards are essential for physical commodity trading because real world delivery needs rarely align with standardized futures. A Singapore jet fuel buyer needs delivery at Changi on specific dates in specific quantities; no exchange contract offers that. In FX, forwards let corporations hedge future foreign currency cash flows at known rates, locking in budget certainty. The forward price embeds the [[interest rate differential]] (FX) or cost of carry including storage and convenience yield (commodities), making forwards a fundamental building block for pricing theory and arbitrage.

## Concrete example

**Concrete:** An airline negotiates a 6 month forward to buy 1 million gallons of jet fuel at $2.50/gallon for December. Jet fuel rises to $3.00/gallon by December. Airline saves $500,000 vs spot, and has had cost certainty for route planning since the forward was booked. Failure mirror: same forward, jet fuel falls to $2.00/gallon. Airline locked at $0.50 above market, $500,000 opportunity cost. Unhedged competitors buy fuel cheaper. The bank that sold the forward also faces credit risk: airline distress could leave it exposed. Forwards lock in both upside and downside; OTC counterparty risk is real.

**Simplified:** A forward is a custom agreement between two parties to trade something at a set price on a future date. Different from a futures contract because the terms are negotiated, not standardized, and there is no exchange in between to guarantee the trade. Used when you need exact specifications that no exchange contract matches. The cost is bilateral credit risk and lower liquidity if you want to exit before maturity.

## Key mechanics and formulas
- **Forward price (commodities):** F = S × e^((r + c − y) × T), where S = spot, r = risk free rate, c = storage cost rate, y = convenience yield, T = time to maturity
- **Forward price (FX):** F = S × (1 + r_domestic × T) / (1 + r_foreign × T). Reflects [[covered interest parity]].
- **Key differences from [[Futures Contract|futures]]:**
  - Customizable vs standardized
  - OTC vs exchange traded
  - Counterparty risk vs clearinghouse
  - At maturity vs daily mark to market
  - Less liquid vs continuous secondary market
- **Credit mitigation:** ISDA master agreements, margin posting (CSA), netting, post crisis clearing mandates

## Prerequisites
- [[Futures Contract]]
- [[Margin]]

## Related concepts (learn next)
- [[Futures Contract]] is the standardized exchange traded version eliminating counterparty risk.
- [[Swap]] is effectively a series of forwards with periodic settlements against a floating index.
- [[Cash Settlement]] is the method when forwards settle financially rather than physically.
- [[Basis Risk]] arises when a forward hedge does not perfectly match the exposure in timing, location, or quality.
- [[Delivery]] in physically settled forwards requires logistics, quality inspection, documentation.
- [[Option]] on a forward adds asymmetric payoff to the linear structure.
- [[Implied Volatility]] is relevant when pricing options on forwards.

## Common misconceptions

**"Forwards and futures are the same."** Differ in standardization, counterparty risk, margining, settlement timing, and liquidity. These differences affect pricing, exit, and risk management.

**"Forwards are always cheaper than futures."** OTC forwards can have wider spreads due to lower liquidity and embedded credit risk premium. Customization has a cost.

**"You can easily exit a forward."** Bilateral. Exiting before maturity requires negotiating an unwind with the original counterparty or entering an offsetting forward with a 3rd party, introducing [[Basis Risk]].

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- BIS Triennial Central Bank Survey, OTC Derivatives Statistics
- CME Group, "Forwards vs Futures Comparison"
- ISDA, "2002 Master Agreement" documentation framework
