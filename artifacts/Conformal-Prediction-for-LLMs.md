# 🛡️ Conformal Prediction ($\text{CP}$) for $\text{LLM}$ Reliability

## 1. Executive Summary
Conformal Prediction ($\text{CP}$) is a framework for uncertainty quantification that transforms probabilistic model outputs into **statistically guaranteed prediction sets**. Unlike standard softmax probabilities, which are often overconfident (calibration drift), $\text{CP}$ provides a distribution-free guarantee that the true label $\text{Y}$ is contained within the prediction set $\Gamma$ with a probability $1 - \alpha$ (e.g., $95\%$), regardless of the underlying data distribution.

## 2. Technical Mechanism
### 2.1 The Non-Conformity Score ($\text{S}$)
The core of $\text{CP}$ is the **non-conformity score**, a measure of how "unusual" a new data point is relative to a calibration set $\mathcal{D}_{cal}$. 
For LLMs, common scores include:
- **Token-Entropy**: $\text{S} = -\sum p(x) \log p(x)$
- **Negative Log-Likelihood (NLL)**: $\text{S} = -\log p(y|x)$
- **Token-Entropy Conformal Prediction ($\text{TECP}$)**: Leveraging token-level entropy to bound the prediction region.

### 2.2 Prediction Set Construction
Given a desired significance level $\alpha \in (0, 1)$, the prediction set $\Gamma$ is constructed as:
$$\Gamma(x) = \{ y \in \mathcal{Y} : \text{S}(x, y) \le \hat{q}_{1-\alpha} \}$$
where $\hat{q}_{1-\alpha}$ is the $(1-\alpha)$-quantile of the scores computed on the calibration set:
$$\hat{q}_{1-\alpha} = \text{Quantile}(\{\text{S}(x_i, y_i) : (x_i, y_i) \in \mathcal{D}_{cal}\}, 1-\alpha)$$

## 3. Application to $\text{LLM}$ Ecosystem
### 3.1 Hallucination Mitigation
By producing a set of possible answers rather than a single greedy token, $\text{CP}$ allows the system to detect **epistemic uncertainty**. If the prediction set $\Gamma$ is excessively large or does not contain a high-confidence answer, the system triggers a "Hallucination Warning" or requests human intervention.

### 3.2 $\text{LLM-as-a-Judge}$ Reliability
Applying $\text{CP}$ to interval evaluations for judges allows the system to quantify the variance in evaluation scores. If the $\text{CP}$ interval for a judge's score is too wide, the evaluation is marked as "Unreliable," preventing noisy signals from corrupting the RLVR/GRPO reward loop.

### 3.3 Adaptive Conformal Prediction
Recent advances ($\text{Adaptive CP}$) allow the quantile $\hat{q}$ to evolve based on recent performance, enabling the model to adapt to domain shifts (e.g., transitioning from general knowledge to specialized medical/legal domains) without full retraining.

## 4. Integration into the Research Flywheel
$\text{CP}$ serves as the mathematical substrate for the **Sensing Layer**:
$$\text{Sensing Trigger} \rightarrow \text{If } |\Gamma(x)| > \tau \text{ or } \text{Confidence}(\Gamma(x)) < \alpha \rightarrow \text{Knowledge Void Detected}$$
This transforms "gap detection" from a semantic search problem into a statistical guarantee problem, effectively operationalizing the **Precision Librarian** objective.

---
**Sources**:
- *Domain-Shift-Aware Conformal Prediction for LLMs* (arXiv:2510.05566)
- *Conformal Prediction for Multi-Choice QA* (arXiv:2305.18404)
- *Adaptive CP for Factuality* (arXiv:2604.13991)
- *TECP: Token-Entropy CP* (arXiv:2509.00461)
