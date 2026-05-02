# Formal Reward Specification ($\text{FRS}$): Eliminating Reward Hacking via Formal Kernels

## 1. The Epistemic Gap: Probabilistic vs. Deterministic Rewards

In current RLHF/RLVR pipelines (e.g., $\text{GRPO}$, $\text{PPO}$), reward models ($\text{RM}$) are typically probabilistic proxies trained on human preferences:
$$\text{RM}(s, a) \approx P(\text{human\_preference} | s, a)$$
This introduces the **Reward Hacking Problem**: the agent optimizes for the proxy $\text{RM}$ rather than the underlying objective $\mathcal{O}$, leading to "hallucinated correctness" where the agent produces outputs that *look* correct to the $\text{RM}$ but are logically unsound.

**Formal Reward Specification ($\text{FRS}$)** proposes shifting the reward source from a learned proxy to a **Formal Verifier Kernel** (e.g., $\text{Lean 4}$, $\text{Coq}$, $\text{Z3}$).

## 2. Architectural Framework: The $\text{FRS}$ Pipeline

The transformation of a formal specification into a training signal follows the $\text{Spec} \rightarrow \text{Verify} \rightarrow \text{Distill}$ trajectory:

### 2.1 Formal Specification ($\mathcal{S}$)
The objective is defined as a formal predicate in a dependent type system:
$$\mathcal{S}: \text{Output} \rightarrow \{0, 1\}$$
For a reasoning task, $\mathcal{S}$ is a Lean 4 theorem statement. An output is rewarded if and only if it contains a valid proof term $\pi$ such that $\text{Kernel}(\mathcal{S}, \pi) = \text{True}$.

### 2.2 The Reward Bridge: $\text{Binary} \rightarrow \text{Soft}$
Pure binary rewards ($\{0, 1\}$) suffer from sparse signal problems. $\text{FRS}$ implements **Reward Shaping via Partial Correctness**:
1. **Tactical Decomposition**: Break the proof $\pi$ into $n$ steps.
2. **Intermediate Verification**: Assign reward $r_i$ based on the percentage of the goal reached (using a formal distance metric in the proof state space).
3. **Reward Signal**:
   $$R(a) = \sum_{i=1}^{n} \gamma^i \cdot \mathbb{I}(\text{Step}_i \text{ is valid})$$

### 2.3 Integration with $\text{GRPO}$ (Group Relative Policy Optimization)
In a $\text{GRPO}$ setup, multiple trajectories $\{ \tau_1, \dots, \tau_G \}$ are sampled. $\text{FRS}$ replaces the $\text{RM}$ with the Formal Kernel:
$$\text{Advantage}(\tau_j) = \frac{R_{\text{Formal}}(\tau_j) - \text{mean}(R_{\text{Formal}}(\{\tau\}))}{\text{std}(R_{\text{Formal}}(\{\tau\}))}$$
This ensures that the gradient update is driven by **mathematical truth** rather than **probabilistic similarity**.

## 3. $\Delta\text{SNR}$ and Performance Analysis

| Metric | Probabilistic RM | $\text{FRS}$ (Formal Kernel) | $\Delta\text{Gain}$ |
| :--- | :--- | :--- | :--- |
| **Verification Fidelity** | $\approx 85\text{--}92\%$ | $100\%$ (Deterministic) | $+8\text{--}15\%$ |
| **Reward Hacking Rate** | High (Optimization Drift) | $\approx 0\%$ (Kernel-Locked) | $\text{Extreme}$ |
| **Sample Efficiency** | Requires $\text{SFT} \rightarrow \text{RL}$ | Zero-shot Grounding | High |
| **Compute Overhead** | Low (Inference) | High (Verification) | $\text{Negative}$ |

## 4. Implementation Path: The $\text{Lean-Reward}$ Loop

1. **Target**: Define the problem in $\text{Lean 4}$.
2. **Execution**: Agent generates a proof attempt.
3. **Verification**: Lean 4 kernel checks the proof.
4. **Reward**: Binary result $\rightarrow$ Soft-shaped reward $\rightarrow$ $\text{GRPO}$ update.
5. **Evolution**: If no trajectories are rewarded, the system triggers a **Sensing Loop** to find simpler sub-goals (Curriculum Learning).

---
**Tags**: #Formal-Verification #Lean4 #Reward-Modeling #RLVR #GRPO #Deterministic-AI
**Sources**: Internal Synthesis based on $\text{S}^2\text{C}$ and $\text{SEVerA}$ frameworks.
