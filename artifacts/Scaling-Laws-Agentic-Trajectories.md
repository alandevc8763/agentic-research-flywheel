# ⚛️ Research Artifact: Scaling Laws for Agentic Trajectories

## 🧩 Conceptual Framework
The transition from **System 1 (Intuitive)** to **System 2 (Deliberative)** reasoning in LLM agents is governed by the scaling of test-time compute ($\text{TTC}$). While traditional scaling laws focused on model parameters ($\text{N}$) and training tokens ($\text{D}$), agentic scaling laws focus on the interaction between **trajectory depth** and **verification fidelity**.

### $\text{TTC}$ scaling and the "Aha Moment"
As seen in $\text{DeepSeek-R1}$, the emergence of self-correction (the "Aha Moment") is a function of $\text{TTC}$ scaling. When an agent is allowed to generate multiple trajectories ($\text{K}$) and verify them via a Reward Model ($\text{RM}$), the success probability $P(\text{success})$ scales according to:
$$P(\text{success}) \approx 1 - (1 - p)^K$$
where $p$ is the base probability of a single trajectory hitting the correct solution.

## 🛠️ Architectural Implementation
To operationalize agentic scaling, the following patterns are required:

1. **Verification-Guided Search**: Utilizing Process-level Reward Models ($\text{PRM}$) to score intermediate steps, preventing the "drift" common in outcome-only verification.
2. **Trajectory Distillation**: Using On-Policy Distillation (OPD) to transfer the reasoning capabilities discovered during high-$\text{TTC}$ search back into the base model's weights, effectively shifting the "intelligence" from test-time to training-time.
3. **Adaptive Compute Allocation**: Implementing Bayesian routing to allocate more $\text{TTC}$ (more trajectories, deeper search) to high-entropy/complex tasks while maintaining low latency for trivial ones.

## 📉 Signal-to-Noise Analysis
The primary bottleneck in scaling agentic trajectories is the **Verification Gap**. If the RM is imperfect, scaling $K$ (number of trajectories) can lead to "Reward Hacking," where the agent finds high-scoring but incorrect trajectories. 

$$\text{SNR}_{\text{agentic}} = \frac{\text{Fidelity}(\text{RM})}{\text{Entropy}(\text{Trajectories})}$$

Increasing the SNR requires improving the RM's granularity (e.g., moving from ORM $\rightarrow$ PRM).

## 🔗 Integration Path
- **Second Brain**: Append to `curated_resources.md` under "Reasoning-Scaling / System-2".
- **Awesome-AI**: Sync to `content/agent_optimization/scaling_laws_trajectories.md`.

---
**Sources**: 
- DeepSeek-R1 Analysis (Internal)
- "A Survey of On-Policy Distillation for Large Language Models" (arXiv:2604.00626)
- "Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs" (arXiv:2506.19290)
