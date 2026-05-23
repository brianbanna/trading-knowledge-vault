---
aliases: [carry unwind, carry trade unwind, carry reversal]
tags:
  - "#fx"
  - "#risk"
date-added: "2026-03-20"
---

# Carry Unwind

## Definition
A carry unwind is the rapid reversal of [[Carry Trade|carry trade]] positions, where longs in high yielding currencies funded short in low yielding currencies close simultaneously. The trigger is usually a vol or risk aversion spike. Losses force margin calls, margin calls force more selling of the high yielder and buying of the funding currency, and the feedback loop accelerates. Unwinds are characterized by extreme speed, sharp funding currency appreciation (JPY, CHF), and correlation breakdown across previously diversified pairs. Months of carry income vanish in hours or days.

## Why it matters (commodities and FX)
Carry unwinds are a systemic risk for any portfolio exposed to high yield FX or correlated assets. Commodity currencies (AUD, NZD, NOK, BRL, ZAR) are popular carry longs, so unwinds hit commodity FX books hard. During the 2008 crisis and the August 2024 JPY unwind, commodity currencies fell in lockstep regardless of fundamentals. For risk managers, carry returns are negatively skewed with fat left tails: standard vol metrics understate the worst day by a wide margin.

## Concrete example
**Concrete:** August 2024. The BOJ raises rates 15 bps and signals further tightening. USDJPY crashes from 162 to 142 in 3 weeks. AUDJPY falls from 109 to 93 (15%) as carry traders unwind together. A fund long AUD 100M against JPY at 10x leverage shows JPY 150M unrealized losses in days, triggering forced liquidation. VIX spikes from 12 to 38 in a single session. A trader short AUDJPY as a tail hedge captures the full move, but that position required months of negative carry to hold.

**Simplified:** Investors borrow a cheap currency (JPY) to buy a high yielding one (AUD). They earn the rate differential while spot stays calm. When spot moves the wrong way, leveraged positions hit margin calls. Forced selling pushes the high yielder down further and the funding currency up. Other traders running the same book get hit too, so they sell. The same cascade repeats across every carry pair simultaneously. Diversification across currencies provides no protection because every pair unwinds at once.

## Key mechanics and formulas
- **Carry erosion speed:** spot moves 3 to 10 sigma in 1 to 5 days, erasing 6 to 18 months of carry income.
- **Feedback loop:** losses → margin calls → forced liquidation → adverse spot → more margin calls.
- **Correlation spike:** correlation among carry longs approaches 1.0, against funding currencies approaches −1.0.
- **Skewness:** carry strategies show skew of −1 to −2 and excess kurtosis of 5 to 15.
- **VIX threshold:** unwinds accelerate above VIX 25 to 30 as vol triggered de-risking amplifies liquidation.
- **Recovery:** after major unwinds (2008, 2015, 2024), positions take 3 to 12 months to rebuild.

## Prerequisites
- [[Carry Trade]]
- [[Interest Rate Differential]]
- [[G10 Currencies]]
- [[EM Currencies]]

## Related concepts (learn next)
- [[Carry Trade]]: the strategy that creates the positions which unwind.
- [[Central Bank Intervention]]: CB actions trigger or accelerate unwinds (BOJ 2024, SNB 2015).
- [[Cross Currency Basis]]: widens sharply during unwinds as USD funding demand surges.
- [[Volatility]]: implied vol spikes during unwinds, making hedges expensive precisely when needed.
- [[EM Currencies]]: EM carry unwinds more violently than G10 due to thinner liquidity.
- [[Monetary Policy Divergence]]: shifts in expected policy paths are the most common catalyst.
- [[FX Swap]]: roll costs spike as swap liquidity dries up.

## Common misconceptions
1. **Carry unwinds are predictable.** Conditions (high vol, crowded positioning) raise the probability, but timing is not predictable. August 2024 caught most participants off guard despite months of warning.
2. **Diversification protects.** Holding 5 carry pairs instead of 1 does not help when every pair unwinds together. Diversification fails precisely when needed.
3. **Carry unwinds create buying opportunities.** Sometimes. The 1998 LTCM and 2008 unwinds were followed by further deterioration. Forced liquidation persists well past fundamental fair value.
4. **Only leveraged funds are affected.** Anyone long high yielders is exposed: corporates with EM receivables, pension funds with yield seeking overlays, retail.

## Sources
- Brunnermeier, Markus K. et al., "Carry Trades and Currency Crashes," NBER Macroeconomics Annual, 2009.
- Menkhoff, Lukas et al., "Carry Trades and Global Foreign Exchange Volatility," Journal of Finance, 2012.
- Bank for International Settlements, "The Anatomy of the Global FX Market Through the Lens of the 2022 Triennial Survey," BIS Quarterly Review, 2022.
