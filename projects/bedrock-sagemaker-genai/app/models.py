from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class Provider(StrEnum):
    MOCK = "mock"
    BEDROCK = "bedrock"
    SAGEMAKER = "sagemaker"


class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=32_000)
    provider: Provider = Provider.MOCK
    system: str | None = Field(default=None, max_length=8_000)
    max_tokens: int = Field(default=256, ge=1, le=4096)
    temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    metadata: dict[str, str] = Field(default_factory=dict)


class Usage(BaseModel):
    input_tokens: int = 0
    output_tokens: int = 0


class GenerateResponse(BaseModel):
    text: str
    provider: Provider
    model: str
    usage: Usage
    latency_ms: int
    trace_id: str
    stop_reason: str | None = None
    guardrail_action: str | None = None
    provider_metadata: dict[str, Any] = Field(default_factory=dict)

