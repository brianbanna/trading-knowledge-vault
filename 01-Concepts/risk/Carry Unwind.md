---
aliases: [carry unwind, carry trade unwind, carry reversal]
tags:
  - "#fx"
  - "#risk"
date-added: "2026-03-20"
---

# Carry Unwind

## Definition
A carry unwind is the rapid, often violent reversal of [[Carry Trade|carry trade]] positions, where investors who had been long high yielding currencies and short low yielding ("funding") currencies are forced to close those positions simultaneously. The unwind typically occurs during sudden spikes in volatility or risk aversion: as losses mount, leveraged traders face margin calls, which trigger further selling of the high yield currency and buying of the funding currency, creating a self reinforcing feedback loop. Carry unwinds are characterized by extreme speed, sharp appreciation of funding currencies (especially JPY and CHF), and a breakdown of normal correlation structures. The process can erase months of carry income in a matter of hours or days.

## Why it matters (commodities and FX)
Carry unwinds create systemic risk for any portfolio exposed to high yield currencies or correlated assets. Because commodity currencies (AUD, NZD, NOK, BRL, ZAR) are popular carry longs, a carry unwind hits commodity FX portfolios especially hard. During the 2008 financial crisis and the August 2024 JPY unwind, commodity currencies fell in lockstep regardless of individual fundamentals. For risk managers, carry unwinds represent tail risk that standard volatility metrics underestimate: the distribution of carry returns is negatively skewed with fat left tails, meaning the worst day is far worse than normal models predict.

## Concrete example
In August 2024, the Bank of Japan unexpectedly raised rates by 15 basis points and signaled further tightening. USD/JPY, which had been a massive carry long for the global market at 162, crashed to 142 within 3 weeks. AUD/JPY fell from 109 to 93 (a 15% move) as carry traders unwound simultaneously. A hedge fund holding a 100 million AUD long against JPY with 10:1 leverage saw unrealized losses of 150 million JPY in days, triggering forced liquidation. The VIX spiked from 12 to 38 in a single session. Conversely, a trader who had positioned short AUD/JPY as a tail hedge before the event captured the entire move, but such positioning requires enduring months of negative carry.

## Key mechanics and formulas
- **Carry erosion speed**: In a typical unwind, spot can move 3 to 10 standard deviations in 1 to 5 days, erasing 6 to 18 months of carry income.
- **Feedback loop**: Initial losses → margin calls → forced liquidation → further adverse spot moves → more margin calls.
- **Correlation spike**: During unwinds, correlation among carry longs approaches 1.0 and correlation with funding currencies approaches −1.0, eliminating diversification.
- **Skewness of carry returns**: Carry strategies typically show skewness of −1.0 to −2.0 and excess kurtosis of 5 to 15, far from normal.
- **VIX threshold**: Historically, carry unwinds accelerate when VIX exceeds 25 to 30, as volatility triggered de risking amplifies the liquidation cycle.
- **Recovery time**: After major unwinds (2008, 2015, 2024), carry positions can take 3 to 12 months to rebuild as traders cautiously re enter.

## Prerequisites
- [[Carry Trade]]
- [[Interest Rate Differential]]
- [[G10 Currencies]]
- [[EM Currencies]]

## Related concepts (learn next)
- [[Carry Trade]]: the strategy that generates the positions which unwind; understanding carry construction is essential to understanding its reversal.
- [[Central Bank Intervention]]: CB actions can trigger or accelerate unwinds, as with the BOJ in 2024 or the SNB floor removal in 2015.
- [[Cross Currency Basis]]: the basis widens sharply during unwinds as demand for USD funding surges.
- [[Volatility]]: implied vol spikes during unwinds, making options on carry pairs extremely expensive precisely when hedging is most needed.
- [[EM Currencies]]: EM carry positions unwind with even greater violence than G10 due to lower liquidity and wider spreads.
- [[Monetary Policy Divergence]]: shifts in expected policy paths are the most common catalyst for carry unwinds.
- [[FX Swap]]: roll costs spike during unwinds as swap market liquidity dries up, adding to the pain for leveraged carry holders.

## Common misconceptions
1. **Carry unwinds are predictable**: While elevated volatility and extreme positioning increase the probability, the timing is nearly impossible to predict. The August 2024 unwind caught most participants off guard despite months of warnings about JPY carry crowding.
2. **Diversification protects during unwinds**: Holding 5 different carry pairs instead of 1 does not help when all carry longs sell off simultaneously. Diversification works in normal markets but fails precisely when needed most.
3. **Carry unwinds create buying opportunities**: Sometimes, but not always. The 1998 LTCM unwind and 2008 crisis unwinds were followed by further deterioration. Trying to catch the bottom of a carry unwind is extremely dangerous because the forced liquidation dynamic can persist far beyond fundamental fair value.
4. **Only leveraged funds are affected**: Carry unwinds affect anyone holding high yield currencies, including corporates with unhedged EM receivables, pension funds with yield seeking FX overlays, and retail traders.

## Sources
- Brunnermeier, Markus K. et al., "Carry Trades and Currency Crashes," NBER Macroeconomics Annual, 2009.
- Menkhoff, Lukas et al., "Carry Trades and Global Foreign Exchange Volatility," Journal of Finance, 2012.
- Bank for International Settlements, "The Anatomy of the Global FX Market Through the Lens of the 2022 Triennial Survey," BIS Quarterly Review, 2022.
