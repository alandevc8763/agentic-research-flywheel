# Knowledge Artifact: SHEAR (Self-Supervised Fine-Grained Credit Assignment)

## 🎯 Core Thesis
$\text{SHEAR}$ (Self-Supervised Hierarchical Evaluation and Assignment of Rewards) addresses the **credit assignment problem** in Reinforcement Learning from Verifiable Rewards ($\text{RLVR}$). While standard RLVR relies on outcome-based rewards (binary success/failure), $\text{SHEAR}$ implements a self-supervised mechanism to distribute reward signal back to individual reasoning steps, maximizing the gradient signal and accelerating convergence.

## 🏗️ Architectural Blueprint

### 1. Temporal Credit Distribution
Instead of a sparse reward $\text{R}_{total}$ at the end of a trajectory $\tau$, $\text{SHEAR}$ employs a **backward-pass attribution network** that decomposes the final reward into step-wise contributions:
$$\text{R}_{total} = \sum_{t=1}^{T} \gamma^{T-t} \hat{	ext{r}}_t$$
where $\hat{	ext{r}}_t$ is the estimated contribution of step $t$ to the final success.

### 2. Self-Supervised Proxy Rewards
To avoid the need for dense human-annotated rewards, $\text{SHEAR}$ leverages a **contrastive trajectory analysis** approach:
- **Positive Trajectories**: Steps that consistently appear in successful completions are assigned higher intrinsic value.
- **Negative Trajectories**: Steps that lead to failure, even if they look "correct" syntactically, are penalized.
The system learns a proxy reward function $\Phi(s_t, a_t)$ that predicts the probability of future success, acting as a dense signal for the policy gradient.

### 3. Fine-Grained Attribution (The "Slicing" Mechanism)
$\text{SHEAR}$ identifies **critical transition points** in the reasoning chain—steps where the probability of success shifts significantly. By applying a second-order derivative analysis to the value function, it "slices" the trajectory and assigns high credit to the specific logic jump that unlocked the solution.

## 📈 Performance Metrics
- **Sample Efficiency**: $\Delta\text{Efficiency} \approx 3\text{--}5\times$ improvement in convergence speed for complex math/coding tasks compared to vanilla GRPO.
- **Reasoning Stability**: Reduces "reward hacking" by ensuring that rewards are tied to structural logic rather than superficial pattern matching.
- **Verification Fidelity**: Higher correlation between $\hat{	ext{r}}_t$ and the actual correctness of the step as verified by an external Lean 4 or Python environment.

## 🛠️ Utility & Actionability
- **Primary Use Case**: Scaling RLVR for domains where the reward is sparse but the process is long (e.g., formal theorem proving, complex software synthesis).
- **Integration Path**: Integrate $\text{SHEAR}$ as a reward-shaping layer between the Verifiable Reward (Outcome) and the Policy Update (Learner).

---
**Tags**: #RLVR #Credit-Assignment #Self-Supervised #Reasoning #Reinforcement-Learning
**Source**: Internal Flywheel Synthesis / RLVR-Scaling-Research
