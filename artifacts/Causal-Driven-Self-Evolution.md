# Knowledge Artifact: Causal-Driven Agentic Self-Evolution ($\text{CD-ASE}$)

## $\text{Architectural Overview}$
$\text{CD-ASE}$ is a framework for transforming agentic self-improvement from heuristic-based reflection to **causal-driven evolution**. Instead of treating the agent's behavior as a black-box sequence of tokens, $\text{CD-ASE}$ models the agent's operational logic as a **Causal Program Graph ($\text{CPG}$)**—a directed hypergraph where nodes are procedural primitives and edges represent causal dependencies.

The core objective is to transition from $\text{Correlation-based Learning}$ (SFT/PPO) to $\text{Causal-based Discovery}$, allowing the agent to understand *why* a specific trajectory succeeded or failed via counterfactual interventions.

## $\text{Key Mechanisms}$

### 1. Counterfactual Probing for Causal Discovery ($\text{CAMO}$)
To avoid the "spurious correlation" trap in self-reflection, the system employs **Counterfactual Probing**.
- **Mechanism**: The agent generates multiple trajectories for a task. It then applies targeted perturbations (micro-behaviors) to the state or action sequence.
- **Causal Attribution**: If a perturbation $\Delta a$ in action $a$ leads to a change in outcome $\Delta o$, the system assigns a causal weight to $a \rightarrow o$.
- **Result**: The agent identifies the "Causal Drivers" of its emergent behavior, distinguishing between necessary steps and coincidental noise.

### 2. World Modeling via Causal Program Graphs ($\text{CPG}$)
The discovered causal drivers are integrated into a $\text{CPG}$.
- **Structure**: A directed hypergraph where nodes are **SGA Atoms** (State-Goal-Action primitives).
- **Compositional Generalization**: By representing logic as a graph of causal programs, the agent can perform **Structural Analogies**. If a Causal Program $\mathcal{P}_1$ solved Task $A$, and Task $B$ shares the same causal topology, the agent can transplant $\mathcal{P}_1$ to Task $B$ regardless of the surface-level lexical difference.
- **Deduction-Abduction Cycle**: The agent *deduces* plans from the $\text{CPG}$ and *abductively* expands the graph when a failure occurs that cannot be explained by the current causal model.

### 3. Amortized Causal Reasoning ($\text{SGA-MCTS}$)
To reduce the computational cost of causal discovery at runtime, the system uses **SGA Distillation**.
- **Offline Search**: Use MCTS to find high-fidelity causal trajectories.
- **De-lexicalization**: Transform trajectories into "SGA Atoms"—symbolic slots that capture the underlying causal logic.
- **Execution**: At inference time, the agent performs a fast look-up of the relevant SGA Atom rather than re-running the full causal search.

## $\text{The Evolutionary Loop}$
$$\text{Experience} \xrightarrow{\text{Counterfactual Probing}} \text{Causal Drivers} \xrightarrow{\text{CPG Integration}} \text{Refined World Model} \xrightarrow{\text{SGA Distillation}} \text{Amortized Policy}$$

## $\text{Actionability}$
- **Implementation**: Integrate a `CausalProbe` module that automatically perturbs successful trajectories to verify causal necessity.
- **Storage**: Replace flat memory buffers with a `GraphRAG` backed Causal Program Graph.
- **Metric**: Track **Causal Fidelity** ($\text{CF}$) — the percentage of predicted outcome changes that occur when the CPG-suggested perturbations are applied.

## $\text{Sources}$
- [arXiv:2604.14691v1](https://arxiv.org/abs/2604.14691v1) - CAMO: Automated Causal Discovery from Micro Behaviors.
- [arXiv:2604.26522v1](https://arxiv.org/abs/2604.26522v1) - AGEL-Comp: Neuro-Symbolic Framework for Compositional Generalization.
- [Internal Artifact](~/ai-second-brain/wiki/articles/sga-mcts.md) - SGA-MCTS: Amortized Causal Logic.
