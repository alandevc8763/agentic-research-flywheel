# 🧠 Artifact: Neurocognitive Memory Routing & Gating (CraniMem & Cost-Sensitive Routing)

## 📐 Architectural Thesis
The transition from "database-style" agent memory to "cognitively-inspired" memory requires moving beyond simple RAG. The objective is to implement **$\text{Gated-Bounded-Consolidated (GBC)}$** memory flows that minimize distractor interference and optimize the $\text{Accuracy} \leftrightarrow \text{Cost}$ trade-off.

## 🔬 Core Components

### 1. CraniMem: Cranial-Inspired Gated Memory
**Source**: $\text{arXiv:2603.15642v1}$
- **Topology**: 
    - $\text{Episodic Buffer}$: A bounded, near-term continuity layer for immediate task state.
    - $\text{Semantic KG}$: A durable long-term knowledge graph for global recall.
- **Mechanism**: $\text{Consolidation Loop}$. High-utility traces are replayed from the episodic buffer into the KG, while low-utility items are pruned.
- **Outcome**: Increased robustness against "distractor content" compared to Vanilla RAG or Mem0.

### 2. Cost-Sensitive Store Routing
**Source**: $\text{arXiv:2603.15658v1}$
- **Thesis**: Memory retrieval is a **Store-Routing Problem**.
- **Optimization**: $\min(\text{Cost}) \text{ s.t. } \text{Accuracy} \ge \tau$. 
- **Implementation**: A learned router determines which specialized memory stores to query, reducing token overhead and irrelevant context injection.

## 🔗 Synthesis with Second Brain
- **Complement to SRMU**: While $\text{SRMU}$ (arXiv:2604.15121) provides **Relevance-Gated Updates** to prevent memory pollution, $\text{CraniMem}$ provides the **Structural Gating** (Episodic $\rightarrow$ KG) to handle temporal state and noise.
- **Integration Path**: 
    - $\text{L1 (Episodic)}$ $\rightarrow$ Bounded Buffer $\rightarrow$ $\text{L2 (Semantic)}$.
    - $\text{L3 (Global)}$ $\rightarrow$ Cost-Sensitive Router.

## ⚡ Utility Score
- $\text{Actionability}$: High. Can be implemented via a priority-queue buffer and a classification-based router.
- $\text{Architectural Depth}$: High. Formalizes the memory metabolism process.
- $\text{Novelty}$: High. Moves memory from "storage" to "processing".
