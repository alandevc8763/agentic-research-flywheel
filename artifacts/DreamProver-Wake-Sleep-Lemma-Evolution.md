# $\text{DreamProver}$: Evolving Transferable Lemma Libraries via Wake-Sleep Program Induction

## 📌 Overview
$\text{DreamProver}$ operationalizes a "wake-sleep" program induction paradigm to autonomously discover and evolve reusable lemmas for formal theorem proving. It addresses the fundamental trade-off in automated theorem proving: fixed libraries are too rigid, while problem-specific synthesized lemmas lack the generality required for transfer to unseen domains.

By mimicking human cognitive cycles of experience acquisition (wake) and conceptual abstraction (sleep), $\text{DreamProver}$ evolves a compact, high-utility lemma library that substantially improves proof success rates and reduces computational overhead in $\text{Lean}$.

---

## 📐 Architectural Depth

### 1. The Wake Stage: Experience Acquisition
The wake stage is the exploration phase where the system interacts with the environment (the theorem prover) to discover "learnable" signals.

- **Learnable Theorem Identification**: A theorem is flagged as learnable if the system can prove it using the current library $\mathcal{L}$ within a predefined compute budget (max attempts/corrections). These theorems serve as the raw material for abstraction.
- **Recursive Theorem Decomposition**: For theorems that remain intractable, $\text{DreamProver}$ employs a recursive decomposition strategy:
  $$\text{Target Theorem} \rightarrow \text{Proof Sketch} \rightarrow \text{Intermediate Goals (sorted by 'sorry' tactics)} \rightarrow \text{Extracted Theorems}$$
- **Consistency Verification**: To ensure the extracted intermediate theorems are valid, the system attempts to reassemble the full proof. If the target theorem is provable using the extracted components, the decomposition is validated.

### 2. The Sleep Stage: Lemma Evolution & Optimization
The sleep stage transforms specific experiences into generalizable knowledge.

- **Cluster-Based Lemma Abstraction**:
  1. **Annotation**: Each learnable theorem is annotated with an LLM-generated NL description (sub-domain, difficulty, dependency).
  2. **Semantic Clustering**: Descriptions are embedded via sentence transformers and grouped using K-Means (cluster count determined by the elbow method).
  3. **Candidate Synthesis**: An LLM synthesizes a candidate lemma for each cluster designed to be a "generalization" of the member theorems.
  4. **Structural Validation**: Candidate lemmas are filtered using a structural similarity metric based on first-order logic expression trees.

- **Library Refinement Loop**:
  - **Forgetting Mechanism**: Implements a Least-Recently-Used (LRU) strategy to prune unused lemmas, keeping the library size $< 100$ to prevent context bloat and maintain stability.
  - **Deduplication**: Utilizes **Tree Edit Distance** to measure the cost of transforming one expression tree to another, ensuring that new lemmas provide novel utility.
  - **Formal Verification**: Every candidate lemma must be formally proved by the system before being committed to $\mathcal{L}$.

### 3. Inference Pipeline
$\text{DreamProver}$ utilizes a tiered inference strategy to maximize efficiency:
$$\text{Direct Prompting} (\text{with } \mathcal{L}) \xrightarrow{\text{fail}} \text{Sketch-and-Prove Workflow} (\text{with } \mathcal{L})$$

---

## 🚀 Impact on Agentic Flywheels

$\text{DreamProver}$ provides a high-fidelity blueprint for **Experience-Driven Tool Synthesis**. While most agents use tools as static capabilities, $\text{DreamProver}$ treats "skills" (lemmas) as evolving artifacts.

- **From Task-Solving to Knowledge-Building**: It shifts the agent's objective from $\text{solve}(T)$ to $\text{evolve}(\mathcal{L} \mid T)$.
- **Compression of Reasoning**: By consolidating redundant experiences into a single, powerful lemma, the agent reduces the token-cost of future reasoning paths.
- **Self-Correcting Knowledge Base**: The integration of formal verification in the sleep stage ensures that the evolved knowledge base is an "Immutable Ground Truth," eliminating the risk of hallucinated "skills."

**Reference**: [arXiv:2604.26311](https://arxiv.org/abs/2604.26311)
**Category**: Certified Synthesis / Formal Verification / Lemma Evolution / Wake-Sleep Paradigm
