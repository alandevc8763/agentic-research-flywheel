import json
import os

class StateManager:
    """Handles the persistence of the Flywheel's current research state."""
    
    def __init__(self, state_file="~/hermes-projects/research-flywheel/.flywheel_state"):
        self.state_file = os.path.expanduser(state_file)

    def load_state(self) -> dict:
        """Loads the current state from the file."""
        if not os.path.exists(self.state_file):
            return {"active_target": None, "completed_targets": [], "last_update": None}
        try:
            with open(self.state_file, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading state: {e}")
            return {"active_target": None, "completed_targets": [], "last_update": None}

    def save_state(self, state: dict):
        """Saves the current state to the file."""
        try:
            with open(self.state_file, "w") as f:
                json.dump(state, f, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving state: {e}")

    def mark_completed(self, target_query: str):
        """Marks a target as completed to avoid redundant research."""
        state = self.load_state()
        if target_query not in state["completed_targets"]:
            state["completed_targets"].append(target_query)
            state["active_target"] = None
            self.save_state(state)
