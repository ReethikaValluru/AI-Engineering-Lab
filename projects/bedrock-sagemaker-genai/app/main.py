import logging

from botocore.exceptions import BotoCoreError, ClientError
from fastapi import FastAPI, HTTPException

from .config import get_settings
from .models import GenerateRequest, GenerateResponse
from .providers import resolve_provider

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("genai-control-plane")

app = FastAPI(
    title="Bedrock SageMaker GenAI Control Plane",
    version="1.0.0",
    description="Normalized inference gateway for Amazon Bedrock and SageMaker AI.",
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    settings = get_settings()
    try:
        response = resolve_provider(request, settings).generate(request)
    except (BotoCoreError, ClientError, ValueError) as exc:
        logger.exception("inference_failure provider=%s", request.provider)
        raise HTTPException(status_code=502, detail=f"Inference provider failure: {exc}") from exc
    logger.info(
        "inference_success provider=%s model=%s latency_ms=%d trace_id=%s",
        response.provider,
        response.model,
        response.latency_ms,
        response.trace_id,
    )
    return response

