# 🧠 Metacognitive Control Framework ($\text{MCF}$) for Autonomous Agents

## 1. Abstract
The $\text{MCF}$ provides a formal substrate for agents to monitor, regulate, and optimize their own cognitive processes. By decoupling **Task Execution** ($\text{S}_1$) from **Cognitive Regulation** ($\text{S}_2$), the agent can navigate open-ended goal spaces and novel environments without catastrophic failure or design fixation.

## 2. Formal Architecture

### 2.1 The Metacognitive Loop ($\mathcal{L}_{meta}$)
The control flow is defined as a continuous cycle of self-assessment and strategic adjustment:
$$\text{State } \mathcal{S} \xrightarrow{\text{Competence Sensing}} \mathcal{C} \xrightarrow{\text{Strategic Policy}} \pi_{meta} \xrightarrow{\text{Execution}} \mathcal{A} \xrightarrow{\text{Reflection}} \Delta \mathcal{C}$$

### 2.2 Core Components

#### A. Competence Sensing ($\mathcal{C}$)
The agent maintains a dynamic model of its own capabilities.
- **Learning Progress ($\text{LP}$)**: Predicted gain in competence for a given goal $g$.
  $$\text{LP}(g) = \mathbb{E}[\mathcal{C}_{t+1}(g) - \mathcal{C}_t(g)]$$
- **Confidence-Awareness**: Using posterior inverse covariance of control actions to determine the reliability of a chosen tool/path.

#### B. Strategic Policy ($\pi_{meta}$)
A high-level governor that selects the operational mode based on $\mathcal{C}$ and $\text{LP}$:
1. **Autonomous Mode**: $\mathcal{C} > \tau_{high}$ $\rightarrow$ Execute task using optimal known trajectory.
2. **Exploratory Mode**: $\text{LP} > \tau_{gain}$ $\rightarrow$ Prioritize goals that maximize learning.
3. **Co-Regulation Mode**: $\mathcal{C} < \tau_{low}$ $\rightarrow$ Trigger a secondary 'Critic' agent to break design fixation.
4. **Deferral Mode**: $\mathcal{C} \approx 0$ $\rightarrow$ Defer to human expert (HILA framework).

#### C. Reflection & Update ($\Delta \mathcal{C}$)
Post-execution, the agent performs an **Isomorphic Perturbation Test (IPT)** to verify if the success was due to robust reasoning or stochastic reward hacking, subsequently updating the competence map $\mathcal{C}$.

## 3. Implementation Blueprint
| Module | Mechanism | Reference |
| :--- | :--- | :--- |
| **LP-Predictor** | Semantic goal embedding $\rightarrow$ Regression | MAGELLAN (2502.07709) |
| **Competence-Gate** | World-model based self-assessment | MUSE (2411.13537) |
| **Co-Regulator** | Adversarial Critic Loop | CRDAL (2603.24768) |
| **Dual-Loop Opt** | GRPO (Inner) $\rightarrow$ Continual Learning (Outer) | HILA (2603.07972) |

## 4. Engineering Impact
Integrating $\text{MCF}$ into the Agentic Research Flywheel allows the `GapDetector` to not only find *what* is missing but to assess *if* the current agent has the competence to fill that gap, automatically escalating to more complex "Hunting" strategies when high-priority voids are detected.
