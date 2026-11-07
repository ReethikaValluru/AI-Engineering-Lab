import json
import time
from abc import ABC, abstractmethod
from typing import Any
from uuid import uuid4

import boto3

from .config import Settings
from .models import GenerateRequest, GenerateResponse, Provider, Usage


class InferenceProvider(ABC):
    @abstractmethod
    def generate(self, request: GenerateRequest) -> GenerateResponse: ...


class MockProvider(InferenceProvider):
    def generate(self, request: GenerateRequest) -> GenerateResponse:
        started = time.perf_counter()
        text = f"[offline-demo] {request.prompt.strip()}"
        return GenerateResponse(
            text=text,
            provider=Provider.MOCK,
            model="deterministic-mock-v1",
            usage=Usage(
                input_tokens=max(1, len(request.prompt) // 4),
                output_tokens=max(1, len(text) // 4),
            ),
            latency_ms=max(1, int((time.perf_counter() - started) * 1000)),
            trace_id=f"tr_{uuid4().hex}",
            stop_reason="end_turn",
            guardrail_action="none",
        )


class BedrockProvider(InferenceProvider):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.client = boto3.client("bedrock-runtime", region_name=settings.aws_region)

    def generate(self, request: GenerateRequest) -> GenerateResponse:
        started = time.perf_counter()
        kwargs: dict[str, Any] = {
            "modelId": self.settings.bedrock_model_id,
            "messages": [{"role": "user", "content": [{"text": request.prompt}]}],
            "inferenceConfig": {
                "maxTokens": request.max_tokens,
                "temperature": request.temperature,
            },
        }
        if request.system:
            kwargs["system"] = [{"text": request.system}]
        if self.settings.bedrock_guardrail_id:
            kwargs["guardrailConfig"] = {
                "guardrailIdentifier": self.settings.bedrock_guardrail_id,
                "guardrailVersion": self.settings.bedrock_guardrail_version,
                "trace": "enabled",
            }
        result = self.client.converse(**kwargs)
        usage = result.get("usage", {})
        content = result.get("output", {}).get("message", {}).get("content", [])
        text = "".join(part.get("text", "") for part in content)
        metadata = result.get("ResponseMetadata", {})
        return GenerateResponse(
            text=text,
            provider=Provider.BEDROCK,
            model=self.settings.bedrock_model_id,
            usage=Usage(
                input_tokens=usage.get("inputTokens", 0),
                output_tokens=usage.get("outputTokens", 0),
            ),
            latency_ms=int((time.perf_counter() - started) * 1000),
            trace_id=metadata.get("RequestId", f"tr_{uuid4().hex}"),
            stop_reason=result.get("stopReason"),
            guardrail_action="intervened" if result.get("stopReason") == "guardrail_intervened" else "none",
            provider_metadata={"metrics": result.get("metrics", {})},
        )


class SageMakerProvider(InferenceProvider):
    def __init__(self, settings: Settings):
        if not settings.sagemaker_endpoint_name:
            raise ValueError("SAGEMAKER_ENDPOINT_NAME is required")
        self.settings = settings
        self.client = boto3.client("sagemaker-runtime", region_name=settings.aws_region)

    def generate(self, request: GenerateRequest) -> GenerateResponse:
        started = time.perf_counter()
        payload = {
            "inputs": request.prompt,
            "parameters": {
                "max_new_tokens": request.max_tokens,
                "temperature": request.temperature,
                "return_full_text": False,
            },
        }
        result = self.client.invoke_endpoint(
            EndpointName=self.settings.sagemaker_endpoint_name,
            ContentType="application/json",
            Accept="application/json",
            Body=json.dumps(payload).encode(),
        )
        decoded = json.loads(result["Body"].read())
        item = decoded[0] if isinstance(decoded, list) else decoded
        text = item.get("generated_text") or item.get("generation") or str(item)
        return GenerateResponse(
            text=text,
            provider=Provider.SAGEMAKER,
            model=self.settings.sagemaker_endpoint_name,
            usage=Usage(input_tokens=max(1, len(request.prompt) // 4), output_tokens=max(1, len(text) // 4)),
            latency_ms=int((time.perf_counter() - started) * 1000),
            trace_id=result.get("ResponseMetadata", {}).get("RequestId", f"tr_{uuid4().hex}"),
            stop_reason="end_turn",
            provider_metadata={"custom_attributes": result.get("CustomAttributes")},
        )


def resolve_provider(request: GenerateRequest, settings: Settings) -> InferenceProvider:
    if request.provider == Provider.MOCK:
        return MockProvider()
    if request.provider == Provider.BEDROCK:
        return BedrockProvider(settings)
    return SageMakerProvider(settings)

