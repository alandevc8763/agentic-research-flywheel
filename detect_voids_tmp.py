
import sys
import os
# Add the src directory to sys.path
sys.path.append(os.path.join(os.getcwd(), 'src'))
from core.gap_detector import GapDetector

kb_path = os.path.expanduser("~/ai-second-brain/curated_resources.md")
detector = GapDetector(knowledge_base_path=kb_path)
voids = detector.detect_voids()

for v in voids:
    print(f"VOID: {v['query']} | Priority: {v['priority']} | Reason: {v['reason']}")
