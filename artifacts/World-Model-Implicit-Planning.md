# $\text{World-Model-Implicit-Planning}$: The Transition from Explicit Search to Latent Trajectory Optimization

## 1. Theoretical Framework: The Action-Space Feasibility Decay
In traditional Agentic Planning, the system performs an explicit search over the action space $\mathcal{A}$ to find a sequence $\tau = (a_1, a_2, \dots, a_H)$ that maximizes a reward $R(\tau)$. 

**The Feasibility Bottleneck**: As the horizon $H$ increases, the probability of a randomly sampled action sequence being "feasible" (i.e., physically or logically valid) decays exponentially:
$$P(\text{feasible}) \propto e^{-\lambda H}$$
This leads to the **Search Explosion Problem**, where the generator spends $99\%$ of its compute exploring "dead ends" in the action space.

## 2. The $\text{WAV}$ Architecture: World-Value-Action
The $\text{WAV}$ model solves this by shifting planning from the **Action Space** $\mathcal{A}$ to a **Structured Latent Space** $\mathcal{Z}$.

### 2.1 Component Decomposition
- **$\text{World Model } (\mathcal{W})$**: A generative transition model $p(z_{t+1} | z_t, a_t, o_t)$ that predicts the next latent state given current state, action, and observation.
- **$\text{Trajectory Value Function } (\mathcal{V})$**: A critic $V(z_{1:H})$ that evaluates the long-horizon utility of a latent trajectory, effectively acting as a "heuristic guide" for the latent search.
- **$\text{Latent-to-Action Decoder } (\mathcal{D})$**: Maps the optimized latent trajectory back to concrete actions: $a_t = \mathcal{D}(z_t)$.

### 2.2 Implicit Planning via Probability Concentration
Instead of $A^*$ or MCTS in action space, WAV performs **Inference in Latent Space**:
1. **Prior Sampling**: Generate a set of candidate latent trajectories $\{z_{1:H}^{(i)}\}$.
2. **Value Steering**: Use the Value Function $\mathcal{V}$ to reshape the distribution, concentrating probability mass on trajectories with high expected utility.
3. **Dynamic Feasibility Filtering**: The World Model $\mathcal{W}$ inherently constrains the latent space to "feasible" regions, bypassing the exponential decay of the action space.

## 3. Synthesis Matrix: Planning Paradigms

| Paradigm | Search Space | Guidance | Complexity | Failure Mode | Key Model |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Explicit Symbolic** | $\mathcal{A}$ (Discrete) | Heuristic $h(s)$ | $\mathcal{O}(b^H)$ | State Explosion | $\text{Classic A}^*$ |
| **MCTS / BoN** | $\mathcal{A}$ (Continuous) | Reward $R(\tau)$ | $\mathcal{O}(N \cdot H)$ | Reasoning Drift | $\text{OpenAI-o1}$ |
| **Latent Implicit** | $\mathcal{Z}$ (Latent) | Value $\mathcal{V}(z)$ | $\mathcal{O}(\text{Inference})$ | Latent Collapse | $\text{WAV-Model}$ |

## 4. Impact on the Flywheel
Integrating $\text{WAV}$ allows the $\text{Agentic Research Flywheel}$ to move beyond "Reasoning Loops" and toward **Predictive World Modeling**. By implementing a latent-space critic, the Watchdog can not only detect a knowledge gap but *simulate* the potential impact of filling that gap before initiating the research trajectory, optimizing the $\text{ROI}$ of the Hunting phase.

**Sources**: [arXiv:2604.14732](https://arxiv.org/abs/2604.14732)
