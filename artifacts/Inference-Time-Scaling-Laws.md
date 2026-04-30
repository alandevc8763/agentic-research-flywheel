# Knowledge Artifact: Inference-Time Compute Scaling Laws for Reasoning Models

## $\text{Architectural Overview}$
The paradigm shift from "Scaling Laws" (parameter-count $\rightarrow$ performance) to "Inference-Time Scaling Laws" (compute $\rightarrow$ performance) defines the current frontier of Reasoning LLMs (e.g., OpenAI o1, DeepSeek-R1). The core hypothesis is that for complex cognitive tasks, performance scales predictably with the amount of computation allocated at test-time, regardless of the base model size, provided the model has a sufficient "reasoning kernel."

## $\text{Key Mechanisms}$

### 1. Internal TTC (Test-Time Compute)
- **Trajectory Synthesis**: Generating multiple reasoning paths (CoT) and selecting the optimal one.
- **Rejection Sampling**: Using a Verifier or Reward Model to prune low-probability/incorrect trajectories, forcing the model to "think longer" to find a verifiable solution.
- **Dynamic Token Allocation**: Models dynamically allocate more tokens to challenging problems, effectively increasing the "thinking budget" $\mathcal{B}_{\text{TTC}}$ for high-entropy decision points.

### 2. External TTC (Search and Verification)
- **Process-Based Search**: Moving from "End-Point" verification (was the final answer correct?) to "Step-Level" verification (was this specific reasoning step valid?).
- **MCTS / Beam Search**: Implementing tree-based search over the latent reasoning space, guided by Process Reward Models (PRMs) to avoid "Semantic Drift."
- **Execution Feedback**: Integrating external tools (compilers, interpreters) as ground-truth verifiers to prune the search tree.

## $\text{Empirical Findings}$
- **Size vs. Compute Trade-off**: A smaller model (e.g., 32B) with aggressive TTC (search + verification) can outperform a massive model (e.g., 671B) that relies on a single-pass greedy decode.
- **Scaling Curves**: Reasoning performance follows a power-law relationship with $\text{compute\_at\_inference}$, allowing for predictable budget scaling.

## $\text{Actionability}$
- **Deployment Strategy**: For private/constrained environments, deploy a medium-sized open-source model (e.g., Llama-3-70B or Qwen-2.5-Coder) and invest in a high-fidelity PRM and a robust MCTS search wrapper.
- **Metric Shift**: Evaluate models not by "per-token" accuracy but by "per-compute-budget" success rate.

## $\text{Sources}$
- [arXiv:2503.23803](https://arxiv.org/abs/2503.23803) - "Thinking Longer, Not Larger: Enhancing Software Engineering Agents via Scaling Test-Time Compute"
- General Synthesis of o1/R1 Scaling Paradigms.
