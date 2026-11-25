"""GraphWeaver: entity-aware GraphRAG retrieval without external dependencies."""
from collections import defaultdict, deque

class KnowledgeGraph:
    def __init__(self):
        self.edges: dict[str, set[str]] = defaultdict(set)
        self.facts: dict[str, list[str]] = defaultdict(list)

    def add_fact(self, subject: str, relation: str, object_: str) -> None:
        self.edges[subject].add(object_); self.edges[object_].add(subject)
        self.facts[subject].append(f"{subject} {relation} {object_}")

    def neighborhood(self, start: str, depth: int = 2) -> list[str]:
        seen, queue, facts = {start}, deque([(start, 0)]), []
        while queue:
            node, level = queue.popleft()
            facts.extend(self.facts[node])
            if level < depth:
                for nxt in sorted(self.edges[node] - seen):
                    seen.add(nxt); queue.append((nxt, level + 1))
        return list(dict.fromkeys(facts))

def grounded_context(graph: KnowledgeGraph, entity: str) -> dict:
    facts = graph.neighborhood(entity)
    return {"entity": entity, "facts": facts, "grounded": bool(facts)}

if __name__ == "__main__":
    g = KnowledgeGraph(); g.add_fact("NbC", "traps", "hydrogen"); g.add_fact("hydrogen", "weakens", "steel")
    print(grounded_context(g, "NbC"))
