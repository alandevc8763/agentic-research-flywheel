# Knowledge Artifact: Memory-Driven Prompt Optimization ($\text{MemAPO}$)

## $\text{Architectural Overview}$
$\text{MemAPO}$ is a framework that reconceptualizes prompt optimization as a process of **generalizable and self-evolving experience accumulation** rather than task-specific search. It addresses the limitation of traditional automatic prompt optimization (APO) which often restarts from scratch for each new task and fails to accumulate reusable knowledge.

## $\text{Key Mechanisms}$

### 1. Dual-Memory Mechanism
The core of $\text{MemAPO}$ is a dual-memory system that stores distilled reasoning trajectories and failure modes:
- **Strategy Memory**: Distills successful reasoning trajectories into **reusable strategy templates**. These templates capture the *how* of successful problem solving, preserving the underlying logic while abstracting away task-specific entities.
- **Error Pattern Memory**: Organizes incorrect generations into **structured error patterns**. This allows the system to identify recurrent failure modes and explicitly discourage them in future prompts.

### 2. Retrieval-Augmented Prompt Composition
Instead of searching for a new prompt, $\text{MemAPO}$ uses a retrieval mechanism:
- **Input**: A new task or query.
- **Retrieval**: Fetches relevant strategy templates from the Strategy Memory and corresponding failure patterns from the Error Pattern Memory.
- **Composition**: Composes a final prompt that promotes effective reasoning (via strategy templates) and prevents known mistakes (via error patterns).

### 3. Iterative Self-Evolution
The system evolves through a continuous loop of reflection and memory editing:
- **Execution**: The model generates a response using the composed prompt.
- **Reflection**: The system analyzes the result to determine if the strategy was successful or if a new error pattern emerged.
- **Update**: The memory is edited—new successful trajectories are distilled into templates, and new failures are added to the error patterns.

## $\text{The Evolutionary Loop}$
$$\text{Query} \xrightarrow{\text{Retrieve Memory}} \text{Compose Prompt} \xrightarrow{\text{Execute}} \text{Outcome} \xrightarrow{\text{Reflection}} \text{Update Memory} \xrightarrow{\text{Iterative Evolution}}$$

## $\text{Actionability}$
- **Implementation**: Implement a dual-memory store (Strategy/Error) using a vector database.
- **Integration**: Use the retrieved strategy/error pairs as "soft constraints" or "reasoning hints" in the system prompt.
- **Metric**: Track **Generalization Gain** ($\Delta\text{GG}$) — the performance improvement on a new, unseen task compared to a zero-shot prompt, attributed to the retrieved memory.

## $\text{Sources}$
- [arXiv:2603.21520v1](https://arxiv.org/abs/2603.21520v1) - Generalizable Self-Evolving Memory for Automatic Prompt Optimization.
