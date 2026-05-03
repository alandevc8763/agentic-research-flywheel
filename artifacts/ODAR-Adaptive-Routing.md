# 💎 Knowledge Artifact: ODAR (Adaptive Routing via Active Inference)

## 🛠️ Architectural Core
ODAR (Principled Adaptive Routing) implements a dynamic resource allocation framework to optimize the $\text{accuracy-efficiency}$ trade-off in LLM reasoning. It replaces uniform brute-force sampling (e.g., Best-of-N) with a principled routing mechanism.

### 🗝️ Key Mechanisms
- **Difficulty Estimator**: Utilizes **amortized active inference** to predict the complexity of a query.
- **Dual-Agent Routing**:
    - $\text{Fast Agent}$: Heuristic-based, low-latency response.
    - $\text{Slow Agent}$: Deliberative, high-compute reasoning trajectory.
- **Fusion Logic**: Implements a **free-energy-principled, risk-sensitive fusion mechanism**. It selects the optimal answer by minimizing a **variational free energy** objective, balancing $\text{log-likelihood}$ with **epistemic uncertainty** ($\text{varentropy}$).

## 📈 Performance Metrics
- **SOTA Results**: $98.2\%$ accuracy on $\text{MATH}$, $54.8\%$ on $\text{Humanity's Last Exam (HLE)}$.
- **Efficiency**: Reduced computational costs by $82\%$ compared to homogeneous sampling strategies on a Llama 4 + DeepSeek stack.

## 🧬 Synthesis & Integration
ODAR provides the mathematical grounding for "thinking-optimal scaling," proving that adaptive resource allocation (informed by active inference) is superior to raw test-time compute scaling.

**Sources**: [arXiv:2602.23681](https://arxiv.org/abs/2602.23681)
**Tags**: #ActiveInference #AdaptiveRouting #TestTimeCompute #VariationalFreeEnergy
