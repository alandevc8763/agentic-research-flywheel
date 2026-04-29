# Adaptive Test-Time Compute Allocation via Constrained Policy Optimization

## 1. Abstract
Adaptive test-time compute allocation optimizes the trade-off between accuracy and inference budget by dynamically assigning computation resources to inputs based on their difficulty. This approach moves beyond uniform compute budgets, treating allocation as a constrained optimization problem.

## 2. Technical Core: Constrained Policy Optimization (CPO)
The objective is to maximize the expected accuracy $\text{Acc}(\pi)$ subject to an average compute budget $\text{B}$:
$$\max_{\pi} \mathbb{E}_{x \sim \mathcal{D}} [\text{Acc}(\pi, x)] \quad \text{s.t.} \quad \mathbb{E}_{x \sim \mathcal{D}} [\text{Cost}(\pi, x)] \leq \text{B}$$

### 2.1 Solve-then-Learn Pipeline
The allocation strategy is implemented via a two-stage pipeline:
1. **Solve Stage (Lagrangian Relaxation)**:
   The global constraint is relaxed using a Lagrange multiplier $\lambda$:
   $$\mathcal{L}(\pi, \lambda) = \mathbb{E}_{\text{Acc}(\pi, x)} - \lambda (\mathbb{E}_{\text{Cost}(\pi, x)} - \text{B})$$
   This allows for per-instance optimal decisions (oracle actions) where compute is increased if the marginal gain in accuracy exceeds $\lambda$.
2. **Learn Stage (Amortized Allocation)**:
   A lightweight classifier is trained to predict the oracle action $a^*$ for a given input $x$, enabling real-time allocation without solving the Lagrangian in every step.

## 3. Performance & Scaling
- **Metric**: $\Delta\text{Accuracy}$ relative to uniform budget.
- **Results**: Achieving up to 12.8% improvement on MATH benchmarks by shifting compute from "easy" to "hard" instances.
- **Scaling Law**: $\text{Compute} \propto \text{Difficulty}(x)$.

## 4. Architectural Integration
For integration into agentic systems, this implies a **Compute-Aware Routing** layer that:
1. Analyzes input complexity.
2. Predicts optimal budget $\text{B}_x$.
3. Dispatches to a reasoning chain with corresponding depth/breadth.

## 5. Sources
- arXiv:2604.14853
