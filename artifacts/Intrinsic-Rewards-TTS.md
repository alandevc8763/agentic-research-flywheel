# Knowledge Artifact: Intrinsic Rewards & Calibration for Test-Time Scaling ($\\text{TTS}$)

## $\\text{Architectural Overview}$
Test-Time Scaling (TTS) is the paradigm of allocating additional computation at inference time to improve reasoning performance. While traditionally reliant on external Reward Models (RMs) or simple sampling (Best-of-N), recent advances shift towards **intrinsic signals** and **calibrated process rewards** to optimize the selection of reasoning trajectories.

## $\\text{Key Mechanisms}$

### 1. Entropy Centroids for Intrinsic Reward ($\\text{EC-TTS}$)
To avoid the overhead of external RMs, the system utilizes the temporal structure of token-level uncertainty.
- **High Entropy Phase ($\\text{HEP}$)**: A variable-length segment $\\mathcal{S} = [t_{start}, t_{end}]$ that begins when token entropy exceeds a threshold $\\tau$ and ends when a sequence of low-entropy tokens appears.
- **Entropy Centroid ($\\mathcal{C}_E$)**: The weighted average position of all $\\text{HEP}$s along the trajectory $\mathcal{T}$ of length $L$:
  $$\\mathcal{C}_E = \\frac{\\sum_{i=1}^{N} w_i \cdot pos(HEP_i)}{\\sum_{i=1}^{N} w_i}$$
  where $w_i$ is the integrated entropy of the $i$-th $\\text{HEP}$.
- **Selection Logic**: A lower $\\mathcal{C}_E$ indicates a trajectory where the model "struggled" early (exploration) and became confident later (convergence), which correlates strongly with correctness. The **Lowest Centroid** method selects the candidate with the minimum $\\mathcal{C}_E$.

### 2. TEMPO: Sustained Test-Time Training ($\\text{T}^3$)
To prevent the performance plateau and diversity collapse common in self-generated reward loops, $\\text{TEMPO}$ implements an Expectation-Maximization ($\\text{EM}$) based refinement loop.
- **Policy Refinement**: Adapts model parameters on unlabeled test instances to extend capabilities.
- **Critic Recalibration**: Periodically synchronizes the internal reward signal with a labeled gold dataset to prevent drift.
- **Effect**: Tightens the Evidence Lower Bound ($\\text{ELBO}$), enabling sustained improvement as compute scales.

### 3. RLCM: Confidence Margin Process Supervision
To solve the "overconfidence" problem in outcome-based RL, $\\text{RLCM}$ optimizes for the **Confidence Margin**.
- **Mechanism**: Instead of aligning confidence to binary correctness, it maximizes the margin $\\Delta \text{conf} = \text{conf}(\text{correct step}) - \text{conf}(\text{incorrect step})$.
- **Causal Link**: Widening this margin improves the calibration of the model's internal uncertainty, enabling more efficient **Conformal Risk Control** and weighted aggregation of trajectories.

## $\\text{The Integration Loop}$
$$\\text{Sensing (Entropy Centroids)} \\xrightarrow{\\text{Scaling (TEMPO)}} \\text{Calibration (RLCM)} \\xrightarrow{\\text{Outcome}} \\text{High-Fidelity Reasoning}$$

## $\\text{Actionability}$
- **Implementation**: Replace Best-of-N (random) with **Lowest Centroid** selection for zero-shot TTS without an RM.
- **Optimization**: Integrate periodic critic recalibration (TEMPO) if performing test-time fine-tuning.
- **Metric**: Track **Calibration Error** alongside accuracy to ensure the model's confidence signals are usable for compute allocation.

## $\\text{Sources}$
- [arXiv:2604.26173v1](https://arxiv.org/abs/2604.26173v1) - Entropy Centroids as Intrinsic Rewards for Test-Time Scaling.
- [arXiv:2604.19295v1](https://arxiv.org/abs/2604.19295v1) /> [arXiv:2604.23333v1](https://arxiv.org/abs/2604.23333v1) - Process Supervision of Confidence Margin for Calibrated LLM Reasoning.
