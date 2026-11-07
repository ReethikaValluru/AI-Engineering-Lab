# NarrowTune

**Domain small model** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. curated corpus
2. QLoRA adapter
3. preference alignment
4. quantization
5. benchmark service

## API contract

`POST /v1/classify`

The executable reference exposes `run_pipeline(text: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- macro F1
- calibration error
- tokens/s
- quality/dollar

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
