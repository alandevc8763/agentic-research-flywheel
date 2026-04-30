# Knowledge Artifact: Relax (Omni-Modal RL Scaling)

## 🎯 Core Thesis
$\text{Relax}$ (Reinforcement Engine Leveraging Agentic X-modality) operationalizes a high-throughput RL post-training framework specifically engineered for omni-modal models. It addresses the critical $\text{staleness} \leftrightarrow \text{throughput}$ tradeoff in large-scale RL by shifting from synchronous, colocated execution to a decoupled, asynchronous service architecture.

## 🏗️ Architectural Blueprint

### 1. Omni-Native Stack
Unlike retrofitted pipelines, $\text{Relax}$ implements multimodal support as a first-class citizen across the full stack:
- **Modality-Aware Parallelism**: Optimized tensor distribution for heterogeneous inputs (image, audio, video).
- **Integrated Preprocessing**: High-efficiency data loading that prevents the GPU from idling during heavy multimodal tokenization.

### 2. Decoupled Service Layer
Each RL role (Rollout, Learner, Reflector) is deployed as an **independent, fault-isolated service**.
- **Elastic Scaling**: Individual roles can be scaled horizontally based on bottleneck analysis (e.g., scaling Rollout nodes for high-variance trajectories).
- **Zero-Coordination Recovery**: A crashing node is recovered by the orchestrator without requiring a global checkpoint restart.

### 3. TransferQueue Data Bus
The central innovation for throughput scaling:
- **Asynchronous Execution**: Decouples the generation of experience (Rollouts) from the update step (Learner).
- **Tunable Staleness**: A $\text{staleness}$ parameter $\tau$ allows the system to interpolate between:
  - $\tau \to 0$: Strict on-policy execution (high stability, low throughput).
  - $\tau \to \infty$: Fully asynchronous execution (maximal throughput, potential gradient lag).

## 📈 Performance Metrics
- **Throughput Gains**:
  - $1.20\times$ speedup over $\text{veRL}$ (Qwen3-4B on-policy).
  - $2.00\times$ speedup over colocate (Qwen3-Omni-30B fully async).
- **Convergence**: All modes converge to the same reward levels, indicating robustness to asynchronous lag.
- **Efficiency**: Supports $\text{R3}$ (Rollout Routing Replay) for MoE models with minimal overhead ($1.9\%$).

## 🛠️ Utility & Actionability
- **GitHub**: [rednote-ai/Relax](https://github.com/rednote-ai/Relax)
- **Primary Use Case**: Training "Reasoning" capabilities into multimodal models (e.g., creating an Omni-modal DeepSeek-R1 equivalent).
- **Integration Path**: Replace synchronous RL trainers with $\text{Relax}$ to reduce training wall-clock time for multimodal agents.

---
**Tags**: #RL #Omni-Modal #Scaling #Infrastructure #Post-Training
**Source**: [arXiv:2604.11554](https://arxiv.org/abs/2604.11554)
