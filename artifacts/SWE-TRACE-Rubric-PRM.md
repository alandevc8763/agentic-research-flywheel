# Rubric-Based Process Reward Models for Long-Horizon SWE Agents (SWE-TRACE)

## 📌 Core Insight
The primary bottleneck in autonomous Software Engineering (SWE) agents is the reliance on sparse, delayed outcome rewards (pass/fail) which leads to trajectory inflation, reward hacking, and inefficient search. **SWE-TRACE** solves this by optimizing the entire agent lifecycle—from SFT data curation to RL and test-time inference—around **process efficiency** and **rubric-guided supervision**.

## 🛠 Technical Pillars

### 1. Token-Efficient Trajectory Synthesis ($	ext{TETS}$)
Instead of training on raw, noisy teacher rollouts, SWE-TRACE uses **LLM Multi-Task Cascading**:
- **Candidate Generation**: Generates multiple actions per step under specific modes: $\{	ext{localize, inspect, edit, validate, summarize}\}$.
- **Oracle Verification**: A generation-time oracle scores candidates based on:
  $$	ext{Score} = \lambda_1 \Delta	ext{test} + \lambda_2 \Delta	ext{scope} + \lambda_3 \Delta	ext{patch} + \lambda_4 \Delta	ext{info} - \lambda_5 C_{	ext{tok}} - \lambda_6 C_{	ext{red}}$$
- **Shortest-Path Optimization**: Greedily selects the most efficient action, distilling raw trajectories into "shortest-path" SFT samples.

### 2. Rubric-Based Process Reward Model ($	ext{R-PRM}$)
To replace sparse outcome rewards, the system implements a dense, interpretable process signal:
- **Rubric Agent**: Generates an issue-specific rubric $\mathcal{R}_x = \{c_1, \dots, c_K\}$ covering localization, edit constraints, and trajectory discipline.
- **Trajectory Scoring**: The PRM evaluates the full trajectory against the rubric:
  $$s_{	ext{prm}}(	au, \mathcal{R}_x) = \sum_{k=1}^K w_k q_k(	au, c_k)$$
- **Margin-Separated GRPO**: Integrates the PRM score with the execution reward $r_{	ext{exec}}$ using a margin $\gamma \in (0.5, 1)$:
  $$R(	au) = egin{cases} (1-\gamma)s_{	ext{prm}}, & r_{	ext{exec}} = 0 \ \gamma + (1-\gamma)s_{	ext{prm}}, & r_{	ext{exec}} = 1 \end{cases}$$
  This ensures every passing trajectory is strictly preferred over any failing one, while still ranking process quality within each class.

### 3. Heuristic-Guided Test-Time Scaling ($	ext{HG-TTS}$)
Repurposes the trained PRM as an inference-time guide to reduce latency:
- **Action Pruning**: Instead of parallel sampling of $N$ full trajectories, the guide scores candidate next actions $a$:
  $$u_t(a) = s_{	ext{guide}}(h_t, a, \mathcal{R}_x)$$
- **Guided Sampling**: Samples the next action from a distribution adjusted by the guide:
  $$q_t(a | h_t, \mathcal{R}_x) \propto \pi_	heta(a | h_t) \exp(eta u_t(a))$$
- **Efficiency**: Shifts the cost from $O(N \cdot 	ext{Length} \cdot C_{	ext{env}})$ to $O(	ext{Length} \cdot (K \cdot C_{	ext{guide}} + C_{	ext{env}}))$, drastically reducing environment interactions.

### 4. Memory-Augmented Architecture
Handles context explosion in long-horizon tasks by preserving **Verbatim Anchors**:
- **Critical Step Detection**: Uses the PRM to identify steps with high absolute scores or significant score shifts.
- **Non-Abstractive Memory**: Stores the exact action-observation pairs $(a_j, o_j)$ for critical steps $j \in \mathcal{K}_t$, preventing the hallucination and loss of precision associated with summarization.

## 📈 Utility Analysis
- **Actionability**: $	ext{High}$. Provides a clear recipe for building Rubric-Agents and integrating them into GRPO.
- **Architectural Depth**: $	ext{High}$. Formalizes the transition from outcome-based to process-based supervision for agentic workflows.
- **Novelty**: $	ext{High}$. Demonstrates that process-guided guidance is more compute-efficient than brute-force parallel sampling (TTS) in repository-scale environments.

## 🔗 Sources
- **Paper**: [arXiv:2604.14820](https://arxiv.org/abs/2604.14820)
- **Key Concept**: Process-Guided Agentic RL / Rubric-Based PRM
