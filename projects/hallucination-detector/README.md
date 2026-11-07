# ClaimGuard

**Factuality verification** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. claim segmentation
2. evidence retrieval
3. NLI scoring
4. authority weighting
5. policy gate

## API contract

`POST /v1/verify`

The executable reference exposes `run_pipeline(answer: str, evidence: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- unsupported-claim recall
- precision
- AUROC
- false-block rate

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
