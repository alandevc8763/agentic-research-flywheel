# Curriculum-Driven RLVR Scaling

$\text{Curriculum-Driven RLVR Scaling}$ operationalizes the transition from naive reinforcement learning to structured cognitive growth via **Multi-Stage Curriculum Learning** within Verifiable Reward environments. It asserts that the $\text{SNR}$ of the gradient update is maximized when the model is exposed to a sequence of tasks with monotonically increasing cognitive complexity.

## 📐 Architectural Depth: The Progressive Scaling Pipeline

The core innovation is the replacement of monolithic RL training with a **Gated Progression Sequence**, where each stage acts as a prerequisite for the next:

$$\text{SFT Base} \xrightarrow{\text{Stage 0: Formal}} \text{SFT}^* \xrightarrow{\text{Stage 1: Discriminative}} \text{SFT}^{**} \xrightarrow{\text{Stage 2: Synthetic}} \text{SFT}^{***} \xrightarrow{\text{Stage 3: Relational}} \text{Production Model}$$

### 1. Complexity Hierarchy
- **Stage 0: Formal/Structural Discipline** (e.g., Bluebook Citation Formatting)
  - *Goal*: Master the "grammar" of the domain.
  - *Reward*: Deterministic string matching and format validation.
- **Stage 1: Discriminative Precision** (e.g., Holding Selection)
  - *Goal*: Accurate identification of core legal/technical truths.
  - *Reward*: Binary accuracy on multiple-choice ground truths.
- **Stage 2: Structured Synthesis** (e.g., IRAC Summarization)
  - *Goal*: Construct coherent, multi-step reasoning chains.
  - *Reward*: Hybrid scoring (Structure $\times$ Content $\times$ Legal Language).
- **Stage 3: Relational Mapping** (e.g., Case Entailment/Overruling)
  - *Goal*: High-level abstract synthesis across disparate entities.
  - *Reward*: Classification accuracy + Contextual consistency.

### 2. Progression Gating ($\text{PG}$)
Transitions between stages are governed by a **Reward Threshold $\theta$**:
$$\text{Transition}(\text{Stage}_n \rightarrow \text{Stage}_{n+1}) \iff \mathbb{E}[\text{Reward}(\text{Stage}_n)] \geq \theta_n \text{ and } \text{Var}(\text{Reward}) < \sigma_n$$
This prevents "catastrophic forgetting" and ensures the model does not attempt high-order synthesis before mastering basic structural discipline.

## 🚀 Impact on Agentic Flywheels
Integrating curriculum-driven RLVR allows the Flywheel to:
- **Bypass the "Reasoning Wall"**: Avoids the plateau effect seen in naive RL by providing a steady stream of achievable "wins" (reward signals).
- **Stable Trajectory Evolution**: Ensures that the base reasoning capabilities are grounded in deterministic truth before introducing complex, high-variance synthetic tasks.
- **Automatic Complexity Tuning**: The $\text{GapDetector}$ can identify which stage of the curriculum a specific knowledge void belongs to, triggering the appropriate training stage.

**Reference**: Based on `cap-rlvr` implementation for legal reasoning.
**Category**: RL / Curriculum Learning / Verifiable-Rewards / Scaling
