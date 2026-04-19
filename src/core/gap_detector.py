import os
import re
from collections import Counter

class GapDetector:
    """The 'Senses' of the Flywheel: Identifies knowledge voids in the Second Brain."""
    
    def __init__(self, knowledge_base_path="~/ai-second-brain/curated_resources.md"):
        self.kb_path = os.path.expanduser(knowledge_base_path)

    def _extract_entities(self, text):
        """Extracts potential technical entities (Acronyms, LaTeX terms, Capitalized Terms)."""
        entities = set()
        # 1. LaTeX notation: $\text{...}$
        latex_matches = re.findall(r"\\\text{\\?([a-zA-Z0-9\-\s_\(\)]+)}", text)
        entities.update(latex_matches)
        
        # 2. Acronyms: 3+ uppercase letters
        acronym_matches = re.findall(r"\b[A-Z]{3,}\b", text)
        entities.update(acronym_matches)
        
        # 3. Proper nouns/Technical terms: Capitalized words (excluding start of sentence)
        # Simple heuristic: sequences of capitalized words not at the very start of a line
        proper_matches = re.findall(r"(?<!^)\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)\b", text)
        entities.update(proper_matches)
        
        return entities

    def detect_voids(self):
        """
        Analyzes the current knowledge base to find gaps via Dependency Mapping.
        Identifies entities that are mentioned but do not have their own dedicated entry.
        """
        print("🧠 Scanning knowledge base for voids via Dependency Mapping...")
        
        if not os.path.exists(self.kb_path):
            print(f"❌ Knowledge base not found at {self.kb_path}")
            return []

        with open(self.kb_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Identify existing entries (headers starting with ### 🌀)
        existing_entries = re.findall(r"### 🌀 \[([^\]]+)\]", content)
        entry_names = {name.lower() for name in existing_entries}

        # Extract all mentioned entities from the entire document
        all_entities = self._extract_entities(content)
        
        voids = []
        for entity in all_entities:
            # If the entity is mentioned but not a primary entry
            if entity.lower() not in entry_names and len(entity) > 2:
                voids.append({
                    "query": entity,
                    "priority": 0.7, # Default priority for mentioned-but-undefined
                    "reason": f"Entity '{entity}' is referenced in the Second Brain but lacks a dedicated distilled entry."
                })

        # Sort by some heuristic or return top N
        return voids[:10]
