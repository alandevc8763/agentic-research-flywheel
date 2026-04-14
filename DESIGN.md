# Technical Specification: Agentic Research Flywheel

## 1. System Philosophy
The Flywheel is based on the principle of **"Closed-Loop Intelligence"**. It assumes that knowledge is not a destination but a dynamic frontier. The system's primary goal is to maintain the **maximal signal-to-noise ratio** ($\text{SNR}$) of the Second Brain while ensuring **continuous expansion**.

---

## 2. Detailed Architectural Flow

### 2.1 Data Pipeline ($\text{DP}$)
The data flow is defined as a series of transformations:
$$\text{KnowledgeVoid} \xrightarrow{\text{ResearchAgent}} \text{DiscoveryDataset} \xrightarrow{\text{Distiller}} \text{KnowledgeArtifact} \xrightarrow{\text{SyncManager}} \text{KnowledgeGraph}$$

### 2.2 Module Deep-Dive

#### A. Gap Detector (The Sensing Layer)
**Objective**: Transform a static knowledge base into a set of active research targets.
- **Detection Logic**:
  - **Semantic Void Analysis**: Using embeddings to find "white spaces" in the latent space of the current knowledge base.
  - **Dependency Mapping**: Identifying concepts that are referenced but not defined (e.g., a mention of "LACP" without a detailed architecture entry).
  - **Freshness Check**: Using timestamps to identify resources that may have evolved (e.g., new LLM model releases).
- **Output**: `ResearchTarget` $\rightarrow$ `{query: str, context: str, priority: float, reason: str}`.

#### B. Deep-Dive Agent (The Acquisition Layer)
**Objective**: Maximize the recall of high-signal information.
- **Strategy**:
  - **Breadth-First Search**: Initial scan for top-tier resources.
  - **Depth-First Extraction**: Deep-diving into specific documentation, codebases, or papers.
  - **Cross-Reference Validation**: If Source A and Source B agree on a technical detail, it is promoted to "High Confidence".
- **Output**: `DiscoveryDataset` $\rightarrow$ `{raw_text: list, urls: list, metadata: dict}`.

#### C. Distillation Engine (The Refinement Layer)
**Objective**: Transform raw data into structured wisdom.
- **The Distillation Protocol**:
  1. **De-noising**: Remove marketing adjectives, redundant introductions, and boilerplate.
  2. **Entity Extraction**: Identify core concepts, their attributes, and their relationships.
  3. **Utility Scoring**: Evaluate the finding based on:
     - $\text{Actionability}$: Can this be implemented or used?
     - $\text{Architectural Depth}$: Does it explain the "why" or just the "what"?
     - $\text{Novelty}$: Does it provide a new perspective?
  4. **Formatting**: Apply a rigid Markdown template for consistent integration.
- **Output**: `KnowledgeArtifact` $\rightarrow$ `{title: str, content: str, tags: list, sources: list}`.

#### D. Sync Manager (The Integration Layer)
**Objective**: Ensure atomic and consistent updates to the knowledge base.
- **Collision Detection**: Checking if the new artifact overlaps with existing entries.
- **Merging Logic**: If overlap exists, the system performs a `merge` rather than an `overwrite`, synthesizing the two perspectives.
- **Distribution**: 
  - $\text{Local}$ $\rightarrow$ `~/ai-second-brain` (Full fidelity).
  - $\text{Remote}$ $\rightarrow$ `awesome-ai-discoveries` (Curated, public version).

---

## 3. Feedback Loops (The "Flywheel" Effect)
The system is not a linear pipe but a circle:
1. **Update Loop**: Sync $\rightarrow$ Knowledge Graph $\rightarrow$ Gap Detector. (New knowledge creates new gaps).
2. **Refinement Loop**: User Feedback $\rightarrow$ Distillation Prompt $\rightarrow$ Better Artifacts.
3. **Strategy Loop**: Success Metric $\rightarrow$ Research Strategy $\rightarrow$ Better Discovery.

---

## 4. Success Metrics ($\text{KPIs}$)
- **Signal Density**: $\frac{\text{Integrated Tokens}}{\text{Processed Tokens}}$.
- **Frontier Expansion**: Number of new unique entities added to the Knowledge Graph per cycle.
- **Autonomous Efficiency**: Time taken from Gap Detection to Sync without human intervention.

---

## 5. Future Expansion
- **Multi-Agent Debate**: Implementing a "Critic Agent" to challenge the distillation results before they are synced.
- **Real-time Triggering**: Integrating with RSS feeds or GitHub Webhooks to trigger the flywheel instantly upon a new discovery.
