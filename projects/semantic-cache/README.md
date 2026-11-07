# SemanticCache

**Embedding cache** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. canonicalization
2. vector encoding
3. partitioned ANN
4. freshness gate
5. quality monitor

## API contract

`POST /v1/cache/lookup`

The executable reference exposes `run_pipeline(query: str, threshold: float = 0.72) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- semantic hit rate
- false-hit rate
- token savings
- staleness

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
