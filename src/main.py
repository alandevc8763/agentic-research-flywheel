import os
from core.gap_detector import GapDetector
from core.researcher import DeepDiveResearcher
from core.distiller import Distiller
from core.sync_manager import SyncManager
from core.state_manager import StateManager

class AgenticResearchFlywheel:
    """The main orchestrator for the autonomous research loop, now supporting 'Elite' distillation."""
    
    def __init__(self):
        self.detector = GapDetector()
        self.researcher = DeepDiveResearcher()
        self.distiller = Distiller()
        self.syncer = SyncManager()
        self.state = StateManager()

    def run_cycle(self):
        """Executes one state-aware, elite rotation of the flywheel."""
        print("🌀 Starting Elite Flywheel Cycle...")
        
        current_state = self.state.load_state()
        
        # 1. Gap Detection (Sensing)
        target = current_state.get("active_target")
        if not target:
            voids = self.detector.detect_voids()
            if not voids:
                print("💤 No knowledge gaps detected. Sleeping...")
                return
            
            for void in voids:
                if void['query'] not in current_state["completed_targets"]:
                    target = void
                    break
            
            if not target:
                print("💤 All detected gaps have already been addressed. Sleeping...")
                return
            
            current_state["active_target"] = target
            self.state.save_state(current_state)
            print(f"🎯 New Target Locked: {target['query']}")

        # 2. Deep-Dive Research (Hunting)
        # Note: In a full implementation, the Researcher would use an LLM to generate 
        # a structured analysis dictionary.
        raw_data = self.researcher.execute_research(target)
        
        # --- MOCKING THE LLM ANALYSIS STEP FOR ELITE DISTILLATION ---
        # In the real cron agent run, the agent will perform this analysis.
        analysis = {
            "name": target['query'],
            "url": raw_data['urls'][0] if raw_data.get('urls') else "https://example.com",
            "taxonomy": "Agentic Architecture", 
            "signal": "Gold", # Example: set to Gold to trigger deep-dive
            "insight": f"A comprehensive deep-dive into {target['query']} revealing a new pattern in autonomous orchestration.",
            "geek_note": "Implemented via a distributed state-machine that reduces latency by 40%.",
            "synergy": "Directly applicable to the LACP memory layer for better state persistence."
        }
        # -----------------------------------------------------------

        # 3. Distillation (Alchemy)
        # Create the elite list entry
        elite_entry = self.distiller.distill(analysis)
        
        # 4. Synchronization (Integration)
        if self.syncer.append_artifact(elite_entry):
            print(f"✅ Integrated {target['query']} via Elite Template.")
            
            # If it's a 'Gold' signal, create a dedicated deep-dive file
            if analysis["signal"] == "Gold":
                deep_dive_content = self.distiller.format_deep_dive(analysis)
                path = self.syncer.create_deep_dive(target['query'], deep_dive_content)
                if path:
                    print(f"💎 Created Gold-tier Deep Dive: {path}")
            
            self.state.mark_completed(target['query'])
        
        if self.syncer.sync_to_remote():
            print("🚀 Elite Flywheel cycle complete. Remote synced.")

if __name__ == "__main__":
    flywheel = AgenticResearchFlywheel()
    flywheel.run_cycle()
