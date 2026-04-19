# Active Epistemic Control (AEC): Verified Planning via Epistemic Separation

**Category**: Agentic Planning / Epistemic Logic
**Tags**: `verified-planning`, `epistemic-control`, `belief-management`, `categorical-feasibility`, `active-sensing`
**Source**: arXiv:2602.03974

## 📌 Executive Summary
$\text{Active Epistemic Control}$ (AEC) is an epistemic-categorical planning framework designed to solve the "silent failure" problem in LLM agents where predicted world-state facts (beliefs) are mistaken for grounded truths, leading to infeasible commitments. AEC introduces a rigorous architectural decoupling between **Belief** (probabilistic prediction) and **Fact** (grounded verification), ensuring that while beliefs guide efficiency, only facts certify execution.

## 🛠 Technical Architecture: The Epistemic Split ($\mathcal{E}_{split}$)

### 1. Dual-Store Memory Architecture
AEC replaces a monolithic state representation with two distinct stores:
- **Grounded Fact Store ($\mathcal{S}_{fact}$)**: Contains only predicates verified through direct environmental interaction or authoritative sensors. This store is the sole source of truth for **commitment**.
- **Belief Store ($\mathcal{S}_{belief}$)**: Contains predictions from a learned world model. This store is used exclusively for **pruning** the search space of candidate plans.

### 2. The Verification Gate ($\mathcal{G}_{verify}$)
To transition from a candidate plan (based on $\mathcal{S}_{belief}$) to an executed action, AEC applies a two-stage gate:
1. **Grounded Precondition Coverage**: Every action's required preconditions must be present in $\mathcal{S}_{fact}$.
2. **SQ-BCP Pullback Compatibility**: A categorical check ensuring that the predicted state transition is compatible with the grounded constraints of the environment.

$$\text{Commitment} \iff (\text{Precond} \subseteq \mathcal{S}_{fact}) \land (\text{Plan} \in \text{Pullback}(\mathcal{B}_{model}, \mathcal{S}_{fact}))$$

### 3. Active Epistemic Loop
The agent dynamically chooses between two modes of operation based on an uncertainty threshold $\tau$:
- **Sensing Mode ($\text{Query} \rightarrow \mathcal{S}_{fact}$)**: If uncertainty in a critical predicate is high, the agent prioritizes an observation action to move the predicate from $\mathcal{S}_{belief} \rightarrow \mathcal{S}_{fact}$.
- **Pruning Mode ($\text{Simulate} \rightarrow \text{Filter}$)**: If confidence is sufficient, the agent uses the belief store to discard infeasible trajectories without querying the environment.

## 💎 Value Analysis
The integration of $\text{AEC}$ into an autonomous agent provides:
1. **Zero-Infeasible Commitment**: By gating commitments on $\mathcal{S}_{fact}$, the agent never attempts an action based on a hallucinated precondition.
2. **Query Efficiency**: By using $\mathcal{S}_{belief}$ for pruning, the agent minimizes costly environmental interactions (e.g., "opening every drawer" to find an object).
3. **Robustness to Model Drift**: Since beliefs only affect efficiency, errors in the learned world model do not cause catastrophic failures, only temporary efficiency losses.

---
**Synergy**: AEC provides the formal "Sensing" logic required for Epoch 1 of the Research Flywheel, transforming the `GapDetector` from a semantic search tool into an active epistemic controller that knows *when* to research based on belief uncertainty.
