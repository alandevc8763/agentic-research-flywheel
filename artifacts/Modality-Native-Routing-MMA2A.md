# 📡 Modality-Native Routing (MMA2A)

## 📝 Abstract
$\text{MMA2A}$ (Multimodal Agent-to-Agent) is an architectural extension to the $\text{A2A}$ protocol designed to eliminate the **text-bottleneck**—the loss of signal that occurs when multimodal inputs are compressed into text descriptions before being passed between agents. By utilizing $\text{Agent Card}$ capability declarations, $\text{MMA2A}$ routes signals in their native modality (voice, image, text), ensuring that high-fidelity environmental context is preserved for downstream reasoning.

## 🏗️ Architectural Specification

### 1. The Text-Bottleneck Problem
In standard A2A communication, a "Sensing Agent" typically describes a visual or auditory scene in text for a "Reasoning Agent". This $\text{T} \rightarrow \text{T}$ transformation acts as a lossy filter:
$$\text{Signal}_{\text{native}} \xrightarrow{\text{Compression}} \text{Signal}_{\text{text}} \xrightarrow{\text{Reasoning}} \text{Outcome}$$
The compression step discards spatial, spectral, and temporal nuances critical for complex troubleshooting.

### 2. MMA2A Protocol Logic
$\text{MMA2A}$ introduces a routing layer that operates on a capability-discovery mechanism:
1. **Capability Discovery**: Every agent publishes an $\text{Agent Card}$ specifying supported modalities $\mathcal{M} = \{ \text{text, image, audio, video} \}$.
2. **Native Routing**: The router inspects the target agent's $\mathcal{M}$ and the input signal's modality $\mu$.
3. **Dispatch**: If $\mu \in \mathcal{M}_{\text{target}}$, the signal is routed natively; otherwise, it falls back to the text-bottleneck path.

$$\text{Route}(\mu, \mathcal{M}_{\text{target}}) = \begin{cases} \text{Native}(\mu) & \text{if } \mu \in \mathcal{M}_{\text{target}} \\ \text{Compress}(\mu) \rightarrow \text{Text} & \text{otherwise} \end{cases}$$

## 📈 Performance Analysis

### 1. Task Completion Accuracy ($\text{TCA}$)
Evaluated on the $\text{CrossModal-CS}$ benchmark (50 tasks):
- **Text-Bottleneck Baseline**: $32\%$
- **MMA2A Routing**: $52\%$
- **$\Delta\text{TCA}$**: $+20\text{pp}$ (95% bootstrap CI: $[8, 32]$ pp; $p = 0.006$).

### 2. Domain-Specific Gains
The impact is non-uniform, concentrating on vision-dependent tasks:
- **Product Defect Reports**: $+38.5\text{pp}$ gain.
- **Visual Troubleshooting**: $+16.7\text{pp}$ gain.

### 3. The Reasoning Requirement
A critical finding: **Routing alone is insufficient.** Replacing the LLM-backed reasoner with simple keyword matching reduced the accuracy to $36\%$ for both paths. This proves that $\text{MMA2A}$'s utility is a function of the downstream agent's ability to exploit native modality:
$$\text{Utility}(\text{MMA2A}) \propto \text{ReasoningCapability}(\text{Agent}_{\text{downstream}})$$

## ⏱️ Trade-offs
- **Latency**: $\text{MMA2A}$ incurs a $1.8\times$ latency penalty compared to text-bottleneck routing due to the increased computational overhead of native multimodal processing.
- **Complexity**: Requires a standardized $\text{Agent Card}$ registry for efficient routing.

## 🔗 References
- **Paper**: [arXiv:2604.12213](https://arxiv.org/abs/2604.12213)
- **Code**: [vasundras/modality-native-routing-a2a-protocol](https://github.com/vasundras/modality-native-routing-a2a-protocol)
- **Tags**: `#A2A-Protocol` `#Multimodal-AI` `#Agentic-Routing` `#SNR-Optimization`
