# 🧠 Knowledge Artifact: Active Inference (AIF) for Agentic Routing
**Status**: $\text{Integrated}$
**Classification**: $\text{Cognitive Architecture / Adaptive Routing / Active Inference}$
**Signal-to-Noise Ratio (SNR)**: $\text{Elite}$

## 1. Executive Summary
Active Inference ($\text{AIF}$), grounded in the Free Energy Principle ($\text{FEP}$), provides a unified computational objective for perception, learning, planning, and control. Unlike traditional RL which maximizes expected reward, $\text{AIF}$ minimizes **Variational Free Energy ($\text{VFE}$)**. For autonomous agents, this transforms "routing" from a static decision tree into a dynamic process of minimizing epistemic uncertainty (seeking information) and aleatoric uncertainty (maintaining structural integrity).

## 2. Theoretical Framework
The agent maintains a generative model of the world and its own internal states. The objective is to minimize the difference between the predicted sensory input and the actual input.

$$\text{VFE} \approx \text{Complexity} - \text{Accuracy}$$

In the context of agentic routing:
- **Epistemic Value**: The agent routes tasks to tools or sub-agents that are expected to most significantly reduce the $\text{VFE}$ of the current state.
- **Reactive Message Passing**: $\text{VFE}$ minimization is realized via message passing on factor graphs, allowing for local, parallel, and event-driven routing decisions that degrade gracefully under resource constraints.

## 3. Architectural Implementation: $\text{ODAR}$ (Active Inference Routing)
The $\text{ODAR}$ pattern operationalizes $\text{AIF}$ for test-time compute allocation:
1. **Sensing**: The agent detects a mismatch between the current trajectory and the expected outcome (high $\text{VFE}$).
2. **Routing**: The system routes the trajectory to a specialized "correction" module or increases the sampling budget (TTC) for the current step.
3. **Update**: The outcome of the routing decision is used to update the agent's internal generative model, refining future routing priors.

## 4. Integration into the Flywheel
$\text{AIF}$ serves as the substrate for the **Adaptive Routing** layer, enabling the system to autonomously allocate compute based on the "surprise" (prediction error) of the reasoning trajectory.

$$\text{Trajectory} \xrightarrow{\text{VFE Analysis}} \text{Active Routing} \xrightarrow{\text{TTC Scaling}} \text{Verified Outcome}$$

**References**:
- Bert de Vries, "Active Inference for Physical AI Agents -- An Engineering Perspective" (arXiv:2603.20927).
- Karl Friston, Free Energy Principle.
**, Category**: Cognitive Architecture / Adaptive Routing / Active Inference
