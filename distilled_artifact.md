# 🚀 Test-Time Compute ($\text{TTC}$) Scaling & Verifier Architectures

**Category**: LLM Reasoning / Inference Optimization  
**Tags**: `ttc-scaling`, `orm-vs-prm`, `mcts-reasoning`, `adaptive-compute`, `grpo`  
**Sources**: 
- Adaptive Test-Time Compute Allocation (arXiv:2604.14853, 2026)
- DeepSeek-R1 Technical Analysis (GRPO / RLVR)
- General SOTA Reasoning Frameworks (OpenAI o1-style search)

## 📌 Executive Summary
Test-Time Compute ($\text{TTC}$) scaling is the paradigm of increasing the computational budget during the inference phase to improve model performance on complex reasoning tasks. This is achieved by shifting from a "single-shot" generation to a "search-and-verify" loop. The core evolution is the transition from **Outcome Reward Models ($\text{ORM}$)** to **Process Reward Models ($\text{PRM}$)**, enabling more granular guidance of the reasoning trajectory and the application of search algorithms like **Monte Carlo Tree Search ($\text{MCTS}$)**.

## 🛠 Technical Architecture

### 1. The $\text{TTC}$ Scaling Hierarchy
$\text{TTC}$ can be scaled across three primary dimensions:
- **Sampling ($\text{Best-of-N}$)**: Generating $N$ independent trajectories and selecting the best via an $\text{ORM}$. 
  - $\text{Complexity}$: $O(N \cdot L)$ where $L$ is trajectory length.
  - $\text{Limitation}$: No inter-step guidance; efficiency drops as task complexity increases.
- **Search ($\text{Tree/Graph}$)**: Exploring the reasoning space via Beam Search or $\text{MCTS}$ guided by a $\text{PRM}$.
  - $\text{Complexity}$: $O(B^D)$ where $B$ is branching factor and $D$ is depth.
  - $\text{Benefit}$: Prunes incorrect paths early, exponentially increasing the probability of finding a correct solution.
- **Computation ($\text{Chain-of-Thought}$)**: Allowing the model to generate more internal tokens (longer "thinking" process) before providing the final answer.

### 2. $\text{ORM}$ vs $\text{PRM}$: The Verifier Evolution
The quality of $\text{TTC}$ scaling depends on the **Verifier** $\mathcal{V}$.
- **Outcome Reward Model ($\text{ORM}$)**: $\mathcal{V}(\tau) \rightarrow [0, 1]$. Evaluates the final answer.
  - $\text{Pros}$: Easy to label (ground truth).
  - $\text{Cons}$: Sparse signal; doesn't penalize "correct answer via wrong reasoning" (reward hacking).
- **Process Reward Model ($\text{PRM}$)**: $\mathcal{V}(s_i) \rightarrow [0, 1]$ for each step $s_i \in \tau$.
  - $\text{Pros}$: Dense signal; enables step-level pruning and search.
  - $\text{Cons}$: Extremely expensive to label (requires human/model expert critique of every step).

### 3. Adaptive $\text{TTC}$ Allocation
Rather than uniform allocation, modern systems use **Adaptive Budgeting** to maximize $\text{Accuracy} / \text{Cost}$:
$$\max \mathbb{E}[\text{Accuracy}(\text{TTC}_i)] \quad \text{s.t.} \quad \frac{1}{N} \sum \text{TTC}_i \le \text{Budget}$$
Using **Lagrangian Relaxation**, the optimal allocation is found by pricing accuracy against cost:
- **Hard Problems**: Higher "price" $\rightarrow$ allocated more samples/search depth.
- **Easy Problems**: Lower "price" $\rightarrow$ solved via single-shot generation.
- **Amortization**: A lightweight classifier predicts the optimal $\text{TTC}_i$ based on input features to avoid the cost of the oracle.

### 4. Implicit Rewards and $\text{GRPO}$
**Group Relative Policy Optimization ($\text{GRPO}$)** enables scaling reasoning without a separate Value/Critic network:
- **Mechanism**: Samples a group of $G$ outputs $\{o_1, \dots, o_G\}$ for the same prompt.
- **Advantage**: Uses the relative reward $\hat{A}_i = \frac{r_i - \text{mean}(\mathbf{r})}{\text{std}(\mathbf{r})}$ as the advantage signal.
- **Effect**: Stabilizes the self-improvement loop and allows the model to discover optimal reasoning paths through relative comparison.

## 📈 Utility Analysis
- **Actionability**: High. $\text{Best-of-N}$ is trivial to implement; $\text{MCTS}$ with a $\text{PRM}$ is the current frontier for "Reasoning-as-a-Service".
- **Architectural Depth**: Deep. Explains the mathematical transition from sparse to dense rewards and the optimization of inference budgets.
- **Novelty**: Integrates the latest 2026 research on adaptive compute allocation.
