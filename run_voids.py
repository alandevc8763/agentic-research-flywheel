import os
import sys
sys.path.append(os.path.expanduser('~/hermes-projects/research-flywheel/src'))
from core.gap_detector import GapDetector

detector = GapDetector()
voids = detector.detect_voids()
for v in voids:
    print(f"QUERY: {v['query']} | PRIORITY: {v['priority']} | REASON: {v['reason']}")
