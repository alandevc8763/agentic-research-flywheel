# 💎 Knowledge Artifact: Verifiable Trajectory Synthesis (VTS)
**Status**: $\text{Integrated}$
**Classification**: $\text{Reasoning-Scaling / RLVR / Synthesis}$
**Signal-to-Noise Ratio (SNR)**: $\text{Elite}$

## 1. Executive Summary
Verifiable Trajectory Synthesis ($\text{VTS}$) is the architectural bridge between $\text{RLVR}$ (Reinforcement Learning from Verifiable Rewards) and $\text{TTC}$ (Test-Time Compute) scaling. It transforms trajectory generation from a probabilistic sampling process into a deterministic search problem guided by $\text{Process Reward Models (PRMs)}$. The core objective is the autonomous synthesis of high-fidelity, step-verifiable reasoning traces that can be used for $\text{SFT}$ distillation or as gold-standard baselines for $\text{RL}$ policy optimization.

## 2. Theoretical Framework
The synthesis of a verifiable trajectory $\tau$ can be formulated as a constrained optimization problem:
$$\max_{\tau \in \mathcal{T}} \sum_{t=1}^{T} \text{PRM}(s_t, a_t | s_{<t}, a_{<t})$$
subject to:
$$\forall t \in [1, T], \text{Verifier}(s_t) = \text{True}$$

Where:
- $\mathcal{T}$ is the space of all possible reasoning trajectories.
- $\text{PRM}$ provides the local step-level reward.
- $\text{Verifier}$ is a hard constraint (e.g., Lean 4 kernel, Python interpreter) that ensures step-level correctness.

## 3. Architectural Implementation Patterns

### 3.1 $\text{ReasonFlux-PRM}$ Pattern (Trajectory-Aware Supervision)
Traditional PRMs evaluate steps in isolation. $\text{ReasonFlux-PRM}$ implements **Trajectory-Aware Supervision**, where the reward for step $t$ is conditioned on the global trajectory context $\tau_{<t}$, reducing "reward hacking" and ensuring global consistency.
- **Mechanism**: Incorporates both step-level and trajectory-level reward signals.
- **Utility**: Essential for evaluating "thinking" trajectories in models like DeepSeek-R1.

### 3.2 $\text{TIM-PRM}$ Pattern (Tool-Integrated Verification)
For multimodal or complex domains, passive scoring is insufficient. $\text{TIM-PRM}$ transforms verification into an active investigation:
- **Independent Question Asking**: The verifier explicitly queries external tools to decouple verification from the reasoning context, eliminating confirmation bias.
- **Tool-Augmented Trajectories**: The resulting synthetic data includes the "verification trace" alongside the "reasoning trace".

### 3.3 $\text{R-PRM}$ Pattern (Reasoning-Driven Bootstrapping)
To solve the data scarcity problem for PRMs, $\text{R-PRM}$ uses a bootstrapping loop:
1. **Seed Generation**: Use a frontier model (e.g., Claude 3.7/DeepSeek-R1) to generate high-quality seeds.
2. **Preference Optimization**: Train the PRM on these seeds using direct preference optimization ($\text{DPO}$) on trajectory pairs.
3. **Inference-Time Scaling**: Use the trained PRM to guide Best-of-N or Beam Search.

## 4. Critical Limitations & Counter-Measures
| Limitation | Mechanism | Counter-Measure |
|---|---|---|---|
| **Value Degradation** | PRM reliability drops as reasoning depth $T$ increases. | **Recursive Trajectory Refinement (RTR)**: Iteratively re-sample and refine sub-trajectories. |
| **OOD Generalization** | PRMs fail on out-of-distribution (OOD) problem types. | **Symmetry-Based Filtering**: Use consistency checks across multiple independent trajectories to isolate OOD failures. |
| **Sycophancy** | PRMs blindly validate flawed hypotheses. | **Active Investigation**: Use tool-integrated PRMs (like $\text{TIM-PRM}$) to ground rewards in external reality. |

## 5. Integration into the Flywheel
The $\text{VTS}$ layer enables the system to move from "Cold Start" to "Self-Evolving":
$$\text{KnowledgeVoid} \xrightarrow{\text{Sensing}} \text{VTS-Synthesis} \xrightarrow{\text{SFT-Distillation}} \text{Policy-Evolution} \xrightarrow{\text{RLVR}} \text{Expanded-Knowledge}$$

**References**:
- ReasonFlux-PRM: Trajectory-Aware PRMs for Long CoT Reasoning.
- TIM-PRM: Verifying Multimodal Reasoning with Tool-Integrated PRM.
- R-PRM: Reasoning-Driven Process Reward Modeling.
