# SynthFactory

**Synthetic dataset engineering** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. schema controller
2. generation workers
3. privacy filters
4. diversity optimizer
5. lineage registry

## API contract

`POST /v1/datasets/generate`

The executable reference exposes `run_pipeline(rows: int = 5, seed: int = 7) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- schema validity
- diversity
- distribution distance
- PII leakage

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
