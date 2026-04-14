class Distiller:
    """The 'Alchemist' of the Flywheel: Transforms raw data into high-signal, elite artifacts."""
    
    def __init__(self, protocol="elite"):
        self.protocol = protocol

    def distill(self, data: dict) -> str:
        """
        Transforms a structured analysis dictionary into an 'Elite' markdown entry.
        Expected data keys: name, url, taxonomy, signal, insight, geek_note, synergy.
        """
        name = data.get("name", "Unknown Resource")
        url = data.get("url", "#")
        taxonomy = data.get("taxonomy", "General")
        signal = data.get("signal", "Bronze")
        insight = data.get("insight", "No insight provided.")
        geek_note = data.get("geek_note", "No technical notes.")
        synergy = data.get("synergy", "No direct synergy identified.")

        # Signal Emoji Mapping
        signal_map = {
            "Gold": "Gold $\text{💎}$",
            "Silver": "Silver $\text{🥈}$",
            "Bronze": "Bronze $\text{🥉}$"
        }
        signal_display = signal_map.get(signal, signal)

        # Elite Template
        template = (
            f"### 🌀 [{name}]({url})\n"
            f"**$\\text{{Taxonomy}}$**: $\\text{{{taxonomy}}}$ | **$\\text{{Signal}}$**: {signal_display}\n"
            f"- **$\\text{{Core Insight}}$**: {insight}\n"
            f"- **$\\text{{Geek Note}}$**: {geek_note}\n"
            f"- **$\\text{{Synergy}}$**: {synergy}\n"
        )
        return template

    def format_deep_dive(self, data: dict) -> str:
        """
        Creates a full-page professional analysis for 'Gold' resources.
        """
        name = data.get("name", "Unknown Resource")
        url = data.get("url", "#")
        
        content = (
            f"# 💎 Deep Dive: {name}\n\n"
            f"**Source**: {url}\n"
            f"**Taxonomy**: {data.get('taxonomy', 'General')}\n"
            f"**Signal Level**: {data.get('signal', 'Gold')}\n\n"
            f"--- \n\n"
            f"## 🎯 Core Architecture Insight\n{data.get('insight', '...')}\n\n"
            f"## 🛠️ Technical Deep-Dive (Geek Notes)\n{data.get('geek_note', '...')}\n\n"
            f"## 🔗 Ecosystem Synergy\n{data.get('synergy', '...')}\n\n"
            f"--- \n"
            f"*Automatically analyzed and distilled by the Agentic Research Flywheel.*"
        )
        return content
