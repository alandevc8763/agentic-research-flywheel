# 🧪 Test-Time Scaling & Overtraining Optimality ($\text{T}^2$-Scaling)

## 🏛️ Architectural Core
The $\text{T}^2$ (Train-to-Test) scaling framework reconceptualizes the relationship between pretraining compute and inference-time scaling. While traditional scaling laws (e.g., Chinchilla) focus on minimizing the validation loss $\mathcal{L}$ for a fixed training budget $C_{\text{train}}$, $\text{T}^2$ jointly optimizes the total end-to-end budget $C_{\text{total}} = C_{\text{train}} + C_{\text{inference}}$.

### 📐 The Fundamental Trade-off
Test-time scaling (e.g., via repeated sampling or search) introduces a non-linear coupling between model capacity and sample efficiency:
- **Small Models**: Lower cost per sample ($\text{cost}_{\text{sample}} \propto \text{params}$), but higher error rate per sample.
- **Large Models**: Higher cost per sample, but lower error rate.
- **The Coupling**: The probability of success under $\text{pass}@k$ modeling is $P(\text{success}) = 1 - (1 - p)^k$, where $p$ is the per-sample success probability.

The $\text{T}^2$ framework proves that for a fixed end-to-end budget, the optimal pretraining allocation shifts radically into the **overtraining regime**. By training smaller models significantly beyond their Chinchilla-optimal token count, the increase in per-sample quality $p$ allows for a more efficient use of the test-time budget $k$, maximizing the overall $\text{pass}@k$ accuracy.

### 🚀 Key Findings
1. **Overtraining as an Optimality Shift**: When accounting for inference cost, "overtraining" is no longer a waste of compute but a strategic shift to reduce the marginal cost of accuracy.
2. **Robustness across Metrics**: The $\text{T}^2$ forecasts are consistent whether measuring the joint scaling effect on task loss or downstream task accuracy.
3. **Post-Training Persistence**: These optimality shifts survive the post-training (SFT/RLHF) stage, confirming that $\text{T}^2$ scaling is a primary driver of performance in modern frontier deployments.

## 📉 Mathematical Formalism
The objective function for $\text{T}^2$ scaling is to maximize:
$$\text{Accuracy}_{\text{pass}@k}(N, D, k) = 1 - \exp\left( -k \cdot \phi(N, D) \right)$$
where $N$ is model size, $D$ is training tokens, and $\phi(N, D)$ is the per-sample success rate derived from pretraining scaling laws.

By optimizing $\nabla_{N, D, k} \text{Accuracy} = 0$ subject to $C_{\text{total}}$, the framework identifies the "Saddle Point of Optimality" where training compute is diverted to maximize the "utility per token" at test-time.

## 🎯 Verifiable Utility
- **Deployment Strategy**: For models intended for high-reasoning tasks (sampled $k \gg 1$ times), the optimal strategy is to use a smaller, heavily overtrained model rather than a larger, Chinchilla-optimal model.
- **Causal Link**: Established a direct causal link between pretraining token-saturation and the efficiency of $\text{pass}@k$ search.

## 🧬 Connection to Flywheel
This artifact integrates into the **Sensing $\rightarrow$ Hunting $\rightarrow$ Alchemy $\rightarrow$ Integration** loop by providing a theoretical substrate for optimizing the Flywheel's own compute allocation. If the Flywheel is to scale its research trajectories, it must optimize the balance between its internal 'model' (the Second Brain's structural knowledge) and its 'inference' (the active research paths explored).
