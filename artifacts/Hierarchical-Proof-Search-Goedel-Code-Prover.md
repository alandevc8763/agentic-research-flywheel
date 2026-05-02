# 🛠️ Hierarchical Proof Search: Gödel-Code-Prover

## 🎯 Executive Summary
**Gödel-Code-Prover** introduces a hierarchical proof search framework for automated code verification in $\text{Lean 4}$. It addresses the "ungrounded decomposition" problem in program verification by replacing flat tactic generation with a structured **Planning-and-Proving** loop. By optimizing a continuous **Decomposition Score** ($S$), an 8B-parameter model achieves $\approx 2.6\times$ the success rate of baselines, including neural provers up to $84\times$ larger.

---

## 🧬 Architectural Core: The Decomposition Score $S$

The fundamental contribution is the transformation of the discrete "proof accepted/rejected" signal into a dense, continuous reward for the planning phase.

### 1. Constructive Justification ($v$)
A decomposition is valid if and only if:
- **Proof Reconstruction**: The proposed lemmas $\mathcal{L} = \{L_1, \dots, L_k\}$ logically entail the parent theorem $G$.
- **Semantic Filtering ($\text{QuickCheck}$)**: Every $L_i$ must survive automated counterexample search.
$$v(\mathcal{L}; G) = \mathbb{1}_{\text{proof}}(\mathcal{L}; G) \cdot \prod_{i=1}^k \mathbb{1}_{\text{qc}}(L_i)$$

### 2. Decomposition Effectiveness ($r$)
Difficulty is quantified via the **Operator Footprint** $d(G)$, the total count of logical and program operators in the AST. Effectiveness is the reduction in the "hardest" subgoal, smoothed via $\text{LogSumExp}$:
$$\bar{d}(\mathcal{L}) = T \cdot \log \sum_{i=1}^k \exp(d(L_i)/T)$$
$$r(\mathcal{L}; G) = \max\left(1 - \frac{\bar{d}(\mathcal{L})}{d(G)}, 0\right)$$

### 3. Unified Objective
The final score $S = r \cdot v$ serves as both the **GRPO training reward** and the **inference-time ranking criterion**, ensuring strict alignment.

---

## ⚙️ Execution Pipeline

### Phase I: Recursive Lemma Decomposition
1. **Target Selection**: Select the goal $g \in \mathcal{O}$ with the highest $d(g)$.
2. **Rollout**: $\pi$ proposes a decomposition $\mathcal{L}$.
3. **Verification**: Filter via $v$ (Proof Recon + QuickCheck).
4. **Update**: Replace $g$ with $\mathcal{L}$ in the open goal set $\mathcal{O}$.

### Phase II: Iterative Lemma Completion
1. **Tactic Generation**: $\pi$ generates proof candidates for leaf lemmas.
2. **Compiler Feedback**: Lean 4 diagnostics $\rightarrow$ $\pi$ $\rightarrow$ Refined Proof.
3. **Termination**: Success when all $\mathcal{L}$ are discharged.

---

## 📈 Key Findings & Scaling Laws

- **Compound Domain Shift**: Code verification is harder than math because of **Concept Proliferation** (every program is a new universe) and **Tactic Distribution Shift** (reliance on `grind`, `native_decide` vs algebraic tactics).
- **Inference-Time Scaling**: Proving success rates improve monotonically with search iterations and sampling budget. Unlike flat sampling, hierarchical search does not plateau rapidly, indicating unsaturated scaling potential.
- **Efficiency**: The 8B model's hierarchical approach outperforms massive 671B provers, proving that **architectural priors (hierarchy) $\gg$ raw parameter count**.

---

## 🛠️ Implementation Notes for Agentic Integration
- **Sensing Application**: Use $d(G)$ as a heuristic for "Knowledge Void" depth in formal repositories.
- **Verification Loop**: Integrate `QuickCheck` as a low-cost "Sensing" gate before committing compute to deep reasoning trajectories.
- **Reward Shaping**: Apply the $S = r \cdot v$ pattern to other domain-specific decomposition tasks (e.g., complex SRE root-cause analysis).

**Source**: Li et al., *"Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification"* (arXiv:2603.19329)
**Tags**: #FormalVerification #Lean4 #InferenceScaling #HierarchicalReasoning #RLVR