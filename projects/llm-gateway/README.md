# RouteLLM

**Inference routing** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. normalized ingress
2. capability registry
3. multi-objective scorer
4. circuit breaker
5. usage ledger

## API contract

`POST /v1/chat/completions`

The executable reference exposes `run_pipeline(task: str, max_latency_ms: int = 800) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- p95 latency
- availability
- routing regret
- cost/request

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
