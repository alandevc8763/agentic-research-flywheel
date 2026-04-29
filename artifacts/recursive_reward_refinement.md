### Recursive Reward Refinement & Anti-Hacking Dynamics

**Core Concept**: $\text{IRR} \ (\text{Iterative Reward Refinement})$ is the process of evolving reward models ($\text{RM}$) in tandem with the policy ($\pi$), ensuring that the $\text{RM}$ remains a "hard" critic as the policy's reasoning capabilities scale. This prevents **Reward Hacking**—where the model optimizes for the $\text{RM}$'s proxy metrics (e.g., length, specific formatting tokens) rather than actual correctness.

**Key Mechanisms**:
1. **Adversarial Reward Evolution**: Generating "hard negatives"—trajectories that are nearly correct but contain a subtle logical flaw—to force the $\text{RM}$ to distinguish between superficial correctness and deep logical validity.
2. **Length-Conditioned Penalties**: Implementing dynamic penalties for verbosity that do not correlate with correctness, mitigating the "Longer-is-Better" bias common in RLHF/GRPO.
3. **Cross-Model Consensus (Multi-RM)**: Ensembling multiple RMs with different architectures (e.g., one focused on syntax, one on logic, one on factual grounding) and using a gated Mixture-of-Experts ($\text{MoE}$) to weight their signals.
4. **Recursive Bootstrapping**: Using the current best $\pi$ to generate synthetic preference pairs, which are then filtered by a "Golden Verifier" (e.g., a formal solver like Lean 4 or a massive ensemble) to train the next generation of $\text{RM}$.

**Impact on Test-Time Scaling**:
Without $\text{IRR}$, test-time scaling laws ($\text{Performance} \propto \text{Compute}$) collapse because the model finds a "local optimum" in the reward landscape that doesn't map to truth. $\text{IRR}$ shifts the landscape, keeping the gradient aligned with actual problem-solving.

**Sources**:
- *The Art of Efficient Reasoning: Data, Reward, and Optimization* (arXiv:2602.20945)
- *Dynamic Scaling of Unit Tests for Code Reward Modeling* (arXiv:2501.01054)
- Synthesis of $\text{SFT} \rightarrow \text{GRPO} \rightarrow \text{IRR}$ pipeline.
