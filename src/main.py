import os
from core.gap_detector import GapDetector
from core.researcher import DeepDiveResearcher
from core.distiller import Distiller
from core.sync_manager import SyncManager
from core.state_manager import StateManager

class AgenticResearchFlywheel:
    """The main orchestrator for the autonomous research loop."""
    
    def __init__(self):
        self.detector = GapDetector()
        self.researcher = DeepDiveResearcher()
        self.distiller = Distiller()
        self.syncer = SyncManager()
        self.state = StateManager()

    def run_cycle(self):
        """Executes one state-aware rotation of the flywheel."""
        print("🌀 Starting State-Aware Flywheel Cycle...")
        
        current_state = self.state.load_state()
        
        # 1. Gap Detection (Sensing)
        # If there's an active target, we continue it; otherwise, we find a new one.
        target = current_state.get("active_target")
        
        if not target:
            voids = self.detector.detect_voids()
            if not voids:
                print("💤 No knowledge gaps detected. Sleeping...")
                return
            
            # Pick the highest priority void that hasn't been completed
            for void in voids:
                if void['query'] not in current_state["completed_targets"]:
                    target = void
                    break
            
            if not target:
                print("💤 All detected gaps have already been addressed. Sleeping...")
                return
            
            # Set as active target
            current_state["active_target"] = target
            self.state.save_state(current_state)
            print(f"🎯 New Target Locked: {target['query']}")

        # 2. Deep-Dive Research (Hunting)
        raw_data = self.researcher.execute_research(target)
        
        # 3. Distillation (Alchemy)
        # In a full implementation, this uses the distilled protocol defined in DESIGN.md
        distilled = self.distiller.distill(
            name=target['query'], 
            url=raw_data['urls'][0] if raw_data.get('urls') else "https://example.com", 
            description="Automatically distilled via State-Aware Flywheel Loop"
        )
        
        # 4. Synchronization (Integration)
        if self.syncer.append_artifact(distilled):
            print(f"✅ Integrated {target['query']} into knowledge base.")
            # Mark as completed to move to the next gap in the next run
            self.state.mark_completed(target['query'])
        
        if self.syncer.sync_to_remote():
            print("🚀 Flywheel cycle complete. Remote synced.")

if __name__ == "__main__":
    flywheel = AgenticResearchFlywheel()
    flywheel.run_cycle()
