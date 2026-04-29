# 🌀 [Agentic Harness Engineering (AHE)]

$\text{AHE}$ operationalizes the autonomous evolution of coding-agent harnesses by transforming the engineering loop into a set of falsifiable contracts through three observability pillars. It addresses the inherent instability of harness tuning (noisy signals, sparse rewards) by instrumenting the $\text{Edit} \rightarrow \text{Inspect} \rightarrow \text{Decide}$ cycle.

### 🏗️ Architectural Framework

The framework decomposes harness evolution into three matched observability primitives:

1. **Component Observability** $\rightarrow$ **Explicit Action Space**
   - Every editable harness component (tool definitions, prompt templates, environment configs) is mapped to a unique file-level representation.
   - $\text{Result}$: The action space becomes discrete and revertible, eliminating the "black-box" effect of monolithic harness updates.

2. **Experience Observability** $\rightarrow$ **Evidence Distillation**
   - Raw, multi-million-token trajectories are distilled into a layered, drill-down evidence corpus.
   - $\text{Result}$: High-signal "experience" is extracted from noisy logs, allowing the evolving agent to consume actionable patterns rather than raw noise.

3. **Decision Observability** $\rightarrow$ **Falsifiable Contracts**
   - Every harness edit is paired with a self-declared prediction of the expected outcome.
   - $\text{Result}$: Edits are treated as hypotheses. Verification against subsequent task-level outcomes converts trial-and-error into a rigorous scientific process.

### 📈 Performance Impact

- **Empirical Gain**: Lifted $\text{pass@1}$ on $\text{Terminal-Bench 2}$ from $69.7\% \rightarrow 77.0\%$.
- **Generalization**: Evolved components showed $+5.1$ to $+10.1\text{pp}$ gains across alternate model families, indicating the capture of general engineering principles rather than benchmark overfitting.
- **Efficiency**: Topped aggregate success on $\text{SWE-bench-verified}$ using $12\%$ fewer tokens than the seed harness.

### ⚡ Key Insight
$\text{AHE}$ shifts the paradigm from **manual harness tuning** to **observability-driven evolution**, where the harness itself becomes a versioned, evolving artifact governed by empirical evidence.

---
**Source**: [arXiv:2604.25850](https://arxiv.org/abs/2604.25850) | **Category**: Agent Infrastructure / Self-Evolution / Observability
