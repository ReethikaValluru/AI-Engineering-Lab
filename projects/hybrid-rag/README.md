# CiteRAG

**Hybrid RAG** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. semantic chunking
2. BM25+dense retrieval
3. reciprocal-rank fusion
4. cross-encoder reranking
5. citation validation

## API contract

`POST /v1/query`

The executable reference exposes `run_pipeline(query: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- Recall@20
- nDCG@10
- faithfulness
- citation precision

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
