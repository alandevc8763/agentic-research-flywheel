# Knowledge Artifact: Bian Que (Agentic O&M Framework)

## $\text{Architectural Overview}$
**Bian Que** is a specialized agentic framework designed to automate Operations and Maintenance (O&M) for large-scale online engine systems (search, recommendation, and advertising). It addresses the **orchestration gap** in SRE automation by treating \"skill arrangement\" as a dynamic, evolvable layer rather than a static prompt mapping.

## $\text{Key Mechanisms}$

### 1. Unified Operational Paradigm
Bian Que abstracts complex day-to-day O&M into three canonical patterns:
- **Release Interception**: Monitoring and validating new deployments to prevent regressions.
- **Proactive Inspection**: Scanning for latent issues before alert triggers.
- **Root Cause Analysis (RCA)**: Automating the diagnostic pipeline upon alert triggering.

### 2. Flexible Skill Arrangement
Instead of static prompts, Bian Que utilizes **Skills** as retrieval specifications:
- **Context-Aware Retrieval**: Skills define precise data/knowledge fetch requirements based on the `business-module` context, preventing signal dilution.
- **Dynamic Generation**: Skills are iteratively refined via LLMs or natural-language instructions from engineers, allowing the system to adapt to architectural shifts without code changes.

### 3. Unified Self-Evolving Mechanism
The framework employs a closed-loop learning system where engineer corrections trigger parallel improvement paths:
- **Knowledge Distillation**: Case-Memory $\xrightarrow{\text{Distill}}$ General Operational Knowledge.
- **Skill Refinement**: Direct updates to the retrieval specifications of the failing skill.

## $\text{Empirical Utility}$
- **Reduced Signal Dilution**: By avoiding "data dumping" into prompts, Bian Que maintains high SNR for diagnostic reasoning.
- **Adaptive Orchestration**: The evolvable skill layer bridges the gap between general LLM reasoning and production-specific telemetry requirements.

## $\text{Actionability}$
- **Implementation Path**: For SRE agents, implement a "Skill" layer that specifies retrieval needs based on the operational pattern (Interception/Inspection/RCA) instead of feeding all available logs/metrics.
- **Feedback Loop**: Treat human corrections as high-signal training data to evolve retrieval logic and the underlying knowledge base.

## $\text{Sources}$
- [arXiv:2604.26805](https://arxiv.org/abs/2604.26805) - Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations.
- [BianQue_Assistant GitHub](https://github.com/benchen4395/BianQue_Assistant)
