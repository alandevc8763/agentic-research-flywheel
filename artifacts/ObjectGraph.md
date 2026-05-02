# 🕸️ ObjectGraph: From Document Injection to Knowledge Traversal

**Source**: [arXiv:2604.27820](https://arxiv.org/abs/2604.27820) | **Date**: 2026-04-30 | **Status**: $\text{Integrated}$

## 1. The Document Consumption Problem ($\text{DCP}$)

Current agentic systems rely on the **Full-Read Assumption**: to retrieve any semantic unit from a document $\mathcal{D}$ of $n$ tokens, the agent must ingest $\Omega(n)$ tokens. This leads to three critical failure modes:

1. **Token Inflation**: Average utilization rate $\bar{\mathcal{U}} \approx 6.3\%$, meaning $\sim 93.7\%$ of context is waste.
2. **Context Compounding**: In multi-turn loops, stateless APIs force the re-transmission of the full document, leading to super-linear growth of $C_{\text{total}}$ relative to turn count $T$.
3. **Role Blindness**: Inability to serve different views of the same document to Orchestrator vs. Worker agents without external middleware.

## 2. The ObjectGraph ($\text{.og}$) Specification

ObjectGraph reconceives the document as a typed, directed knowledge graph $\mathcal{G} = (V, E, \lambda, \rho)$ where:
- $V$: Set of nodes (atomic semantic units).
- $E$: Typed dependency edges (e.g., `:requires`, `:precedes`).
- $\lambda$: Edge labeling function.
- $\rho$: Scope function mapping nodes to access roles $\mathcal{S}$ (e.g., $\text{all}, \text{orchestrator}, \text{worker}$).

### 2.1 Progressive Disclosure Model ($\text{PDM}$)
ObjectGraph eliminates inflation via a three-pass reading depth:
- **Pass 1 (Index)**: $\sim 30$ tokens. Read `::meta` and `::index` to determine relevance.
- **Pass 2 (Dense)**: $\sim 12$ tokens/node. Read `::dense` blocks for routing and planning.
- **Pass 3 (Full)**: $\sim 180$ tokens/node. Read `::full`, `::code`, and `::steps` for execution.

$$\text{Savings}(\tau) = 1 - \frac{C_{\text{index}} + |M(\tau)| \cdot \bar{c}_d + |F(\tau)| \cdot \bar{c}_f}{n}$$

### 2.2 The LLM-Native Query Protocol
The interaction is reduced to two primitives:
1. $\text{search\_index}(f, q, r) \rightarrow$ returns node IDs matching query $q$ for role $r$.
2. $\text{resolve\_context}(f, N) \rightarrow$ returns full content of nodes $N$ plus all `:requires` dependencies.

## 3. Advanced Primitives

- **Role-Scoped Access**: Content is filtered at the format level. A Worker agent never discovers the existence of Orchestrator-only nodes.
- **Executable Assertion Nodes**: Encodes validation logic directly in the document:
  $$\text{Trigger} \rightarrow \text{Check}(\text{cmd}) \rightarrow \text{on-pass}(\text{proceed}) \mid \text{on-fail}(\text{retry/escalate})$$
- **Delta Loading**: The `::changelog` meta-node allows agents to fetch only $\Delta$ nodes between versions $v_1$ and $v_2$, reducing update cost from $O(n)$ to $O(\mu \cdot \bar{c}_f)$.

## 4. Empirical Impact

| Metric | Markdown (Baseline) | ObjectGraph (Arch B) | $\Delta$ |
| :--- | :--- | :--- | :--- |
| **Token Consumption** | $2,340$ tokens | $187$ tokens | $-92.0\%$ |
| **Context Compounding** | Super-linear | Near-linear | $36.5\times$ reduction |
| **Task Accuracy** | $76.0\%$ | $90.8\%$ | $+14.8\%$ |

**Key Insight**: The accuracy gain is attributed to the reduction of **Attention Dilution**. By removing irrelevant "noise" tokens, the model's focus on the core task signal is maximized.

---
**Tags**: #Agentic-Memory #Token-Efficiency #Knowledge-Traversal #ObjectGraph #Context-Optimization
