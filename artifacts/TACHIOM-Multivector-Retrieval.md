# TACHIOM: Token-Aware Clustering for Efficient Multivector Retrieval

## 1. Architectural Core
TACHIOM addresses the scalability bottleneck of multivector retrieval models (e.g., ColBERT) where the memory and computational cost of storing and searching token-level embeddings are prohibitive. 

The system replaces standard $\kappa\text{-means}$ clustering with a **Token-Aware Centroid Allocation** mechanism. While $\kappa\text{-means}$ favors frequent tokens and scales poorly, TACHIOM exploits the underlying token distribution to scale to millions of centroids, enabling high-fidelity document scoring using only centroid proxies.

### 1.1 The TACHIOM Pipeline
$$\text{Token Embeddings} \xrightarrow{\text{Token-Aware Clustering}} \text{Centroid-based Index} \xrightarrow{\text{Graph-based Retrieval}} \text{PQ-refined Scoring}$$

## 2. Technical Innovations

### 2.1 Token-Aware Clustering
Standard clustering ignores the semantic rarity of tokens. TACHIOM implements a distribution-aware allocation that prevents "centroid collapse" on frequent tokens, ensuring that discriminative, rare tokens maintain high-resolution representation.
- **Scaling**: Achieves up to $247\times$ faster clustering than $\kappa\text{-means}$.
- **Resolution**: Supports millions of centroids without the quadratic overhead of traditional Lloyd's algorithm.

### 2.2 Hierarchical Retrieval Index
To optimize the "Gather" phase of the late-interaction process:
1. **Centroid Graph**: Implements a graph-based index over the centroids to rapidly prune the search space.
2. **Optimized Product Quantization (PQ)**: Uses a specialized PQ layout for the residual vectors, minimizing memory footprint while maintaining $\text{MaxSim}$ accuracy.
3. **Centroid-Only Scoring**: Enables an initial high-accuracy pass using only centroid assignments, bypassing token-level computation for non-candidate documents.

## 3. Performance Metrics ($\text{KPIs}$)
- **Retrieval Speedup**: Up to $9.8\times$ faster than state-of-the-art multivector retrieval systems.
- **Clustering Efficiency**: $247\times$ acceleration in the index construction phase.
- **Effectiveness**: Maintains comparable or superior NDCG/Recall on MS-MARCOv1 and LoTTE benchmarks.

## 4. Synthesis for Second Brain
TACHIOM represents a critical shift from *probabilistic approximation* to *structural exploitation* in vector databases. By treating token distribution as a first-class citizen in the clustering process, it enables the deployment of Late Interaction models at a scale previously reserved for single-vector dense retrievers.

**Tags**: #InformationRetrieval #MultivectorRetrieval #LateInteraction #Tachiom #VectorQuantization #Efficiency
**Source**: [arXiv:2604.28142](https://arxiv.org/abs/2604.28142)
