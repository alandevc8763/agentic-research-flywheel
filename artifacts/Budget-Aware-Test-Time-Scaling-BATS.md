# 💰 Budget-Aware Test-Time Scaling ($\text{BATS}$)

## 1. Formalism: The Resource-Constrained Agent Scaling Problem
Standard test-time compute scaling for LLMs focuses on token-budget expansion (thinking). For tool-augmented agents, scaling is a dual-optimization problem across **Internal Cognition** (tokens) and **External Interaction** (tool calls). 

The core bottleneck is the **Cognitive Ceiling**: agents without explicit budget awareness fail to utilize additional resources, terminating prematurely because they *believe* they have sufficient information or are "stuck," regardless of available budget.

### 1.1 Unified Cost Metric ($\text{C}_{\text{unified}}$)
To quantify the cost-performance Pareto frontier, $\text{BATS}$ introduces a unified metric that maps disparate resources to economic cost:
$$\text{C}_{\text{unified}} = \text{C}_{\text{token}} + \sum_{i=1}^{K} (c_i \cdot P_i)$$
Where:
- $\text{C}_{\text{token}}$: Total cost of input, output, and cache-hit tokens.
- $c_i$: Realized number of calls to tool $t_i$.
- $P_i$: Economic cost per invocation of tool $t_i$.

## 2. Architectural Implementation: The $\text{BATS}$ Framework

### 2.1 The Budget Tracker (Sensing Layer)
A plug-and-play module that surfaces real-time resource states within the agent's reasoning loop. It transforms the latent budget into an explicit prompt-level signal:
$$\text{State}_{t} \rightarrow \{ \text{Budget}_{\text{used}}, \text{Budget}_{\text{remaining}} \}$$
This allows the agent to condition its subsequent $\text{Think} \rightarrow \text{Act}$ cycle on the remaining resource density.

### 2.2 $\text{BATS}$ Orchestration (Control Layer)
$\text{BATS}$ extends simple awareness into active strategy adaptation through two primary mechanisms:
1. **Dynamic Planning**: Adjusts stepwise effort and exploration breadth to match the remaining budget.
2. **Adaptive Verification**: Employs a "Dig Deeper vs. Pivot" logic. If a lead is promising and budget is ample, it increases depth; if budget is critical, it pivots to alternative paths.

## 3. Utility Analysis & Impact
- $\text{Actionability}$: High. Budget trackers can be implemented as simple system prompt injections; $\text{BATS}$ logic can be integrated into ReAct loops.
- $\text{Architectural Depth}$: High. Shifts the paradigm from "naive scaling" (just giving more budget) to "strategic scaling" (budget-aware optimization).
- $\text{Novelty}$: Introduces the first systematic study of budget-constrained agent scaling and the associated cost-performance Pareto curves.

**Outcome**: $\text{BATS}$ effectively pushes the Pareto frontier, achieving higher accuracy with lower unified cost compared to standard ReAct agents, and avoids the performance saturation observed in budget-unaware systems.

---
**Tags**: #TestTimeCompute #AgentScaling #BudgetAwareness #BATS #ResourceOptimization
**Sources**: Liu et al. (2025) - "Budget-Aware Tool-Use Enables Effective Agent Scaling" [arXiv:2511.17006]
