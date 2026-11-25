"""VisionRAG: deterministic multimodal retrieval demo with reciprocal-rank fusion."""
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Asset:
    asset_id: str
    text: str
    visual_labels: tuple[str, ...]

def tokens(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", value.lower()))

def rank(query: str, assets: list[Asset], k: int = 60) -> list[tuple[Asset, float]]:
    q = tokens(query)
    text_rank = sorted(assets, key=lambda a: len(q & tokens(a.text)), reverse=True)
    image_rank = sorted(assets, key=lambda a: len(q & set(a.visual_labels)), reverse=True)
    scores = {a.asset_id: 0.0 for a in assets}
    for ordered in (text_rank, image_rank):
        for i, asset in enumerate(ordered, 1):
            scores[asset.asset_id] += 1 / (k + i)
    return sorted(((a, scores[a.asset_id]) for a in assets), key=lambda x: x[1], reverse=True)

def answer(query: str, assets: list[Asset]) -> dict:
    hits = rank(query, assets)[:2]
    return {"answer": "Evidence found across text and visual metadata.",
            "citations": [a.asset_id for a, _ in hits],
            "scores": [round(score, 4) for _, score in hits]}

if __name__ == "__main__":
    corpus = [Asset("fig-01", "Crack propagation after cyclic loading", ("microscope", "crack", "steel")),
              Asset("table-02", "Model latency and retrieval precision", ("chart", "latency", "precision"))]
    print(answer("steel crack microscope", corpus))
