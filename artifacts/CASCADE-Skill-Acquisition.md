# 🌌 CASCADE: Cumulative Agentic Skill Acquisition

## 🎯 Core Thesis
$\text{CASCADE}$ operationalizes the paradigm shift from **"LLM + Tool Use"** $\rightarrow$ **"LLM + Skill Acquisition"**. It argues that true agentic autonomy requires the cumulative mastery of external tools and the codification of executable routines, rather than relying on predefined action spaces.

## 🏗️ Architectural Framework: The $\text{DeepSolver}$ Loop
The system implements a high-fidelity acquisition pipeline designed to maximize the $\text{SNR}$ of tool interaction:

$$\text{Task} \xrightarrow{\text{Researcher}} \text{Initial Solution} \xrightarrow{\text{Executor}} \text{Error} \xrightarrow{\text{Parallel Debuggers}} \text{Refined Skill} \xrightarrow{\text{Processor}} \text{Output}$$

### 1. $\text{Solution Researcher}$ (The Synthesis Layer)
- **Function**: Performs targeted intelligence gathering via web search and code extraction.
- **Mechanism**: Synthesizes initial executable hypotheses by retrieving real-world code examples and adapting them to the specific task constraints.

### 2. $\text{Code Agent}$ (The Validation Layer)
- **Function**: Executes the solution in an isolated environment.
- **Constraint**: Strictly a "single-shot" executor; it does not self-debug, ensuring a clean signal for the debugging layer.

### 3. $\text{Parallel Debug Agents}$ (The Evolution Layer)
When execution fails, $\text{CASCADE}$ spawns multiple debuggers employing divergent strategies:
- $\text{Direct Fix}$: Corrects syntax/obvious logical errors.
- $\text{Introspection/Probe}$: Uses `quick_introspect` and `runtime_probe_snippet` to resolve `KeyError`/`AttributeError`.
- $\text{Knowledge Graph Fix}$: Explores package hierarchies and method signatures via AST analysis.
- $\text{Research Fix}$: Re-queries external documentation for non-Python/CLI tools.

### 4. $\text{Output Processor}$ (The Consolidation Layer)
- **Function**: Evaluates the parallel debug outputs, selects the optimal solution based on execution success and data quality, and formats the final result.

## 🧠 Meta-Skill Taxonomy
$\text{CASCADE}$ evolves via two primary meta-skills:
1. **Continuous Learning**: Real-time acquisition of targeted external knowledge $\rightarrow$ $\text{Web Search} \oplus \text{Code Extraction} \oplus \text{Memory Retrieval}$.
2. **Self-Reflection**: Introspective evaluation of solution quality $\rightarrow$ $\text{Introspection} \oplus \text{KG Exploration} \oplus \text{Runtime Probing}$.

## 📊 Performance Metrics
Evaluated on $\text{SciSkillBench}$ (116 materials science/chemistry tasks):
- **Success Rate**: $\sim 93.3\%$ (GPT-5) vs $35.4\%$ (Baseline).
- **Robustness**: Maintains high accuracy on "Difficult" tasks where standard Search&Debug baselines collapse.
- **Generalization**: Domain-agnostic design allows transfer to software engineering and biology.

## 🛠️ Implementation Detail: MCP Integration
The framework leverages the **Model Context Protocol (MCP)** to decouple capabilities:
- $\text{Tavily MCP}$: High-signal web search.
- $\text{Memory MCP}$: Hybrid Vector $\oplus$ Graph store for skill retention.
- $\text{Research MCP}$: Code intelligence, AST parsing, and introspection.
- $\text{Workspace MCP}$: Environment isolation and package management.

---
**Source**: [arXiv:2512.23880](https://arxiv.org/abs/2512.23880)
**Tags**: #SkillAcquisition #SelfEvolution #AgenticAI #MCP #DeepSolver
