---
aliases: [branch prediction, branch misprediction, speculative execution, CPU prediction]
tags:
  - "#infrastructure"
date-added: "2026-03-27"
---

# Branch Prediction

## Definition
Branch prediction is a CPU optimization where the processor guesses which side of a conditional (if/else, switch) will execute and runs instructions along that path before the condition resolves. A correct guess keeps the pipeline full. A wrong guess (misprediction) forces the CPU to flush speculative work and restart, costing 15 to 20 clock cycles (5 to 7 nanoseconds on modern hardware). Modern CPUs hit 95 to 99% accuracy on regular patterns, but data dependent branches with unpredictable outcomes (uptick vs downtick) defeat the predictor. Low latency trading systems minimize branching on the [[Hot Path]], use branchless code (bitwise ops, conditional moves), and sort data to make branches predictable.

## Why it matters (commodities and FX)
On the [[Hot Path]] of a commodity or FX system, the pricing function holds dozens of conditional checks: spread above threshold, position above limit, venue active, tick fresh. Each misprediction adds 5 to 7 nanoseconds. With 10 branches at 20% misprediction rate, the penalty is $10 \times 0.20 \times 6 = 12$ nanoseconds per tick. In a 100 nanosecond [[Tick to Trade]] budget, that is 12%. For a Brent crude market maker against firms running branchless pricing, those 12 nanoseconds cost queue priority on thousands of fills per day.

## Concrete example
**Concrete:** EURUSD market maker on EBS, pricing function with 5 branches per tick (spread, long limit, short limit, venue latency, tick age). Each mispredicts 25% of the time at 6 ns penalty: $5 \times 0.25 \times 6 = 7.5$ ns per tick. The developer rewrites with conditional moves and arithmetic masking, e.g., $\text{skew} = \text{base\_skew} \times \text{clamp}(\text{position} / \text{max\_position}, -1, 1)$. Penalty drops to 0. Over 1 million ticks per day, every single tick is 7.5 ns faster, holding queue priority that earns the desk 200 extra fills.

**Simplified:** Modern CPUs guess which side of an if statement will execute and run ahead. A wrong guess wastes 5 to 7 nanoseconds clearing the pipeline. When the condition depends on live market data (random by nature), the CPU guesses wrong 20 to 40% of the time. Replace the if statement with arithmetic and the guess goes away.

## Key mechanics and formulas
**Branch misprediction penalty:**
$$T_{penalty} = \text{pipeline depth} \times \text{clock period}$$

On a modern Intel Xeon with a 14 stage pipeline at 3.5 GHz:
$$T_{penalty} = 14 \times \frac{1}{3.5 \times 10^9} \approx 4 \text{ ns}$$

Measured penalties run 5 to 7 ns with additional effects.

**Expected branch cost per tick:**
$$E[T_{branch}] = \sum_{i=1}^{N} p_i^{miss} \times T_{penalty}$$

Where $N$ is the number of branches on the hot path and $p_i^{miss}$ is the misprediction probability for branch $i$.

**Branchless conditional move example:**
Instead of: `if (a > b) result = x; else result = y;`
Use: `result = y + (x - y) * (a > b);`

The compiler emits a `cmov` instruction with 0 misprediction risk.

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
- [[Tail Latency]] is worsened by branches that mispredict rarely but catastrophically (error handling paths).
- [[Compiler Optimization]] flags like `-O3` and profile guided optimization (PGO) help generate branchless code.

## Common misconceptions
1. **"Branch prediction does not matter because CPUs are 99% accurate."** That 99% is the average across all code. Data dependent branches in trading logic (live prices, positions, thresholds) predict at 50 to 80%.
2. **"Removing all if statements makes code faster."** Branchless code is slower when the branch is highly predictable (error checks that never trigger). The CPU predicts these at 99.9%. Replacing them with branchless arithmetic adds unconditional work.
3. **"This only matters for HFT."** Branch mispredictions also tank backtest throughput. A branchy pricing model over 100 million ticks runs 2 to 3x slower than a branchless equivalent.

## Sources
- "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson
- Agner Fog, "Microarchitecture of Intel, AMD, and VIA CPUs" (agner.org)
- Intel, "Intel 64 and IA 32 Architectures Optimization Reference Manual"
- "Performance Analysis and Tuning on Modern CPUs" by Denis Bakhvalov
