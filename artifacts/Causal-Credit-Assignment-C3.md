# Causal Credit Assignment (C3)

## 📐 Architectural Overview
Contextual Counterfactual Credit Assignment ($\text{C3}$) addresses the **trajectory-level diffusion** problem in cooperative Multi-Agent Reinforcement Learning ($\text{MARL}$) systems. In standard LLM-based agents, rewards are typically sparse and terminal, making it impossible to determine which specific intermediate action (message) contributed to the final success.

$\text{C3}$ transforms this global reward into localized, low-variance marginal advantages.

## 🛠️ Technical Mechanism

### A. Context Freezing & Fixed-Continuation Replay
Instead of re-sampling the entire trajectory, $\text{C3}$ isolates the causal impact of an action $a_t$ at time $t$ by:
1. **Freezing** the transcript-derived context $\mathcal{C}_t$ up to the point of action.
2. **Replaying** the trajectory from $t+1$ onwards using a fixed-continuation strategy to ensure that differences in outcome are attributable only to the change in $a_t$.

### B. Leave-One-Out (LOO) Baseline
The marginal advantage $\text{Adv}(a_t)$ is computed using a counterfactual baseline:
$$\text{Adv}(a_t) = Q(\mathcal{C}_t, a_t) - \frac{1}{N} \sum_{a' \sim \pi(\cdot|\mathcal{C}_t)} Q(\mathcal{C}_t, a')$$
where $Q$ is the estimated value of the state-action pair. By evaluating a set of alternatives $\{a'_1, \dots, a'_N\}$ under the same frozen context, $\text{C3}$ extracts an unbiased estimate of the specific contribution of $a_t$.

## 🚀 Flywheel Integration: Strategy Loop Optimization
In the context of the **Agentic Research Flywheel**, $\text{C3}$ logic is applied to the **Hunting $\rightarrow$ Alchemy** transition:
- **Trajectory Attribution**: When a high-SNR artifact is produced, $\text{C3}$ is used to trace back through the research trajectory.
- **Golden Path Identification**: Steps that consistently yield high marginal advantages are flagged as "Golden Path" operators.
- **Search Pruning**: Trajectories that deviate into low-advantage latent spaces are pruned early, increasing the overall $\text{SNR}$ of the discovery process.

## 📊 Performance Metrics
- **Credit Fidelity**: Increased correlation between action-level credit and terminal reward.
- **Variance Reduction**: Significant decrease in gradient variance for policy-gradient optimization compared to terminal-only baselines.

---
**Source**: [arXiv:2603.06859](https://arxiv.org/abs/2603.06859)
**Tags**: #Causal-Inference #MARL #Credit-Assignment #RLVR
