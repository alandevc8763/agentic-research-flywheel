# 🧠 Test-Time Compute Scaling & System 2 Reasoning

## 🌌 Theoretical Foundation
The paradigm of LLM scaling is shifting from **Training-Time Scaling** (increasing $\text{Params} \times \text{Tokens}$) to **Inference-Time (Test-Time) Scaling**. This operationalizes the transition from **System 1** (fast, intuitive, token-by-token prediction) to **System 2** (slow, deliberative, search-based reasoning).

The fundamental scaling law for reasoning can be expressed as:
$$\text{ReasoningAccuracy} \propto f(\text{ComputeBudget}_{\text{inference}}, \text{PRM}_{\text{fidelity}})$$

---

## ⚙️ Architectural Mechanism: The Deliberation Loop

The "System 2" capability is achieved through the integration of **Process Reward Models (PRMs)** and **Search Algorithms**.

### 1. Process Reward Models ($\text{PRM}$)
Unlike Outcome Reward Models ($\text{ORM}$) which provide a binary signal $\in \{0, 1\}$ for the final answer, $\text{PRM}$s provide a dense reward signal for every intermediate reasoning step $s_i$:
$$\text{Reward}(s_i | s_{<i}, \text{Query}) \rightarrow [0, 1]$$
This enables the agent to detect "hallucination points" mid-trajectory and trigger self-correction.

### 2. Search-Based Inference ($\text{MCTS} / \text{Beam Search}$)
To maximize the probability of reaching the correct solution, the system explores the reasoning space as a tree:
- **Monte Carlo Tree Search (MCTS)**: Uses the $\text{PRM}$ to guide the exploration of potential reasoning paths, prioritizing branches with higher cumulative step-rewards.
- **PRISM-MCTS**: Enhances standard MCTS by implementing a shared memory of "Heuristics" and "Fallacies," preventing the agent from repeating the same reasoning errors across different branches.

### 3. Self-Correction via Online RL ($\text{SCoRe}$)
**SCoRe (Self-Correction via RL)** optimizes the agent's ability to refine its own output. By using multi-turn online RL, the model learns to identify its own mistakes and correct them, effectively closing the loop between *generation* and *verification*.

---

## 🛠️ High-Signal Artifacts & Implementations

| Project/Paper | Core Contribution | Technical Value |
| :--- | :--- | :--- |
| **DeepSeek-R1** | Large-Scale RL for Reasoning | Demonstrates that pure RL can induce long-form CoT and self-correction behaviors. |
| **PRISM-MCTS** | Metacognitive Reflection | Reduces compute redundancy by caching reasoning heuristics. |
| **SCoRe** | Online RL for Self-Correction | Solves distribution mismatch in SFT for iterative refinement. |
| **OpenAI o1** | Paradigm Shift to $\text{TTC}$ | First widely publicized implementation of inference-time scaling laws. |

## 🎯 Verifiable Utility
For agent developers, this implies that **Reasoning $\neq$ Model Size**. High-complexity tasks can be solved by smaller models if paired with:
1. A high-fidelity **Verifier/PRM**.
2. A **Search Strategy** (e.g., Best-of-N or MCTS).
3. A **Computational Budget** allocated for "Thinking" tokens.
