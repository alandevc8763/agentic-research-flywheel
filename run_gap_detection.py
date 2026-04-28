
import os
import sys
# Add project root to path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.core.gap_detector import GapDetector

detector = GapDetector()
voids = detector.detect_voids()
if not voids:
    print("No voids detected.")
else:
    for i, void in enumerate(voids):
        print(f"{i}: {void['query']} | Priority: {void['priority']} | Reason: {void['reason']}")
