# LocalServe

**Self-hosted inference** reference implementation with a deterministic execution harness, typed data contracts, production architecture, acceptance criteria, and zero-credential local verification.

## Architecture

1. artifact registry
2. GPU workers
3. continuous batching
4. paged KV cache
5. compatible API

## API contract

`POST /v1/chat/completions`

The executable reference exposes `run_pipeline(prompts: list[str], gpu_memory_gb: int = 24) -> dict`. The deterministic adapter isolates core orchestration semantics; replace in-memory primitives with the production services defined above without changing the contract.

## Working demo

```bash
python demo.py
python -m unittest -v test_demo.py
```

## Acceptance metrics

- TTFT
- TPOT
- tokens/s
- GPU utilization

## Production hardening

Instrument OpenTelemetry spans, enforce schema validation and tenant isolation, add bounded retries and circuit breakers, persist versioned artifacts, execute adversarial evaluation, and gate promotion on statistical thresholds.
