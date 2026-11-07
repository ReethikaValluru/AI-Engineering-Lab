# ApproveAgent

**Human-in-the-loop agent** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. state graph
2. typed tools
3. durable checkpoints
4. risk policy
5. approval inbox

## API contract

`POST /v1/agents/runs`

The executable reference exposes `run_pipeline(goal: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- task completion
- tool validity
- approval precision
- recovery success

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
