from demo import Asset, answer

def test_visual_and_text_evidence_are_ranked():
    items = [Asset("a", "steel fracture", ("crack",)), Asset("b", "sales", ("chart",))]
    assert answer("steel crack", items)["citations"][0] == "a"
