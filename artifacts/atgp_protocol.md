# 🌌 Protocol: Autonomous Target Generation ($\text{ATGP}$)

## 1. Executive Summary
The $\text{Autonomous Target Generation Protocol (ATGP)}$ is the cognitive bridge between **Sensing** (detecting a void) and **Hunting** (executing a trajectory). It transforms raw signals from Semantic Void Analysis and Dependency Mapping into actionable $\text{ResearchTargets}$ $\tau$.

The goal is to maximize the **Frontier Expansion Rate** ($\text{FER}$) of the Second Brain by ensuring that research energy is allocated to targets with the highest theoretical utility.

---

## 2. Formal Framework

### 2.1 Target Definition
A $\text{ResearchTarget}$ $\tau$ is defined as a tuple:
$$\tau = \{ q, \mathcal{C}, P, \mathcal{R} \}$$
Where:
- $q$: The optimized search query.
- $\mathcal{C}$: The contextual anchor (existing nodes in the Knowledge Graph).
- $P$: The priority score $\in [0, 1]$.
- $\mathcal{R}$: The rationale (the "Why" derived from the void analysis).

### 2.2 The Priority Function
The priority $P$ of a target is calculated via a weighted linear combination of three primary signals:

$$\text{Priority}(\tau) = \sigma \left( \omega_v \cdot \Phi_{\text{void}} + \omega_d \cdot \Phi_{\text{dep}} + \omega_c \cdot \Phi_{\text{cur}} \right)$$

Where:
- $\Phi_{\text{void}}$ (**Semantic Void Magnitude**): The distance from the centroid of the nearest known cluster in embedding space.
- $\Phi_{\text{dep}}$ (**Dependency Centrality**): The number of existing high-value nodes that reference the missing concept.
- $\Phi_{\text{cur}}$ (**Curiosity Score**): Derived from the $\text{AgentEvolver}$ self-questioning loop (Novelty $\times$ Potential Actionability).
- $\sigma$: Sigmoid normalization function.
- $\omega$: Weights tuned for the current Epoch.

---

## 3. Operational Workflow

### Phase I: Signal Synthesis (Detection $\rightarrow$ Candidate)
1. **Void Extraction**: Identify regions in the latent space with $\text{density} < \epsilon$.
2. **Node Grafting**: Identify "dangling" references (Entity $\text{A} \xrightarrow{\text{ref}} \text{Entity B}$ where $\text{B}$ is undefined).
3. **Candidate Generation**: Use a "Bridge-LLM" to propose a concept that would resolve the void or the dangling reference.

### Phase II: Query Formulation (Candidate $\rightarrow$ Target)
The system applies a **Multi-Perspective Query Expansion** to $q$:
- **Technical Perspective**: "Implementation details of [Concept]..."
- **Theoretical Perspective**: "First principles and mathematical foundations of [Concept]..."
- **Comparative Perspective**: "Difference between [Concept] and [Existing Alternative]..."

### Phase III: Utility Scoring (The Alchemist's Filter)
Each $\tau$ is scored by the Distillation Engine:
| Metric | Definition | Scoring Logic |
| :--- | :--- | :--- |
| $\text{Actionability}$ | $\text{Can this be converted to code/tool?}$ | $\text{Binary (0/1)}$ |
| $\text{Depth}$ | $\text{Does it target a 'How' rather than a 'What'?}$ | $\text{Scale 1-5}$ |
| $\text{Novelty}$ | $\text{Is it absent from the top-10 curated resources?}$ | $\text{Scale 1-5}$ |

---

## 4. Integration into the Flywheel
The $\text{ATGP}$ closes the loop in Epoch 1 by automating the $\text{Sensing} \rightarrow \text{Hunting}$ transition:

$$\text{Sensing} \xrightarrow{\text{ATGP}} \text{Hunting} \xrightarrow{\text{Alchemy}} \text{Integration} \xrightarrow{\text{Sensing}} \dots$$

By treating "curiosity" as a differentiable signal ($\Phi_{\text{cur}}$), the Flywheel evolves from a passive librarian into an active explorer.

**Tags**: #AgenticAI #ResearchFlywheel #AutonomousSensing #CognitiveArchitecture
**Sources**: $\text{AgentEvolver}$, $\text{SRA Framework}$, $\text{DESIGN.md}$
