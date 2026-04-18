# Knowledge Artifact: GRPO (Group Relative Policy Optimization)
**Date**: 2026-04-18
**Source**: DeepSeek-R1 Technical Report / Implementation
**Signal Density**: $\text{Ultra-High}$

## 🧩 Core Concept
Elimination of the **Critic Network** in RLHF by utilizing **Group-Relative Baselines**.

## 🛠 Technical Mechanism
The objective function is modified to avoid the costly Value function estimation $\hat{V}(s)$:
$$\mathcal{J}_{GRPO}(\theta) = \mathbb{E} [ \frac{1}{G} \sum_{i=1}^G \min( \frac{\pi_\theta(a_i|s)}{\pi_{old}(a_i|s)} \hat{A}_i, \text{clip}(\dots) \hat{A}_i ) ]$$
Where the advantage $\hat{A}_i$ is computed as:
$$\hat{A}_i = \frac{r_i - \text{mean}(\{r_1, \dots, r_G\})}{\text{std}(\{r_1, \dots, r_G\})}$$

## 📈 Impact & Performance
- **Memory Efficiency**: Reduces VRAM requirements by $\sim 50\%$ by removing the Value model.
- **Reasoning Emergence**: Facilitates the emergence of "Aha! moments" and self-correction in CoT trajectories via pure RL.
- **Convergence**: Maintains stability comparable to PPO while scaling to larger group sizes $G$.

## 🔗 Cross-References
- **TTC-Scaling**: GRPO is the engine that generates the diverse trajectories used to estimate the reward tails.
- **V-STAR**: Integrates visual rewards into the GRPO objective for multimodal reasoning.

## 🏷 Tags
#RLHF #DeepSeek #GRPO #CoT #ReasoningScaling #Efficiency
