# 🌀 Methodological Evolution Graph (MEG)
**Source**: Intern-Atlas (arXiv:2604.28158v1)
**Status**: Integrated $\rightarrow$ $\text{Sensing Engine Substrate}$

## 📐 Theoretical Framework
The $\text{Methodological Evolution Graph}$ ($\text{MEG}$) represents a paradigm shift from **Document-Centric** to **Method-Centric** knowledge retrieval. Traditional citation networks $\mathcal{G}_{cit} = (V, E)$ where $V$ are papers and $E$ are citations, fail to capture the *causal mechanisms* of innovation. 

$\text{MEG}$ defines a graph $\mathcal{G}_{meth} = (\mathcal{M}, \mathcal{R})$ where:
- $\mathcal{M}$: Method-level entities (e.g., $\text{GRPO}$, $\text{MCTS}$, $\text{KV-Caching}$).
- $\mathcal{R}$: Lineage relationships $\mathcal{R} \subseteq \mathcal{M} \times \mathcal{M}$, representing a transformation $\mathcal{T}: m_i \rightarrow m_j$ driven by a specific **innovation bottleneck** $\mathcal{B}$.

### $\text{The Bottleneck Equation}$
Innovation is modeled as the resolution of a structural bottleneck:
$$\Delta \text{Capability} = \int_{t_0}^{t_1} \mathcal{F}(\mathcal{B}, \mathcal{T}) \, dt$$
Where $\mathcal{B}$ is the limiting factor (e.g., $\text{VRAM bottleneck} \rightarrow \text{FlashAttention}$) and $\mathcal{T}$ is the methodological transformation.

## 🛠️ Implementation for Flywheel Sensing
Integrating $\text{MEG}$ into the `GapDetector` transforms sensing from "keyword missing" to "causal void detection":

1. **Entity Extraction**: Identify method-level primitives in the Second Brain.
2. **Lineage Mapping**: Construct the evolution path of these primitives.
3. **Void Identification**: Detect "unresolved bottlenecks"—points where a known limitation $\mathcal{B}$ exists in the current stack, but the corresponding transformation $\mathcal{T}$ is missing from the knowledge base.

## 🚀 Strategic Impact
- **SNR Optimization**: Filters out noise by focusing on the *evolutionary delta* rather than redundant paper summaries.
- **Predictive Research**: Identifies "likely" next-step breakthroughs by analyzing similar bottleneck resolutions in adjacent domains.
- **Architectural Precision**: Enables the Second Brain to act as a $\text{Causal Map}$ of AI progress.
