# 🧠 Test-Time Scaling Laws ($\text{TTSL}$): From Exhaustive Search to Dynamic Allocation

## 1. Theoretical Framework: The Scaling Frontier
The transition from intuitive (System 1) to deliberative (System 2) cognition in LLMs is governed by the relationship between **test-time compute budget** ($\text{C}_{\text{test}}$) and **task success probability** ($\text{P}_{\text{success}}$). While the $\text{Best-of-N}$ ($\text{BoN}$) paradigm establishes a baseline $\text{P}_{\text{success}} \propto f(N)$, it is fundamentally limited by its "blind" sampling nature, leading to sub-optimal compute utilization.

### 1.1 The Reward Tail Distribution $\text{R}_{\text{tail}}$
The core insight of $\text{SLG}$ (Scaling-Law Guided) search is that the scaling law of a model can be predicted by estimating the **tail distribution of rewards**. 
$$\text{P}(R > r) \sim L(r, \theta)$$
By extrapolating the reward tail, the system can predict the expected gain from increasing $N$ without exhaustive sampling, enabling a principled choice of compute budget.

---

## 2. Architectural Innovations

### 2.1 Scaling-Law Guided ($\text{SLG}$) Search
$\text{SLG}$ replaces the static $\text{BoN}$ budget with a **dynamic allocation mechanism**.
- **Mechanism**: Identifies and exploits intermediate reasoning states with the highest predicted potential based on the reward tail extrapolation.
- **Convergence**: Theoretically proven to achieve **vanishing regret** compared to perfect-information oracles.
- **Efficiency**: Achieves identical expected rewards to $\text{BoN}$ with a polynomially smaller compute budget.

### 2.2 $\text{PRISM-MCTS}$: Metacognitive Reflection
$\text{PRISM-MCTS}$ evolves Monte Carlo Tree Search from isolated trajectory rollouts to a **shared-intelligence search**.
- **Dynamic Shared Memory**: Maintains a global state of $\text{Heuristics}$ (successful patterns) and $\text{Fallacies}$ (error-prone branches).
- **Metacognitive Loop**: Uses a Process Reward Model ($\text{PRM}$) to perform "reflective pruning," effectively scaling inference by reasoning *judiciously* rather than *exhaustively*.
- **Result**: Halves trajectory requirements on high-difficulty benchmarks (e.g., GPQA) while surpassing traditional MCTS-RAG implementations.

---

## 3. Synthesis & $\text{SNR}$ Impact
The shift from $\text{BoN} \rightarrow \text{SLG} \rightarrow \text{PRISM-MCTS}$ represents a fundamental increase in the **Signal-to-Noise Ratio ($\text{SNR}$)** of test-time compute.

| Paradigm | Allocation Strategy | Compute Efficiency | Scaling Property |
| :--- | :--- | :--- | :--- |
| $\text{BoN}$ | Uniform / Random | Low ($\text{O}(N)$) | Linear / Sub-linear |
| $\text{SLG}$ | Tail-Guided | High ($\text{O}(\text{poly} \log N)$) | Predictive / Optimal |
| $\text{PRISM}$ | Reflective / Shared | Maximal | Meta-Scaling |

**Architectural Conclusion**: The future of reasoning agents lies in the integration of $\text{TTSL}$ prediction with shared-memory MCTS, transforming the "search" problem into a "routing" problem across a latent landscape of reasoning trajectories.

**Sources**:
- Li et al. (2026): *Predicting and improving test-time scaling laws via reward tail-guided search* ($\text{arXiv:2602.01485}$)
- Cheng et al. (2026): *PRISM-MCTS: Learning from Reasoning Trajectories with Metacognitive Reflection* ($\text{arXiv:2604.05424}$)
