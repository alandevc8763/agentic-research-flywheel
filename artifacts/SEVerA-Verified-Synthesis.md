# SEVerA: Verified Synthesis of Self-Evolving Agents

## 📌 Architectural Overview
SEVerA ($\text{SEVerA}$) implements a constrained learning framework for agentic code generation, ensuring that self-evolving agent programs satisfy hard formal specifications while optimizing for soft utility objectives. It bridges the gap between probabilistic LLM synthesis and deterministic formal verification.

### 🏗️ Core Components

#### 1. Formally Guarded Generative Models (FGGM)
The fundamental primitive of SEVerA. An FGGM wraps a generative model call (e.g., an LLM) with a formal output contract.
- **Formal Contract**: Specified using first-order logic (FOL).
- **Mechanism**: Employs a rejection sampler with a verified fallback.
- **Guarantee**: Every output is guaranteed to satisfy the contract regardless of the underlying model's parameterization or input.

#### 2. The Three-Stage Pipeline
$\text{SEVerA}$ evolves agents through a rigorous cycle of synthesis, verification, and optimization:
1. **Search**: The planner LLM synthesizes candidate parametric programs. These programs are structured as sequences of FGGM calls.
2. **Verification**: Formal proofs are generated to ensure the programs satisfy hard constraints for all possible parameter values. This effectively transforms the constrained problem into an unconstrained one by pruning the search space of unsafe programs.
3. **Learning**: Scalable gradient-based optimization (including GRPO-style fine-tuning) is applied to the parametric models to maximize the soft utility objective (task performance) while the FGGM guarantees ensure correctness is preserved.

### 🚀 Key Contributions & Results
- **Zero Constraint Violations**: Achieved $0\%$ violation rate on benchmarks including Dafny program verification and $\tau^2\text{-bench}$.
- **Performance Gain**: Outperforms SOTA unconstrained baselines by steering the synthesis process toward higher-quality, verified trajectories.
- **Application Domains**: Demonstrated efficacy in symbolic math synthesis and policy-compliant agentic tool use.

## 🛠️ Implementation Insights for the Flywheel
To integrate SEVerA logic into the Research Flywheel, the following primitives should be adopted:
- **Contract-Based Tool Synthesis**: Move from "prompt-based" tool descriptions to "FOL-contract" based definitions.
- **Verified Fallbacks**: Implement a safety layer that catches LLM-generated tool calls that violate pre-defined safety/correctness invariants.
- **Constraint-Steered Evolution**: Use formal verification results as a reward signal (or a hard filter) during the distillation process to ensure that integrated knowledge is not just "likely" correct, but "provably" correct.

## 📚 Reference
- **Paper**: [arXiv:2603.25111](https://arxiv.org/abs/2603.25111)
- **Authors**: Debangshu Banerjee, Changming Xu, Eugene Ie, Ming Zhang, Daiyi Peng, Chu-Cheng Lin, Gagandeep Singh.
- **Date**: April 2026.
