# 💠 CascadeDebate: Multi-Agent Deliberation for Cost-Aware LLM Cascades

## 📌 Abstract
$\text{CascadeDebate}$ optimizes the trade-off between accuracy and compute cost in LLM cascades by inserting a **Multi-Agent Deliberation (MAD)** layer at escalation boundaries. Instead of escalating uncertain queries directly to a larger, more expensive model (e.g., $\text{GPT-4} \rightarrow \text{Human}$), the system activates a lightweight agent ensemble to resolve ambiguities via consensus.

## 🛠️ Technical Architecture

### 1. The Escalation Boundary Trigger
The system employs a $\text{Confidence-Based Router}$ $\mathcal{R}$. For a query $q$, if the current tier model $M_i$ produces a confidence score $C(M_i, q) < \tau_{threshold}$, the system enters the **Deliberation Phase** rather than immediate escalation.

### 2. Multi-Agent Deliberation (MAD) Layer
$\text{MAD}$ consists of an ensemble of lightweight models $\{m_1, m_2, \dots, m_k\}$ that perform parallel reasoning.
- **Consensus Mechanism**: A voting or synthesis agent $\mathcal{S}$ aggregates the outputs.
- **Resolution**: If $\text{Consensus}(\{m_j\}) \rightarrow \text{High Confidence}$, the result is returned, bypassing the expensive $M_{i+1}$.
- **Fallback**: If deliberation fails to reach consensus, the query is escalated to $M_{i+1}$.

### 3. Dynamic Compute Scaling
The total test-time compute $\text{TTC}_{total}$ is defined as:
$$\text{TTC}_{total} = \sum_{i=1}^{n} \mathbb{I}(\text{escalate}_i) \cdot \text{Cost}(M_i) + \sum_{i=1}^{n} \mathbb{I}(\text{deliberate}_i) \cdot \text{Cost}(\text{MAD}_i)$$
where $\mathbb{I}(\cdot)$ is the indicator function. This allows for **elastic adaptation** to query difficulty.

## 📈 Impact & Performance
- **Accuracy**: Up to $26.75\%$ improvement over standalone cascades.
- **Efficiency**: Significant reduction in high-cost model invocations.
- **Optimization**: An online threshold optimizer $\mathcal{O}$ dynamically adjusts $\tau_{threshold}$ based on the real-world distribution.

## 🔗 Reference
- **Paper**: [arXiv:2604.12262](https://arxiv.org/abs/2604.12262)
- **Tags**: `#MultiAgent` `#TTC` `#ComputeScaling` `#LLMCascades`
