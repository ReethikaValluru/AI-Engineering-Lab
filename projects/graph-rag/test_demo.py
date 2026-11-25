from demo import KnowledgeGraph, grounded_context

def test_two_hop_context():
    g = KnowledgeGraph(); g.add_fact("A", "links", "B"); g.add_fact("B", "links", "C")
    assert len(grounded_context(g, "A")["facts"]) == 2
