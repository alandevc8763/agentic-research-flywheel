import os
import subprocess
from datetime import datetime

class ResearchFlywheelMVP:
    def __init__(self, resources_path="~/ai-second-brain/curated_resources.md"):
        self.resources_path = os.path.expanduser(resources_path)

    def distill_resource(self, name, url, description):
        """
        Distills raw resource info into a structured markdown entry.
        Format: - [Name](URL) - Description
        """
        return f"- [{name}]({url}) - {description}\n"

    def append_to_knowledge_base(self, entry):
        """Appends the distilled entry to the local curated_resources.md."""
        with open(self.resources_path, "a", encoding="utf-8") as f:
            f.write(entry)
        print(f"✅ Resource appended to {self.resources_path}")

    def sync_to_remote(self):
        """Pushes the updated knowledge base to the remote repository."""
        # This assumes the directory is a git repo or we handle the sync via a separate script
        # For MVP, we'll trigger a git push if the path is within a git repo
        try:
            # Find git root
            cwd = os.path.dirname(self.resources_path)
            subprocess.run(["git", "-C", cwd, "add", "."], check=True)
            subprocess.run(["git", "-C", cwd, "commit", "-m", f"auto: sync discovery {datetime.now().isoformat()}"], check=True)
            subprocess.run(["git", "-C", cwd, "push"], check=True)
            print("🚀 Successfully synced to remote GitHub repository.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Sync failed: {e}")

    def run_pipeline(self, discoveries):
        """
        discoveries: List of tuples (name, url, description)
        """
        print(f"🚀 Starting Flywheel MVP Pipeline for {len(discoveries)} discoveries...")
        for name, url, description in discoveries:
            entry = self.distill_resource(name, url, description)
            self.append_to_knowledge_base(entry)
        
        self.sync_to_remote()
        print("✨ Pipeline completed successfully.")

if __name__ == "__main__":
    # Example usage for testing
    flywheel = ResearchFlywheelMVP()
    test_discoveries = [
        ("Agentic Workflow Patterns", "https://example.com/patterns", "A deep dive into iterative agent loops."),
        ("LACP Architecture Spec", "https://example.com/lacp", "Technical specifications for Local Agent Control Plane.")
    ]
    # flywheel.run_pipeline(test_discoveries) # Commented out to avoid spamming during initial setup
    print("Flywheel MVP initialized. Ready for integration with Research Agents.")
