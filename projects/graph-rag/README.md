# GraphWeaver

An entity-first GraphRAG reference that traverses typed relationships to assemble explainable multi-hop context before generation.

## Run

```bash
python demo.py
python -m pytest -q
```

The dependency-free core makes traversal behavior easy to test. A production version can use Neo4j, automated entity/relation extraction, community summaries, access controls, and LLM synthesis with fact-level citations.
