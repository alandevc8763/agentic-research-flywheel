# 🧩 Mesh Memory Protocol (MMP): Semantic Infrastructure for Collective Intelligence

## 🌌 Abstract
The **Mesh Memory Protocol (MMP)** shifts the paradigm of multi-agent coordination from *data exchange* (message passing) to *cognitive remixing*. Instead of sharing raw state or documents, agents exchange **Cognitive Memory Blocks (CMBs)** which are processed through the receiver's domain-specific lens to produce new, emergent understanding.

$$\text{Signal} \xrightarrow{\text{SVAF}} \text{Domain Filter} \xrightarrow{\text{Remix}} \text{Emergent Knowledge}$$

---

## 🏗️ Architectural Framework

### 1. The CAT7 Schema (Cognitive Memory Blocks)
MMP defines an immutable 7-field basis for all cognitive units. This near-orthogonal basis spans three axes of communication: **Subject**, **Intent**, and **Affect**.

| Index | Field | Axis | Captures |
| :--- | :--- | :--- | :--- |
| 0 | `focus` | Subject | Central topic/subject of the observation. |
| 1 | `issue` | Tension | Gaps, risks, assumptions, or open questions. |
| 2 | `intent` | Goal | Desired change, purpose, or objective. |
| 3 | `motivation` | Why | Drivers, incentives, or underlying reasons. |
| 4 | `commitment` | Promise | Specific actions, deadlines, or obligations. |
| 5 | `perspective` | Vantage | Viewpoint or situational context. |
| 6 | `mood` | Affect | Emotional valence and arousal (cross-domain signal). |

### 2. SVAF: Symbolic-Vector Attention Fusion (Layer 4)
SVAF is the gating mechanism that determines if an incoming CMB is worth processing. It prevents "paraphrase accumulation" and ensures high signal-to-noise ratios.

#### $\text{Evaluation Logic}$
The system computes a $\text{totalDrift}$ combining field-level semantic distance and temporal decay:
$$\text{totalDrift} = (1 - \lambda) \cdot \frac{\sum(\alpha_f \cdot \delta_f)}{\sum \alpha_f} + \lambda \cdot (1 - e^{-\text{age}/\tau})$$

Where:
- $\delta_f$: Cosine distance between incoming field and local anchor.
- $\alpha_f$: Per-agent field weight (defines the agent's "interest").
- $\lambda$: Temporal weighting factor.

#### $\text{The Band-Pass Decision Model}$
Signals are categorized into four states based on their $\text{totalDrift}$:
1. **Redundant**: $\max(\delta_f) < T_{\text{redundant}} \rightarrow$ Discard (Zero information gain).
2. **Aligned**: $\text{totalDrift} \le T_{\text{aligned}} \rightarrow$ High-confidence integration.
3. **Guarded**: $T_{\text{aligned}} < \text{totalDrift} \le T_{\text{guarded}} \rightarrow$ Conditional integration (Low confidence).
4. **Rejected**: $\text{totalDrift} > T_{\text{guarded}} \rightarrow$ Discard (Irrelevant/Noise).

### 3. The Remix Mechanism & Lineage
MMP prohibits the storage of raw peer signals. Agents must **Remix** accepted signals into a new CMB reflecting their own domain understanding.

**The Remix Chain (DAG):**
Every remixed CMB carries a lineage metadata object:
- $\text{parents}$: Direct parent CMB keys.
- $\text{ancestors}$: Full chain $\text{union}(\text{parent.ancestors}) + \text{parent.keys}$ (capped at 50).
- $\text{method}$: The fusion algorithm used (e.g., `SVAF-v2`).

This transforms the memory of the mesh into a **Directed Acyclic Graph (DAG)** of evolving intelligence, allowing $O(1)$ detection of influence across the network.

---

## 🚀 Utility Analysis

### $\text{Actionability}$
- **Protocol Implementation**: Can be deployed as a middleware layer between LLM agents.
- **Memory Management**: Replaces flat vector stores with a structured, lineage-aware graph.
- **Cross-Domain Triggering**: The `mood` field allows high-level affective signals (e.g., "User is fatigued") to trigger actions in unrelated domains (e.g., Music Agent $\rightarrow$ Ambient Playlist) without needing to understand the domain-specific `focus` (e.g., "Debugging C++ memory leak").

### $\text{Architectural Depth}$
MMP solves the **Echo Chamber Problem** in multi-agent systems by ensuring that agents only store their *understanding* of a signal, not the signal itself, thus preventing the mindless replication of tokens across the mesh.

### $\text{Novelty}$
Introduces the concept of **Semantic Infrastructure**—treating the communication protocol as a cognitive process rather than a transport mechanism.

---

## 📚 References
- **Paper**: [arXiv:2604.19540](https://arxiv.org/abs/2604.19540) - *Mesh Memory Protocol: Semantic Infrastructure for Multi-Agent LLM Systems*
- **Spec**: [sym.bot/spec/mmp](https://sym.bot/spec/mmp)
