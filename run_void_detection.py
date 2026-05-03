import os
from src.core.gap_detector import GapDetector

detector = GapDetector(knowledge_base_path="~/ai-second-brain/curated_resources.md")
voids = detector.detect_voids()
for v in voids:
    print(f"QUERY: {v['query']} | PRIORITY: {v['priority']} | REASON: {v['reason']}")
