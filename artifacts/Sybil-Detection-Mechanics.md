# $\text{Behavioral Sybil Detection in Agentic Economies}$

## 1. $\text{Abstract}$
Sybil attacks—the creation of multiple pseudonymous identities to gain disproportionate influence—represent a systemic risk to decentralized agentic economies, particularly in reward distribution and governance. This artifact formalizes the transition from **Identity-based** detection (static) to **Behavioral-based** detection (dynamic), utilizing high-dimensional clustering of agentic traces.

## 2. $\text{Detection Framework: Behavioral Clustering}$
The core objective is to identify "coordination signatures" that distinguish a cluster of Sybils from independent agents.

### 2.1 $\text{Feature Space} \ (\mathcal{F})$
We define a behavioral feature vector $\vec{v}$ for each agent $a$:
$$\vec{v}_a = [ \text{Temporal}, \text{Strategy}, \text{Graph}, \text{Flow} ]$$

- **Temporal Signatures**: 
    - $\text{Entropy}(\text{HourOfDay})$: High coordination often manifests as synchronized activity windows.
    - $\text{BurstRatio}$: Ratio of active-to-idle time, identifying programmatic execution.
- **Strategy Signatures**:
    - $\text{GasPriceCV}$: Coefficient of variation in gas/compute pricing. Sybils typically use a uniform pricing strategy.
    - $\text{Inter-TX-Time}$: Median and variance of time between actions.
- **Graph & Flow Signatures**:
    - $\text{CommonFunder}$: Identification of a "Root-Seed" wallet/account that funds the cluster.
    - $\text{FundingEdgeCount}$: Number of edges connecting to a common source within a temporal window $\Delta t$.

### 2.2 $\text{Clustering Algorithm: HDBSCAN}$
To handle varying cluster densities and noise, we employ **Hierarchical Density-Based Spatial Clustering of Applications with Noise (HDBSCAN)**.
- **Objective**: Group agents $a_i, a_j$ such that the distance $d(\vec{v}_i, \vec{v}_j)$ is minimized across the behavioral manifold.
- **Advantage**: Does not require a pre-specified $k$ (number of clusters), allowing the system to discover an arbitrary number of Sybil rings.

## 3. $\text{Evidence Scoring & Validation}$
A cluster $\mathcal{C}$ is flagged as a Sybil ring if its **Coordination Score** $\mathcal{S}_{coord}$ exceeds a threshold $\tau$:
$$\mathcal{S}_{coord}(\mathcal{C}) = \sum_{i=1}^{n} w_i \cdot \text{Evidence}_i$$
Where $\text{Evidence}_i$ includes:
- **Temporal Correlation**: $\text{Pearson}(\text{ActivityTimeline}_j, \text{ActivityTimeline}_k)$.
- **Funding Concentration**: Percentage of cluster funds originating from $\leq 3$ sources.
- **Sequential Correlation**: Similarity in the sequence of contract interactions (Action-Chain Isomorphism).

## 4. $\text{Architectural Implications for Agentic Trust}$
This behavioral layer complements the $\text{L}_{id} \rightarrow \text{L}_{comp} \rightarrow \text{L}_{rep}$ trust stack:
1. **$\text{L}_{id}$ (Identity)**: Initial registration.
2. **$\text{L}_{comp}$ (Computation)**: Proof of work/stake/contribution.
3. **$\text{L}_{behavior}$ (Behavioral - New)**: Continuous auditing of coordination signatures to detect "dormant" Sybils that activate during critical governance votes.

## 5. $\text{References}$
- `onchain-sybil-detector`: Behavioral clustering framework for EVM wallets.
- `Sybillo`: Open Sybil attack framework.
