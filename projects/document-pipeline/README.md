# DocFusion

**Document AI** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. quality classifier
2. OCR/layout
3. table extraction
4. reading-order graph
5. semantic export

## API contract

`POST /v1/documents/parse`

The executable reference exposes `run_pipeline(document: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- OCR CER
- table TEDS
- layout mAP
- coverage

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
