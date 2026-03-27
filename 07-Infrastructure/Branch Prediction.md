---
aliases: [branch prediction, branch misprediction, speculative execution, CPU prediction]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Branch Prediction

## Definition
Branch prediction is a CPU optimization where the processor guesses which direction a conditional branch (if/else, switch) will take and begins executing instructions along the predicted path before the condition is actually evaluated. If the guess is correct, execution continues at full speed. If the guess is wrong (a branch misprediction), the CPU must flush the speculatively executed instructions and restart from the correct branch, wasting roughly 15 to 20 clock cycles (5 to 7 nanoseconds on a modern processor). Modern CPUs predict correctly 95% to 99% of the time for common patterns, but data dependent branches with unpredictable outcomes (e.g., "is this tick an uptick or downtick?") defeat the predictor. Trading systems on the [[Hot Path]] minimize branching, use branchless code (bitwise operations, conditional moves), and sort data to make branches predictable.

## Why it matters (commodities and FX)
On the [[Hot Path]] of a commodity or FX trading system, the pricing function may contain dozens of conditional checks: is the spread wider than threshold, is position above limit, is this venue active, does this tick pass the filter. Each branch that mispredicts adds 5 to 7 nanoseconds. If 10 branches each mispredict 20% of the time, the expected penalty is $10 \times 0.20 \times 6 = 12$ nanoseconds per tick. That sounds small, but in a system targeting 100 nanosecond [[Tick to Trade]], it is 12% of the budget. For a Brent crude market maker competing against firms with branchless pricing engines, those 12 nanoseconds can mean losing queue priority on thousands of fills per day.

## Concrete example
An EUR/USD market maker on EBS has a pricing function with the following conditional logic on every tick:

```
if (spread > min_spread) → adjust quote
if (position > max_long) → skew offer
if (position < max_short) → skew bid
if (venue_latency > threshold) → skip venue
if (tick_age > stale_threshold) → ignore tick
```

Each condition depends on real time market state and is inherently unpredictable.

**Baseline:** 5 branches, each mispredicted 25% of the time, 6 nanosecond penalty each.
$$\text{Expected penalty} = 5 \times 0.25 \times 6 = 7.5 \text{ ns per tick}$$

**Win scenario (branchless rewrite):** The developer replaces if/else with conditional moves and arithmetic masking. For example, the position skew becomes:
$$\text{skew} = \text{base\_skew} \times \text{clamp}(\text{position} / \text{max\_position}, -1, 1)$$

No branches. The penalty drops to 0 nanoseconds. Over 1 million ticks per day, the system saves 7.5 milliseconds of cumulative compute time, but more importantly, every single tick is 7.5 nanoseconds faster, improving queue priority consistency.

**Fail scenario:** A developer adds a complex multi level if/else tree to handle 8 different market regimes on every tick. The predictor cannot learn the pattern because regime switches are rare and random. Misprediction rate hits 40%. The pricing function adds 20 nanoseconds of penalty, pushing [[Tick to Trade]] from 150 to 170 nanoseconds. The system loses priority on 30% of competitive fills.

## Key mechanics and formulas
**Branch misprediction penalty:**
$$T_{penalty} = \text{pipeline depth} \times \text{clock period}$$

On a modern Intel Xeon with a 14 stage pipeline at 3.5 GHz:
$$T_{penalty} = 14 \times \frac{1}{3.5 \times 10^9} \approx 4 \text{ ns}$$

In practice, measured penalties are 5 to 7 nanoseconds due to additional effects.

**Expected branch cost per tick:**
$$E[T_{branch}] = \sum_{i=1}^{N} p_i^{miss} \times T_{penalty}$$

Where $N$ is the number of branches on the hot path and $p_i^{miss}$ is the misprediction probability for branch $i$.

**Branchless conditional move example:**
Instead of: `if (a > b) result = x; else result = y;`
Use: `result = y + (x - y) * (a > b);`

The compiler generates a `cmov` instruction with 0 misprediction risk.

## Prerequisites
- [[Hot Path]]
- [[Cache Locality]]
- [[Latency]]

## Related concepts (learn next)
- [[Hot Path]] is where branch mispredictions have the greatest impact on [[Tick to Trade]].
- [[Cache Miss]] is the other major CPU stall source alongside branch misprediction.
- [[Cache Locality]] interacts with branch prediction because mispredicted branches can trigger unnecessary cache prefetches.
- [[FPGA]] avoids branch prediction entirely by implementing all paths in parallel in hardware.
- [[Tick to Trade]] latency includes branch misprediction penalties in the signal evaluation and order construction stages.
- [[Tail Latency]] is worsened by branches that mispredict rarely but catastrophically (e.g., error handling paths).
- [[Compiler Optimization]] flags like `-O3` and profile guided optimization (PGO) help the compiler generate branchless code.

## Common misconceptions
1. **"Branch prediction does not matter because CPUs are 99% accurate."** That 99% accuracy is an average across all code. Data dependent branches in trading logic (comparing live prices, positions, thresholds) have much lower prediction rates, often 50% to 80%.
2. **"Removing all if statements makes code faster."** Branchless code can be slower when the branch is highly predictable (e.g., error checks that almost never trigger). The CPU predicts these correctly 99.9% of the time. Replacing them with branchless arithmetic adds unconditional work.
3. **"This only matters for HFT."** Branch mispredictions also affect backtest throughput. A branchy pricing model backtesting over 100 million ticks can be 2x to 3x slower than a branchless equivalent.

## Sources
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- Agner Fog, "Microarchitecture of Intel, AMD, and VIA CPUs" (agner.org)
- Intel, "Intel 64 and IA 32 Architectures Optimization Reference Manual"
- "Performance Analysis and Tuning on Modern CPUs" by Denis Bakhvalov
