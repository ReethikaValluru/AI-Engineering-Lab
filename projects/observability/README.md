# TraceLens

**LLM observability** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. OTel collectors
2. trace normalization
3. cost attribution
4. SLO engine
5. trace explorer

## API contract

`POST /v1/traces/query`

The executable reference exposes `run_pipeline(spans: list[dict]) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- trace completeness
- p99 latency
- error-budget burn
- cost/trajectory

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
