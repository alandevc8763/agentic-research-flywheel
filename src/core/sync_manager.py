import os
import subprocess
from datetime import datetime

class SyncManager:
    """The 'Librarian' of the Flywheel: Handles integration and synchronization."""
    
    def __init__(self, resources_path="~/ai-second-brain/curated_resources.md"):
        self.resources_path = os.path.expanduser(resources_path)

    def append_artifact(self, content: str):
        """Appends a distilled knowledge artifact to the local knowledge base."""
        try:
            with open(self.resources_path, "a", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"❌ File append error: {e}")
            return False

    def sync_to_remote(self):
        """Pushes the updated knowledge base to the remote GitHub repository."""
        try:
            cwd = os.path.dirname(self.resources_path)
            subprocess.run(["git", "-C", cwd, "add", "."], check=True)
            subprocess.run(["git", "-C", cwd, "commit", "-m", f"auto: sync discovery {datetime.now().isoformat()}"], check=True)
            subprocess.run(["git", "-C", cwd, "push"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Git sync failed: {e}")
            return False
