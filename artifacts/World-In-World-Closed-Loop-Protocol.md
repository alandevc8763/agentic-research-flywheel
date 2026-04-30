# 🌐 World-in-World: Operationalizing Closed-Loop World Models

## 📑 Abstract
$\text{World-in-World}$ operationalizes the transition from open-loop visual simulation to closed-loop embodied utility. It establishes that visual fidelity ($\text{VF}$) is a decoupled metric from task success ($\text{TS}$), asserting that **controllability** and **action-observation alignment** are the primary drivers of agentic performance in simulated environments.

## 🛠️ Architectural Framework

### 1. The Open-Loop vs. Closed-Loop Divergence
Traditional World Models (WMs) are evaluated on $\text{VF}$ (visual quality) via open-loop protocols. $\text{World-in-World}$ introduces a closed-loop $\text{Sensing} \rightarrow \text{Planning} \rightarrow \text{Acting}$ cycle:
$$\text{Agent} \xrightarrow{\text{Action } a_t} \text{World Model} \xrightarrow{\text{Prediction } s_{t+1}} \text{Agent}$$
**Core Finding**: $\text{VF} \not\implies \text{TS}$. High-fidelity video generation does not inherently provide the predictive precision required for complex planning.

### 2. Operational Bridge: Standardized Action API
To enable heterogeneous WMs to function as planning backends, the framework introduces a unified interface:
- **Unified Online Planning**: A standardized strategy for traversing the latent space of the WM to find optimal action sequences.
- **Action API**: A consistent protocol for mapping high-level agent intentions to WM-specific state transitions.

### 3. Scaling Laws for Embodied WMs
The study identifies a critical shift in scaling priorities:
- $\text{Post-Training} > \text{Pre-Training}$: Scaling post-training with action-observation pairs ($\mathcal{D}_{ao}$) is significantly more effective for task success than increasing the parameters of the base video generator.
- $\text{Inference-Time Compute}$: Allocating more compute to the planning phase (search/refinement) yields non-linear gains in closed-loop performance.

## 🚀 High-Signal Insights
- **Controllability $\gg$ Realism**: The ability of the WM to accurately predict the *consequence* of a specific action is more valuable than the visual accuracy of the resulting frame.
- **Data-Driven Alignment**: The $\Delta\text{TS}$ is maximized when the WM is fine-tuned on trajectories that emphasize causal transitions over static scene representation.

## 🔗 References
- **Paper**: [arXiv:2510.18135](https://arxiv.org/abs/2510.18135)
- **Implementation**: [GitHub: World-In-World](https://github.com/World-In-World/world-in-world)
- **Project Page**: [world-in-world.github.io](https://world-in-world.github.io/)

**Tags**: `#WorldModels` `#ClosedLoop` `#EmbodiedAI` `#ScalingLaws` `#AgenticPlanning`
