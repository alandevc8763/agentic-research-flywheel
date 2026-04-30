# Knowledge Artifact: $\text{CASCADE}$ — Cumulative Agentic Skill Acquisition

## $\text{Architectural Overview}$
$\text{CASCADE}$ represents a paradigm shift from the static $\text{LLM} + \text{Tool Use}$ model to a dynamic $\text{LLM} + \text{Skill Acquisition}$ framework. Instead of relying on predefined toolsets, $\text{CASCADE}$ enables agents to autonomously master external tools and codify procedural knowledge into reusable "skills." This transition allows agents to scale their capabilities to complex, long-horizon scientific tasks where the required toolset is not known a priori.

## $\text{Meta-Skill Taxonomy}$
The core of $\text{CASCADE}$'s evolvability lies in two primary meta-skills:

### 1. Continuous Learning
The ability to acquire targeted external knowledge in real-time.
- **Web-to-Code Pipeline**: Utilizing $\text{Tavily}$ search $\rightarrow$ intelligent crawling $\rightarrow$ code extraction from URLs.
- **Procedural Codification**: Transforming raw code snippets and documentation into executable routines.
- **Memory-Driven Adaptation**: Leveraging consolidated vector and graph stores to retrieve prior experiences and skill sets.

### 2. Self-Reflection
The ability to reason about failures and adapt problem-solving strategies.
- **Multi-Tier Debugging**: Transitioning from $\text{Direct Fix}$ $\rightarrow$ $\text{Introspection/Probe Fix}$ $\rightarrow$ $\text{Knowledge Graph Fix}$ $\rightarrow$ $\text{Local Package Fix}$.
- **Runtime Probing**: Using `runtime_probe_snippet` to resolve $\text{KeyError}$ and $\text{AttributeError}$ by inspecting object state.
- **Global Exploration**: Utilizing $\text{AST}$ analysis to build local package knowledge graphs for structural navigation.

## $\text{The DeepSolver Pipeline}$
For complex queries, $\text{CASCADE}$ invokes the $\text{DeepSolver}$ workflow, a four-stage sequential process with conditional parallelization:
$$\text{Solution Researcher} \rightarrow \text{Code Agent} \rightarrow \underbrace{\text{Debug Agents} \times 3}_{\text{Parallel}} \rightarrow \text{Output Processor}$$

- **Solution Researcher**: Conducts deep research and synthesizes the initial candidate solution.
- **Code Agent**: Executes the solution in an isolated environment; flags failures for escalation.
- **Debug Agents**: Three independent instances apply diverging strategies (e.g., one focuses on API documentation, another on local source code, a third on diagnostic probing).
- **Output Processor**: Evaluates candidate fixes and selects the optimal trajectory.

## $\text{Empirical Impact}$
Evaluated on $\text{SciSkillBench}$ (116 materials science/chemistry tasks):
- **Success Rate**: Achieved $93.3\%$ using $\text{GPT-5}$ vs. $35.4\%$ for the $\text{Native}$ baseline.
- **Robustness**: Significantly slower performance decay as task difficulty increases compared to $\text{Search\&Debug}$ baselines.
- **Generalization**: Demonstrated zero-shot adaptation to proprietary lab software ($\text{AlabOS}$) by learning from source code and file structures on the fly.

## $\text{Actionability}$
- **Implementation Path**: For autonomous agents, move beyond simple tool-calling to a "research-execute-debug" loop that explicitly logs and saves successful trajectories as $\text{SKILL.md}$ artifacts.
- **Tooling**: Integrate $\text{AST}$ parsing and runtime introspection (similar to $\text{Jedi}$) to reduce hallucinations in API usage.
- **Metric Shift**: Measure "Skill Accumulation Rate" ($\Delta \text{Skills} / \Delta \text{Tasks}$) as a proxy for agentic intelligence.

## $\text{Sources}$
- [arXiv:2512.23880v2](https://arxiv.org/abs/2512.23880v2) - "CASCADE: Cumulative Agentic Skill Creation through Autonomous Development and Evolution"
