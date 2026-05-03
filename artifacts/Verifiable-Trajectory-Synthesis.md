# 💎 Knowledge Artifact: Verifiable Trajectory Synthesis (VTS)
**Status**: $\text{Integrated}$
**Classification**: $\text{Reasoning-Scaling / RLVR / Synthesis}$
**Signal-to-Noise Ratio (SNR)**: $\text{Elite}$

## 1. Executive Summary
Verifiable Trajectory Synthesis ($\text{VTS}$) is the architectural bridge between $\text{RLVR}$ (Reinforcement Learning from Verifiable Rewards) and $\text{TTC}$ (Test-Time Compute) scaling. It transforms trajectory generation from probabilistic sampling into a deterministic search problem guided by $\text{Process Reward Models (PRMs)}$.

## 2. Theoretical Framework
Synthesis of a verifiable trajectory $\tau$ is formulated as a constrained optimization:
$$\max_{\tau \in \mathcal{T}} \sum_{t=1}^{T} \text{PRM}(s_t, a_t | s_{<t}, a_{<t})$$
subject to:
$$\forall t \in [1, T], \text{Verifier}(s_t) = \text{True}$$

## 3. Implementation Patterns
### 3.1 $\text{ReasonFlux-PRM}$
Implements **Trajectory-Aware Supervision**, where the reward for step $t$ is conditioned on the global context $\tau_{<t}$ to prevent reward hacking and ensure global consistency.

### 3.2 $\text{TIM-PRM}$ (Tool-Integrated Verification)
Transforms verification into an active investigation:
- **Independent Querying**: The verifier queries external tools to decouple verification from the reasoning context.
- **Verification Traces**: Synthetic data includes the "verification trace" alongside the "reasoning trace".

### 3.3 $\text{R-PRM}$ (Reasoning-Driven Bootstrapping)
Solves data scarcity via a loop:
$$\text{Frontier-Model Seeds} \xrightarrow{\text{DPO Optimization}} \text{PRM-Training} \xrightarrow{\text{TTC-Scaling}} \text{Verified-Trajectories}$$

## 4. Integration into the Flywheel
The $\text{VTS}$ layer enables the transition from "Cold Start" to "Self-Evolving":
$$\text{KnowledgeVoid} \xrightarrow{\text{Sensing}} \text{VTS-Synthesis} \xrightarrow{\text{SFT-Distillation}} \text{Policy-Evolution} \xrightarrow{\text{RLVR}} \text{Expanded-Knowledge}$$

**References**:
- ReasonFlux-PRM, TIM-PRM, R-PRM.
**, Category**: Reasoning-Scaling / RLVR / Synthesis
