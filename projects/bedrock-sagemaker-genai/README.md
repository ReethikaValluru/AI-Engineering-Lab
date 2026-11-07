# AWS GenAI Control Plane

Provider-neutral generative inference gateway for **Amazon Bedrock** and **Amazon SageMaker AI** with a deterministic offline provider for CI and local demonstrations.

## Execution topology

`FastAPI ingress → typed provider router → Bedrock Converse | SageMaker InvokeEndpoint | mock → normalized response + telemetry`

## Local demo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

```bash
curl -s http://127.0.0.1:8000/v1/generate \
  -H 'content-type: application/json' \
  -d '{"provider":"mock","prompt":"Explain retrieval-augmented generation.","max_tokens":128}'
```

OpenAPI: `http://127.0.0.1:8000/docs`

## Bedrock execution

```bash
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=amazon.nova-lite-v1:0
aws sts get-caller-identity
uvicorn app.main:app
```

Send `provider=bedrock`. The adapter uses the Bedrock Converse API and normalizes output text, stop reason, usage, request identifier, latency, and guardrail intervention state.

## SageMaker execution

```bash
export AWS_REGION=us-east-1
export SAGEMAKER_ENDPOINT_NAME=my-generative-endpoint
uvicorn app.main:app
```

Send `provider=sagemaker`. The endpoint contract expects the Hugging Face Text Generation Inference JSON projection; modify the payload projection for model-specific containers.

## Deployment

```bash
sam build
sam deploy --guided
```

The SAM template provisions an image-based Lambda HTTP API with resource-scoped `bedrock:InvokeModel` and `sagemaker:InvokeEndpoint` permissions. Production deployments should add WAF, JWT authorization, provisioned concurrency, CloudWatch alarms, X-Ray/OpenTelemetry export, Secrets Manager references, model invocation logging, VPC endpoints, and per-tenant throttling.

## Verification

```bash
ruff check .
pytest -q
docker build -t aws-genai-control-plane .
docker run --rm -p 8000:8000 aws-genai-control-plane
```

## API contract

`POST /v1/generate`

```json
{
  "provider": "bedrock",
  "prompt": "Summarize the incident report.",
  "system": "Return evidence-bounded output.",
  "max_tokens": 256,
  "temperature": 0.2,
  "metadata": {"tenant": "demo"}
}
```

Response fields: `text`, `provider`, `model`, `usage`, `latency_ms`, `trace_id`, `stop_reason`, `guardrail_action`, and `provider_metadata`.

## Security invariants

- resource-scoped IAM actions; no wildcard invoke permissions
- credential resolution through the AWS SDK provider chain; no static secrets
- bounded request lengths and typed validation
- Bedrock Guardrails interception support
- non-root container runtime
- structured request identifiers without prompt-body logging

