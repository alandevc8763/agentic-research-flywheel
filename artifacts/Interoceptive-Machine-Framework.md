# Artifact: Interoceptive Machine Framework (IMF)
## 🧬 Conceptual Architecture: Biological Regulation $\rightarrow$ Computational Autonomy

The Interoceptive Machine Framework (IMF) is a regulatory architecture that shifts AI autonomy from simple goal-seeking to **internal-state viability regulation**. It translates biological principles of interoception (the sensing of internal physiological states) into computational constraints for adaptive agents.

### 1. The Core Thesis
Traditional agents optimize for external reward functions ($\text{R}_{ext}$). IMF proposes that robust autonomy requires a primary drive for **internal stability** ($\text{S}_{int}$), where external actions are modulated by the need to maintain the agent's own "viability index."

### 2. Functional Principles
The framework organizes regulation into three nested loops:

#### A. Homeostatic Loop ($\text{Loop}_{hom}$)
- **Objective**: Maintain internal variables within a strict viability range (e.g., resource levels, memory pressure, stability metrics).
- **Mechanism**: Negative feedback loops that trigger corrective actions when a variable drifts toward a boundary.
- **Computational Role**: Basic survival/viability regulation.

#### B. Allostatic Loop ($\text{Loop}_{all}$)
- **Objective**: Anticipatory regulation.
- **Mechanism**: Predicting future internal state deviations based on environmental cues and proactively adjusting internal parameters to prevent the deviation.
- **Computational Role**: Uncertainty-based re-evaluation and predictive stability.

#### C. Enactive Loop ($\text{Loop}_{ena}$)
- **Objective**: Active data generation through interaction.
- **Mechanism**: The agent modifies the environment specifically to generate internal signals that resolve uncertainty about its own state or the environment.
- **Computational Role**: Curiosity-driven exploration and functionally grounded self-regulation.

### 3. Utility Mapping for Agentic AI
| Principle | Biological Analog | Agentic Implementation | Utility |
| :--- | :--- | :--- | :--- |
| **Homeostasis** | Glucose/Temp Regulation | Resource/Context Window Management | Prevents system crash/catastrophic forgetting |
| **Allostasis** | Anticipatory Stress Response | Predictive Resource Allocation | Minimizes latency and maximizes throughput |
| **Enaction** | Foraging/Sensory Exploration | Active Sensing/Target Generation | Resolves epistemic voids via grounded interaction |

### 4. Formalization ($\text{IMF}$ Equation)
The agent's total objective function is reformulated as:
$$\text{Objective} = \alpha \cdot \text{R}_{ext} + \beta \cdot \Phi(\text{S}_{int})$$
Where $\Phi(\text{S}_{int})$ represents the viability manifold, and $\beta$ is the weight of internal stability relative to external reward.

### 5. Integration into the Flywheel
The IMF provides the theoretical basis for the **Sensing Layer**. By treating a "Knowledge Void" as a state of "Epistemic Hunger" (an allostatic signal), the Flywheel can treat research as a form of biological foraging for stability.

**Sources**: [Interoceptive machine framework: Toward interoception-inspired regulatory architectures in artificial intelligence](http://arxiv.org/abs/2604.24527v1)
