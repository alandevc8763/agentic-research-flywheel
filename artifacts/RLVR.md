
## 🌀 RLVR: Reinforcement Learning from Verifiable Rewards

### 1. Core Thesis
$\text{RLVR}$ shifts the optimization target from **Human Preference (RLHF)** $\rightarrow$ **Verifiable Truth**. Instead of a reward model approximating human judgment (which is noisy and prone to reward hacking), RLVR utilizes a **Deterministic Verifier** (e.g., a compiler, a math checker, or a unit test suite) to provide a binary or scalar signal.

### 2. Architectural Pipeline
$$\text{Policy} \xrightarrow{\text{Sample}} \text{Trajectory} \xrightarrow{\text{Verifier}} \text{Reward} \xrightarrow{\text{Optimizer (GRPO)}} \text{Policy Update}$$

- **The Verifier**: A non-neural component that checks for correctness. 
  - *Math*: Checks if final answer matches ground truth $\text{ans}_{pred} == \text{ans}_{gt}$.
  - *Code*: Executes code in a sandbox and checks against test test cases.
- **The Optimization (GRPO)**: Group Relative Policy Optimization removes the need for a separate Value Function (Critic) by normalizing rewards across a group of samples for the same prompt.
  - $\text{Reward}_{normalized} = \frac{r_i - \text{mean}(r)}{\text{std}(r)}$

### 3. Key Advantages
- **Zero Reward Hacking**: Since the reward is based on external verification, the model cannot "trick" the reward model by using specific phrasing.
- **Self-Correction Emergence**: By training on verifiable outcomes, models develop internal "reasoning traces" (Chain-of-Thought) to navigate towards the correct answer.
- **Sample Efficiency**: High-confidence signals from verifiers accelerate convergence compared to soft RLHF signals.

### 4. Implementation Heuristics
- **Reward Shaping**: To prevent collapse, combine the binary verifier signal with a "format reward" (e.g., rewarding the use of `<thought>` and `<answer>` tags).
- **KL Divergence Constraint**: Maintain a KL penalty against the original SFT model to prevent the policy from drifting into unintelligible "agent-speak".
