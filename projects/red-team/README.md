# RedTeamBench

**AI security evaluation** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. attack corpus
2. mutation engine
3. target adapter
4. safety graders
5. exploit replay

## API contract

`POST /v1/redteam/campaigns`

The executable reference exposes `run_pipeline(prompts: list[str]) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- attack success rate
- leakage rate
- unsafe tool rate
- coverage

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
