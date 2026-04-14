# Project: Agentic Research Flywheel

## 1. Vision
To transform AI research from a manual, episodic task into a continuous, autonomous, and self-evolving loop that feeds a high-fidelity "Second Brain".

## 2. Architecture
The system consists of four primary modules:

### A. Gap Detector (The "Senses")
- **Input**: Current Knowledge Graph / `curated_resources.md`.
- **Process**: Semantic analysis to identify "knowledge voids" or outdated entries.
- **Output**: A set of `ResearchTarget` objects (Query, Context, Priority).

### B. Deep-Dive Agent (The "Hunter")
- **Input**: `ResearchTarget`.
- **Process**: 
  - Multi-step web research.
  - Vision-guided scraping of technical documentation.
  - Cross-referencing multiple sources.
- **Output**: Raw `DiscoveryDataset` (Links, Snippets, Metadata).

### C. Distillation Engine (The "Alchemist")
- **Input**: `DiscoveryDataset`.
- **Process**: 
  - Noise filtering.
  - Mapping to LLM-Wiki schema (Entity $\rightarrow$ Relation $\rightarrow$ Attribute).
  - Formatting for Markdown/MkDocs.
- **Output**: `KnowledgeArtifact` (Structured Markdown).

### D. Sync Manager (The "Librarian")
- **Input**: `KnowledgeArtifact`.
- **Process**: 
  - Local file update in `~/ai-second-brain`.
  - Git commit and push to `awesome-ai-discoveries`.
- **Output**: Updated public and private knowledge bases.

## 3. Implementation Roadmap

### Phase 1: MVP (The Linear Pipe)
- [ ] Implement basic `Search $\rightarrow$ Format $\rightarrow$ Push` pipeline.
- [ ] Create a standard "Discovery Template" for curated resources.
- [ ] Verify end-to-end flow from a single trigger to GitHub.

### Phase 2: Cognitive (The Gap Detector)
- [ ] Integrate with `Second Brain` graph to detect missing topics.
- [ ] Implement automated query generation based on knowledge gaps.

### Phase 3: Evolutionary (The Feedback Loop)
- [ ] Implement trajectory logging for research runs.
- [ ] Create a feedback mechanism where user ratings refine search strategies.
- [ ] Autonomous refinement of "Distillation" prompts.

## 4. Success Metrics
- **Signal-to-Noise Ratio**: Percentage of discovered resources that are actually integrated into the Second Brain.
- **Knowledge Growth Rate**: Number of new, high-value entities added to the graph per week.
- **Autonomy Level**: Ratio of autonomous discoveries vs. user-triggered research.
