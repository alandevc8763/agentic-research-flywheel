# 🧩 Non-Monotonic Reasoning Trajectories: Beyond Monotonic Decoding

## 📐 Architectural Overview
Traditional LLM inference is formulated as a **strictly monotonic process**:
$$\text{Probability}(\text{token}_t \mid \text{token}_{<t})$$
This linear progression creates a "commitment trap" where early errors propagate through the trajectory, necessitating expensive post-hoc correction agents. **Non-Monotonic Reasoning (NMR)** elevates generation to a dynamic trajectory where the model can explicitly backtrack, revise, and explore alternative reasoning paths within the decoding stream.

---

## 🛠️ Core Implementation Paradigms

### 1. In-Decoding Revision (Stream of Revision)
Proposed in `arXiv:2602.01187`, this approach internalizes the revision loop into the model's intrinsic semantic reasoning.

- **Mechanism**: Introduction of **Action Tokens** that trigger non-linear transitions in the KV-cache or output stream.
- **Operation**: 
    - $\text{Forward Pass} \rightarrow \text{Detection of Error} \rightarrow \text{Action Token [REVISE]} \rightarrow \text{Backtrack to index } i \rightarrow \text{Regenerate}$.
- **$\Delta\text{SNR}$ Gain**: Drastically reduces vulnerabilities in secure code generation by eliminating the latency of external static analysis tools.

### 2. Search-Taught Internalization (ASTRO)
Proposed in `arXiv:2507.00417`, ASTRO teaches models to "reason like search algorithms."

- **Mechanism**: Distilling **Monte Carlo Tree Search (MCTS)** traces into natural language Chain-of-Thought (CoT).
- **Logic**: 
    - $\text{MCTS Trace} \xrightarrow{\text{Synthesis}} \text{CoT with explicit "Success" and "Recovery from Failure" markers}$.
- **Outcome**: Internalizes structured search behavior (exploration $\rightarrow$ reflection $\rightarrow$ backtracking) into the model's weights.
- **Performance**: $\Delta\text{Accuracy}$ gains of $\approx 16\text{--}27\%$ on hard mathematical benchmarks (MATH-500, AIME 2024).

---

## 📈 Comparative Analysis: Monotonic vs. Non-Monotonic

| Metric | Monotonic (Standard CoT) | Non-Monotonic (NMR) | Impact |
| :--- | :--- | :--- | :--- |
| **Trajectory** | Linear / Immutable | Graph-like / Revisable | $\uparrow$ Search Space Efficiency |
| **Error Handling** | Post-hoc (Critic Agent) | In-situ (Intrinsic) | $\downarrow$ Inference Latency |
| **Compute** | Constant per token | Variable (Test-Time Scaling) | $\uparrow$ Reasoning Fidelity |
| **Convergence** | Greedy / Beam Search | Reflective / Backtracking | $\downarrow$ Hallucination Rate |

---

## 🎯 Synthesis for Agentic Systems
For the **Agentic Research Flywheel**, NMR provides the substrate for **Self-Correcting Trajectories** (Phase 3). By implementing a "Revision-Aware" prompt or fine-tuning on search-derived traces, the system can:
1. **Sensing**: Detect a contradiction in the distillation artifact.
2. **Backtracking**: Jump back to the raw discovery dataset.
3. **Refinement**: Re-distill with a corrected semantic mapping.

**Tags**: #ReasoningScaling #NonMonotonic #MCTS #SelfCorrection #InDecodingRevision
**Sources**: [arXiv:2602.01187], [arXiv:2507.00417]
