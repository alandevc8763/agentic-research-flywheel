import os
import subprocess
from datetime import datetime

class SyncManager:
    """The 'Librarian' of the Flywheel: Handles integration and synchronization."""
    
    def __init__(self, resources_path="~/ai-second-brain/curated_resources.md", deep_dive_dir="~/ai-second-brain/wiki/research"):
        self.resources_path = os.path.expanduser(resources_path)
        self.deep_dive_dir = os.path.expanduser(deep_dive_dir)
        
        # Ensure deep dive directory exists
        os.makedirs(self.deep_dive_dir, exist_ok=True)

    def append_artifact(self, content: str):
        """Appends a distilled knowledge artifact to the local curated_resources.md."""
        try:
            with open(self.resources_path, "a", encoding="utf-8") as f:
                f.write(content + "\n\n") # Add spacing between elite entries
            return True
        except Exception as e:
            print(f"❌ File append error: {e}")
            return False

    def create_deep_dive(self, name: str, content: str):
        """Creates a detailed analysis file for high-signal resources."""
        # Sanitize filename
        safe_name = "".join([c for c in name if c.isalnum() or c in (' ', '_', '-')]).rstrip()
        filename = f"{safe_name.replace(' ', '_').lower()}.md"
        filepath = os.path.join(self.deep_dive_dir, filename)
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return filepath
        except Exception as e:
            print(f"❌ Deep dive creation failed: {e}")
            return None

    def sync_to_remote(self):
        """Pushes the updated knowledge base to the remote repository."""
        try:
            # We need to find the git root of the Second Brain repo
            # For this implementation, we assume it's in ~/ai-second-brain
            cwd = os.path.expanduser("~/ai-second-brain")
            subprocess.run(["git", "-C", cwd, "add", "."], check=True)
            subprocess.run(["git", "-C", cwd, "commit", "-m", f"auto: sync elite discovery {datetime.now().isoformat()}"], check=True)
            subprocess.run(["git", "-C", cwd, "push"], check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Git sync failed: {e}")
            return False
