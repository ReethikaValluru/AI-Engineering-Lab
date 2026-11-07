# SchemaForge

**Structured extraction** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. preprocessor
2. schema compiler
3. constrained generation
4. validation loop
5. provenance

## API contract

`POST /v1/extract`

The executable reference exposes `run_pipeline(text: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- field precision
- schema validity
- retry rate
- provenance coverage

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
