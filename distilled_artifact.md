# $\text{PRM-Evolution}$: From Binary Verification to Generative Correction and Implicit Reward Structures

## 1. Theoretical Framework: The Verifier Bottleneck
In the scaling of test-time compute ($\text{TTC}$), the bottleneck shifts from the **Generator** (the policy model) to the **Verifier** (the reward model). If the verifier cannot distinguish between a "correct-looking" hallucination and a truly logical step, the system suffers from **Reasoning Drift**.

## 2. Evolutionary Trajectory of Process Reward Models (PRMs)

### Phase I: Unidirectional Process Supervision ($\text{PRM}_{L2R}$)
The baseline paradigm where a model assigns a scalar score to each step in a left-to-right trajectory.
- **Constraint**: Lack of global context; suffers from "greedy" local optima.

### Phase II: Architectural Enhancements ($\text{BiPRM}$, $\text{RetrievalPRM}$, $\text{PQM}$)
- **$\text{BiPRM}$ (Bidirectional)**: Introduces a parallel right-to-left ($\text{R2L}$) stream, fusing bidirectional context via a gating mechanism. $\text{Gain} \approx 10.6\%$ over unidirectional baselines.
- **$\text{RetrievalPRM}$**: Combats Out-of-Distribution ($\text{OOD}$) failures by retrieving semantically similar reasoning steps as a warmup.
- **$\text{PQM}$ (Process Q-value Model)**: Shifts from classification (Cross-Entropy) to Q-value ranking within a Markov Decision Process ($\text{MDP}$) framework.

### Phase III: Generative & Corrective Verifiers ($\text{GM-PRM}$)
The transition from passive judging to active collaboration.
- **Mechanism**: Instead of $\text{Score} \in [0, 1]$, the verifier generates a corrected version of the first identified erroneous step.
- **Impact**: Enables **Refined Best-of-N (Refined-BoN)**, where the generator is steered by the verifier's corrections in real-time.

### Phase IV: Implicit Reward Structures ($\text{GRPO} \approx \text{PRM}$)
The theoretical unification of Group Relative Policy Optimization.
- **Key Insight**: GRPO equipped with an Outcome Reward Model ($\text{ORM}$) is mathematically equivalent to a $\text{PRM}$-aware RL objective using Monte-Carlo based process rewards.
- **Result**: High-performance reasoning can be achieved without explicit step-level human annotations.

## 3. Synthesis Matrix

| Paradigm | Signal Type | Context | Primary Utility | Key Model/Paper |
| :--- | :--- | :--- | :--- | :--- |
| $\text{ORM}$ | Scalar (End) | Global | Coarse filtering | $\text{RLHF-Baseline}$ |
| $\text{PRM}$ | Scalar (Step) | Local | Fine-grained credit | $\text{OpenAI-PRM}$ |
| $\text{BiPRM}$ | Fused Scalar | Bi-directional | Contextual Robustness | $\text{Zhang et al. 2025}$ |
| $\text{GM-PRM}$ | Generative Text | Collaborative | Direct Correction | $\text{GM-PRM}$ |
| $\text{GRPO}$ | Relative Group | Implicit | Annotation-free scaling | $\text{DeepSeek-R1}$ |

## 4. Impact on the Flywheel
This evolution allows the $\text{Agentic Research Flywheel}$ to move toward **Autonomous Gap Detection** by implementing a $\text{GM-PRM}$ based critic that not only identifies a "void" in knowledge but generates the specific research query needed to fill it.
