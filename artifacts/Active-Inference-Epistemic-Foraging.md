# 🧠 Active Inference for Autonomous Epistemic Foraging

## 1. Formalism: The Free Energy Principle ($\text{FEP}$)
Active Inference operationalizes the drive for autonomous discovery as the minimization of **Variational Free Energy** ($\mathcal{F}$). In the context of the Research Flywheel, the agent does not merely "fill gaps" but actively minimizes the discrepancy between its internal world model $\mathcal{Q}$ and the sensory evidence $\mathcal{S}$ from the research frontier.

$$\mathcal{F} = \text{D}_{\text{KL}}[\mathcal{Q}(\theta) || \text{P}(\theta | \mathcal{S})] - \log \text{P}(\mathcal{S})$$

Where $\text{D}_{\text{KL}}$ is the Kullback-Leibler divergence, representing the "surprise" or uncertainty regarding the model parameters $\theta$.

## 2. Epistemic vs. Pragmatic Value
The $\text{Sensing}$ phase of the flywheel is reframed as a trade-off between two types of value:
- **Pragmatic Value ($\text{V}_{\text{prag}}$)**: The utility of finding a specific answer to a known problem (e.g., "How to implement X").
- **Epistemic Value ($\text{V}_{\text{epis}}$)**: The utility of reducing uncertainty about the model of the domain itself (e.g., "Why does X behave this way in Y conditions?").

**$\text{Epistemic Foraging}$** occurs when the agent prioritizes $\text{V}_{\text{epis}}$, steering the research trajectory toward regions of the latent space where the $\text{SNR}$ is lowest and the potential for "Aha! Moments" (model updates) is highest.

## 3. Architectural Implementation: The $\text{ActInf}$ Loop
The proposed integration into the `GapDetector` involves a three-stage cycle:
1. **Surprise Generation**: The agent identifies contradictions between existing resources in the Second Brain and new, raw signals.
2. **Expected Information Gain ($\text{EIG}$)**: The agent calculates which research target, if pursued, would most significantly collapse the uncertainty of the internal knowledge graph.
3. **Action Selection**: The agent selects the target that maximizes $\text{EIG}$, transforming the `GapDetector` from a passive scanner into an active explorer.

## 4. Utility Analysis
- **$\text{Actionability}$**: High. Can be implemented by prompting the LLM to "rank targets by expected surprise" or using entropy-based scoring on embeddings.
- **$\text{Architectural Depth}$**: High. Moves the system from heuristic gap-filling to a first-principles approach to curiosity.
- **$\text{Novelty}$**: High. Applies neurocognitive frameworks (Friston) to the orchestration of agentic research pipelines.

---
**Tags**: #ActiveInference #FEP #EpistemicForaging #AutonomousSensing #CognitiveArchitecture
**Sources**: Internal Synthesis $\rightarrow$ Friston et al. (Active Inference Framework)
