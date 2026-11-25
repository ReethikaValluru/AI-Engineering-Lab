# VisionRAG

A compact multimodal retrieval pipeline that fuses document text with image-derived labels using reciprocal-rank fusion and returns traceable citations.

## Architecture

1. Normalize text and visual metadata into independent retrieval views.
2. Rank each view and combine results with reciprocal-rank fusion.
3. Return grounded evidence IDs and confidence scores.

## Run

```bash
python demo.py
python -m pytest -q
```

Production extensions: replace lexical scoring with CLIP/text embeddings, store vectors in OpenSearch or pgvector, and connect a vision-language model for chart and image understanding.
