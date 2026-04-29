# 💎 Knowledge Artifact: ProofBridge

**Source**: [arXiv:2510.15681](https://arxiv.org/pdf/2510.15681v3)
**Status**: $\text{SOTA Specification}$
**Utility Score**: $\text{Actionability: 8/10} \mid \text{Depth: 9/10} \mid \text{Novelty: 9/10}$

---

## 🌌 Conceptual Framework
$\text{ProofBridge}$ operationalizes the auto-formalization of natural language (NL) theorems and proofs into formal languages (FL), specifically Lean 4. Unlike previous efforts that either focused on theorem-only translation or FL proof synthesis from FL theorems, ProofBridge provides a unified framework for translating entire NL theorem+proof pairs.

The core thesis is that proof auto-formalization can be treated as **learning from demonstrations**. By aligning NL and FL theorem+proof pairs in a shared semantic space, the system can retrieve high-fidelity formalization patterns to guide the LLM's translation process.

## 🏗️ Technical Architecture
The architecture consists of three primary layers:

### 1. Joint Embedding Layer ($\text{JEL}$)
The system maps $\text{MNL} = \langle \text{T}_{\text{NL}}, \text{P}_{\text{NL}} \rangle$ and $\text{M}_{\text{FL}} = \langle \text{T}_{\text{FL}}, \text{P}_{\text{FL}} \rangle$ into a shared embedding space $\mathbb{R}^d$ using modality-specific encoders.
- **NL Encoder**: Uses `all-MiniLM-L6-v2` projected to $d=512$.
- **FL Encoder**: Linearizes the DAG traversal of tactics from the Lean REPL, encodes states via `ByT5`, and mean-pools them into $\mathbb{R}^d$.
- **Alignment**: Trained via a symmetric contrastive loss $\mathcal{L}(B)$ to maximize cosine similarity between equivalent NL and FL pairs.

### 2. Retrieval-Augmented Translation ($\text{RAT}$)
The LLM (based on `Kimina-Prover-RL-1.7B`) is fine-tuned on a curated dataset ($\text{NuminaMath-Lean-PF}$) of 38.9k NL $\leftrightarrow$ Lean 4 pairs.
- **Conditioning**: The translation is conditioned on the top-K retrieved FL theorem+proof pairs $\mathcal{R}(\text{MNL}, \mathcal{D})$ and their relevance scores.
- **Goal**: Generate $\hat{	ext{M}}_{\text{FL}} = \langle \text{T}_{\text{eFL}}, \text{P}_{\text{eFL}} \rangle$ that satisfies both type correctness and semantic equivalence.

### 3. Iterative Proof Repair ($\text{IPR}$)
To handle the stochastic nature of LLMs, a verifier-guided loop is employed:
- **Syntactic Verification**: Lean's type-checker verifies $\text{P}_{\text{eFL}}$ proves $\text{T}_{\text{eFL}}$ with no open goals.
- **Semantic Verification**: An LLM-based judge verifies that $\text{T}_{\text{eFL}} \equiv \text{T}_{\text{NL}}$.
- **Repair**: If either fails, feedback is generated and the LLM attempts a repair (up to $R_{\max} = 5$ attempts).

## ⚙️ Operationalization
- **Dataset**: Use $\text{NuminaMath-Lean-PF}$ for SFT.
- **Verification**: Integration with `Lean REPL` is mandatory for the iterative repair loop.
- **Evaluation Metrics**:
    - $\text{TC (Type Correctness)}$: Percentage of proofs that pass the type-checker.
    - $\text{SC (Semantic Correctness)}$: Verified via bi-directional equivalence proofs.

## 🚀 Integration Strategy
ProofBridge fills a critical gap in the "Auto-Formalization" frontier. It moves the needle from "theorem translation" to "verifiable proof translation," providing a blueprint for autonomous AI-led research where hypotheses (NL) can be automatically transformed into verified formal theorems (FL).
