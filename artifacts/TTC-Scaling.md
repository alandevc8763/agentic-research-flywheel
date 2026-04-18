# 🚀 Knowledge Artifact: TTC-Scaling (The Laws of Test-Time Compute)

## 1. Core Thesis
The transition from **System 1 (Intuitive)** to **System 2 (Deliberative)** reasoning in LLMs is governed by the allocation of compute during the inference phase. Performance is not merely a function of parameter count $\Theta$, but of the total test-time compute $\text{TTC}$ invested in exploration and verification.

## 2. The Fundamental Scaling Law
Empirical evidence suggests a power-law relationship between the search budget (samples, search depth, or CoT length) and the probability of correctness $P(\text{correct})$:
$$\text{Performance} \approx k \cdot \text{TTC}^\alpha$$
where $\alpha$ is the scaling exponent determined by the task complexity and the quality of the verifier.

## 3. The Compute-Optimal Frontier
There exists an isomorphism between training-time parameters and test-time compute. A **Compute-Optimal Inference** strategy balances:
- **Model Scale**: $\Theta$ (The "prior" knowledge).
- **Search Budget**: $N$ (The "deliberation" effort).

**Trade-off**: A smaller model with a large search budget (e.g., MCTS-guided) can often outperform a massive model using greedy decoding, provided a high-fidelity **Verifier** is available.

## 4. Taxonomy of TTC Methodologies
| Method | Mechanism | Compute Driver | Scaling Characteristic |
| :--- | :--- | :--- | :--- |
| **Best-of-N (BoN)** | Parallel Sampling $\rightarrow$ RM Selection | $N \times \text{Forward Pass}$ | Logarithmic/Saturating |
| **MCTS** | Tree Exploration $\rightarrow$ Value Pruning | $\text{Nodes Explored}$ | Exponential $\rightarrow$ Polynomial |
| **CoT Scaling** | Extended Reasoning Traces | $\text{Token Count}$ | Linear/Drifting |
| **Looped Transformers** | Recurrent Layer Application | $\text{Iterations} \times L$ | Depth-Scaling |

## 5. Critical Failure Modes
- **The Verifier Bottleneck**: The scaling of $\text{TTC}$ is strictly bounded by the Reward Model's $\text{SNR}$. If the verifier cannot distinguish the ground truth from a "high-scoring hallucination," $\alpha \to 0$.
- **Reasoning Drift**: For extended $\text{TTC}$ (long CoT), models exhibit an "Inverted U" performance curve where compounded errors eventually lead to a collapse in accuracy.

## 6. High-Signal Resources
- **Reward Tail-Guided Search** ([arXiv:2602.01485](https://arxiv.org/abs/2602.01485)) - Optimizing BoN scaling.
- **Adaptive TTC Allocation** ([arXiv:2604.14853](https://arxiv.org/abs/2604.14853)) - Dynamic budget allocation.
- **Parcae** ([arXiv:2604.12946](https://arxiv.org/abs/2604.12946)) - Scaling laws for looped architectures.
- **PRISM-MCTS** ([arXiv:2604.05424](https://arxiv.org/abs/2604.05424)) - Metacognitive reflection via MCTS.
