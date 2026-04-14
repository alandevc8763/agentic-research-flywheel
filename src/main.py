import os
from core.gap_detector import GapDetector
from core.researcher import DeepDiveResearcher
from core.distiller import Distiller
from core.sync_manager import SyncManager

class AgenticResearchFlywheel:
    """The main orchestrator for the autonomous research loop."""
    
    def __init__(self):
        self.detector = GapDetector()
        self.researcher = DeepDiveResearcher()
        self.distiller = Distiller()
        self.syncer = SyncManager()

    def run_cycle(self):
        """Executes one full rotation of the flywheel."""
        print("🌀 Starting Flywheel Cycle...")
        
        # 1. Gap Detection
        voids = self.detector.detect_voids()
        
        for void in voids:
            # 2. Deep-Dive Research
            raw_data = self.researcher.execute_research(void)
            
            # 3. Distillation
            # For MVP, we use a simplified mock result since the actual research 
            # is usually triggered by the high-level Hermes Agent.
            distilled = self.distiller.distill(
                name=void['query'], 
                url=raw_data['urls'][0], 
                description="Automatically distilled via Flywheel Loop"
            )
            
            # 4. Synchronization
            if self.syncer.append_artifact(distilled):
                print(f"✅ Integrated {void['query']} into knowledge base.")
        
        if self.syncer.sync_to_remote():
            print("🚀 Flywheel cycle complete. Remote synced.")

if __name__ == "__main__":
    flywheel = AgenticResearchFlywheel()
    flywheel.run_cycle()
