# VoxAgent

**Realtime voice AI** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. VAD
2. streaming ASR
3. incremental agent
4. tool bus
5. streaming TTS

## API contract

`WS /v1/voice/session`

The executable reference exposes `run_pipeline(transcript: str) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- end-to-end latency
- WER
- barge-in recovery
- task success

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
