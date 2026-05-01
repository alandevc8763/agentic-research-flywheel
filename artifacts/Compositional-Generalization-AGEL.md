# Knowledge Artifact: Neuro-Symbolic Compositional Generalization ($\text{NS-CG}$)

## $\text{Architectural Overview}$
$\text{NS-CG}$ addresses the fundamental "Generalization Gap" in agentic systems: the inability to apply learned procedural knowledge to out-of-distribution ($\text{OOD}$) tasks that share structural logic but differ in surface-level lexical or environmental features. 

While traditional RL and SFT rely on **pattern matching** (correlation), $\text{NS-CG}$ (exemplified by the $\text{AGEL-Comp}$ framework) implements **Structural Isomorphism**—treating agent trajectories as compositional programs that can be decomposed into symbolic primitives and recomposed via topological mapping.

---

## $\text{Key Mechanisms}$

### 1. Symbolic Primitive Decomposition ($\text{SPD}$)
Instead of treating a trajectory as a sequence of tokens, $\text{NS-CG}$ decomposes it into a set of $\mathcal{P}$ (Primitives):
$$\mathcal{T} = \{p_1, p_2, \dots, p_n\} \mid p_i \in \text{Symbolic Library } \mathcal{L}$$
- **Mechanism**: A "Decomposition Layer" maps neural activations to symbolic operators (e.g., `Find(object)`, `Transform(state)`, `Verify(condition)`).
- **Benefit**: This removes the "lexical noise" of the environment, allowing the agent to recognize that "Opening a door with a key" and "Unlocking a file with a password" share the same $\text{SGA}$ (State-Goal-Action) topology.

### 2. Topological Mapping & Structural Analogy
To solve a new task $\mathcal{T}_{new}$, the system performs a **Graph Isomorphism Search** against its library of solved trajectories:
1. **Subgraph Extraction**: Extracts the dependency graph $\mathcal{G}_{new}$ of the target task.
2. **Analogy Matching**: Finds a solved graph $\mathcal{G}_{solved}$ such that there exists a mapping $\phi: \mathcal{G}_{new} \rightarrow \mathcal{G}_{solved}$ that preserves causal edges.
3. **Primitive Transplantation**: Replaces the symbolic primitives of the solved task with the specific entities of the new task.

### 3. The Neuro-Symbolic Feedback Loop ($\text{NS-Loop}$)
The system maintains a dual-process architecture:
- **System 1 (Neural)**: Proposes a candidate trajectory $\hat{\mathcal{T}}$ based on intuitive pattern matching.
- **System 2 (Symbolic)**: Validates $\hat{\mathcal{T}}$ against the $\text{CPG}$ (Causal Program Graph) constraints. If a violation is detected, the symbolic engine generates a **Counterfactual Constraint** $\mathcal{C}$ which is used to refine the Neural proposer.

---

## $\text{The Compositional Flywheel}$
$$\text{Trajectory} \xrightarrow{\text{SPD}} \text{Symbolic Primitive} \xrightarrow{\text{Topological Map}} \text{Structural Analogy} \xrightarrow{\text{Transplantation}} \text{OOD Generalization}$$

## $\text{Actionability}$
- **Implementation**: Deploy a `SymbolicMapper` module that converts LLM-generated plans into Directed Acyclic Graphs (DAGs) of primitives.
- **Evaluation**: Measure **Generalization Efficiency** ($\text{GE}$) as the ratio of OOD success rate to the number of training examples required.
- **Metric**: $\text{Compositional Gain} = \frac{\text{Success}(\text{NS-CG})}{\text{Success}(\text{Pure-Neural})}$.

## $\text{Sources}$
- [arXiv:2604.26522v1](https://arxiv.org/abs/2604.26522v1) - AGEL-Comp: Neuro-Symbolic Framework for Compositional Generalization.
- [Internal Artifact](~/hermes-projects/research-flywheel/artifacts/Causal-Driven-Self-Evolution.md) - $\text{CD-ASE}$ framework.
