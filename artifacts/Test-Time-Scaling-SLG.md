# Knowledge Artifact: Scaling-Law Guided (SLG) Search

## 1. Metadata
- **Source**: arXiv:2602.01485 / [GitHub: PotatoJnny/Scaling-Law-Guided-search](https://github.com/PotatoJnny/Scaling-Law-Guided-search)
- **Title**: Predicting and improving test-time scaling laws via reward tail-guided search
- **Domain**: Test-Time Compute $\rightarrow$ Scaling Laws $\rightarrow$ Reasoning Verification
- **Confidence**: High (Empirical validation + Theoretical regret bounds)

## 2. Core Thesis
The "Best-of-N" (BoN) strategy for enhancing LLM reasoning is computationally inefficient because it allocates budget blindly. By modeling the **tail distribution of rewards**, it is possible to predict the scaling behavior of a state and dynamically allocate compute to the most promising trajectories, achieving superior reward yields with polynomially smaller budgets.

## 3. Technical Architecture ($\text{SLG-Search}$)

### 3.1 The Scaling Law Estimator
The system estimates the potential value $V^N(s)$ of an intermediate state $s$ given a total budget $N$. Instead of exhaustive sampling, it uses a small number of samples $m \ll N$ to extrapolate the tail of the reward distribution.

### 3.2 Algorithm Logic
Given a prompt $x$, total budget $N$, search width $K$, and estimation samples $m$:

1. **$\text{Expansion}$**: Generate $K$ candidate intermediate states $\mathcal{S} = \{s_1, s_2, \dots, s_K\}$.
2. **$\text{Estimation}$**: For each $s_i \in \mathcal{S}$:
   - Sample $m$ completions $\{y_{i,1}, \dots, y_{i,m}\}$.
   - Calculate rewards $\{r_{i,1}, \dots, r_{i,m}\}$.
   - Estimate the predicted value $V^N(s_i)$ using tail extrapolation.
3. **$\text{Selection}$**: Identify the optimal state $I^* = \arg\max_{i \in [K]} V^N(s_i)$.
4. **$\text{Exploitation}$**: Allocate the remaining budget $N - (K \times m)$ to state $s_{I^*}$ to maximize the probability of hitting the reward peak.
5. **$\text{Termination}$**: Return $\max(\text{all observed rewards})$.

## 4. Theoretical & Empirical Impact
- **Regret Bounds**: SLG achieves **vanishing regret** relative to a perfect-information oracle.
- **Compute Efficiency**: achieves the same expected reward as BoN but with a **polynomially smaller compute budget**.
- **Application**: Validated across multiple LLMs (Llama series) and Reward Models (Skywork-Reward), specifically on high-difficulty reasoning datasets like AIME.

## 5. Synthesis for Second Brain
$\text{Test-Time Scaling} \neq \text{More Samples}$. The frontier is shifting toward **$\text{Adaptive Budget Allocation}$**. SLG Search proves that the *distribution* of rewards in the tail is a sufficient statistic for predicting the utility of a reasoning path, allowing the agent to "bet" its compute on the most promising seeds.
