# 💎 Knowledge Artifact: World-Model Planning for Autonomous Agents ($\text{WMP}$)

## 1. Theoretical Framework
World-Model Planning ($\text{WMP}$) represents a paradigm shift from reactive agents ($\text{Policy}: \mathcal{S} \rightarrow \mathcal{A}$) to deliberative agents that internalize environmental dynamics. The core objective is to minimize the divergence between imagined trajectories and real-world outcomes:
$$\min_{\pi} \mathbb{E}_{s_0 \sim \rho_0} \left[ \sum_{t=0}^{H} \gamma^t \mathcal{R}(s_t, a_t) \mid s_{t+1} \sim \text{WorldModel}(s_t, a_t) \right]$$

## 2. High-Signal Architectural Patterns

### A. Adaptive Lookahead Imagination ($\text{ITP}$)
Instead of fixed-horizon rollouts, **Imagine-then-Plan (ITP)** employs a dynamic horizon $H(s, g)$ based on the distance to goal $g$ and current task progress. This prevents "imagination collapse" in long-horizon tasks by allocating compute to critical decision junctions.

### B. Disentangled Dynamics Prediction ($\text{DDP-WM}$)
To solve the real-time constraint of Model Predictive Control ($\text{MPC}$), dynamics are decomposed into:
- $\text{Primary Dynamics}$: Sparse, high-frequency updates driven by direct physical/agent interaction.
- $\text{Secondary Dynamics}$: Dense, low-frequency background/contextual updates.
$\text{Result}$: $\approx 9\text{x}$ inference speedup with improved success rates in precise manipulation tasks.

### C. Model-Based Web Planning ($\text{WebDreamer}$)
Extends world models to non-simulated, irreversible environments (the Web).
- **World Model**: $\text{LLM}_{\text{WM}}(s, a) \rightarrow s_{\text{next}}$ (predicts HTML/DOM state changes).
- **Value Function**: $\text{LLM}_{\text{VF}}(s) \rightarrow v$ (estimates probability of task completion).
Allows "dreaming" and backtracking in the latent space before executing an irreversible API call.

### D. Sparse Latent Rollouts
Utilizes randomized grouped attention in Transformer-based world models to reduce the token overhead during forward prediction. This enables high-fidelity $\text{VLA}$ (Vision-Language-Action) planning on resource-constrained hardware.

## 3. Implementation Blueprint for Second Brain
To integrate $\text{WMP}$ into the autonomous flywheel:
1. **Sensing**: Use $\text{WorldDB}$ to maintain a structured entity-relationship graph.
2. **Planning**: Implement a $\text{Lookahead}$ loop where the agent simulates $N$ potential research trajectories.
3. **Evaluation**: Use a value function (or a Critic Agent) to score trajectories based on $\text{Expected Information Gain}$ ($\text{EIG}$).

## 4. Sources & References
- **Imagine-then-Plan**: [arXiv:2601.08955](https://arxiv.org/abs/2601.08955)
- **DDP-WM**: [arXiv:2602.01780](https://arxiv.org/abs/2602.01780)
- **WebDreamer**: [arXiv:2411.06559](https://arxiv.org/abs/2411.06559)
- **LAW Framework**: [arXiv:2312.05230](https://arxiv.org/abs/2312.05230)
- **Sparse Imagination**: [arXiv:2506.01392](https://arxiv.org/abs/2506.01392)
