
import os
from core.gap_detector import GapDetector

detector = GapDetector()
voids = detector.detect_voids()

if not voids:
    print("No voids detected.")
else:
    for i, void in enumerate(voids):
        print(f"{i+1}. Query: {void['query']} | Priority: {void['priority']} | Reason: {void['reason']}")
