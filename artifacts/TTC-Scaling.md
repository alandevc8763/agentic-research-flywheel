# Knowledge Artifact: TTC-Scaling (Tail-Guided Test-Time Compute)
**Date**: 2026-04-18
**Source**: [arXiv:2602.01485](https://arxiv.org/abs/2602.01485)
**Signal Density**: $\text{High}$

## 🧩 Core Concept
Transition from **Brute-Force Sampling** ($\text{Best-of-N}$) to **Predictive Compute Allocation** ($\text{SLG-Search}$).

## 🛠 Technical Mechanism
The system implements a **Tail-Guided Search** framework:
1. **Tail Estimation**: $\mathcal{P}(\text{Reward} > \tau)$ is estimated to predict the scaling property of the model without exhaustive sampling.
2. **SLG-Search**: Dynamically allocates compute budgets to intermediate reasoning states based on the predicted probability of hitting the reward tail.
3. **Regret Minimization**: Mathematically proven to achieve vanishing regret relative to a perfect-information oracle.

## 📈 Impact & Performance
- **Compute Efficiency**: Achieves target rewards with $\text{poly}(1/\epsilon)$ smaller budgets compared to BoN.
- **Scaling Law**: Establishes a principled relationship between test-time compute $\mathcal{C}_{\text{test}}$ and the probability of success $P(\text{success})$.

## 🔗 Cross-References
- **PRISM-MCTS**: Complements SLG by using metacognitive reflection to refine the trajectories that SLG selects.
- **GRPO**: Provides the reward signal (group-relative baseline) that can be used for the tail estimation.

## 🏷 Tags
#TestTimeCompute #ScalingLaws #Reasoning #SOTA-Optimization #TailGuidedSearch
