
import os
import sys
sys.path.append('/home/alan/hermes-projects/research-flywheel')
from src.core.gap_detector import GapDetector

detector = GapDetector()
voids = detector.detect_voids()
for v in voids:
    print(f"QUERY: {v['query']} | REASON: {v['reason']}")
