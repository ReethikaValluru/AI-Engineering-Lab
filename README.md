# AI Engineering Lab

Twenty-one executable, production-oriented AI engineering reference systems spanning retrieval, evaluation, inference, safety, observability, agentic orchestration, multimodal processing, dataset engineering, model monitoring, and AWS-native Generative AI.

## Project catalog

| # | Project | Technical scope |
|---:|---|---|
| 01 | [CiteRAG](projects/hybrid-rag/README.md) | Hybrid retrieval, RRF, reranking, cited synthesis |
| 02 | [EvalGate](projects/eval-pipeline/README.md) | Regression evaluation and release gating |
| 03 | [RouteLLM](projects/llm-gateway/README.md) | Capability/cost/latency-aware inference routing |
| 04 | [SemanticCache](projects/semantic-cache/README.md) | Similarity lookup, TTL and collision controls |
| 05 | [NarrowTune](projects/small-model/README.md) | Domain specialization and quantized serving |
| 06 | [SchemaForge](projects/structured-extractor/README.md) | Schema-constrained extraction and validation |
| 07 | [PromptRegistry](projects/prompt-registry/README.md) | Immutable prompt lineage and experiments |
| 08 | [ClaimGuard](projects/hallucination-detector/README.md) | Claim decomposition and evidence verification |
| 09 | [VoxAgent](projects/voice-agent/README.md) | Sub-second streaming voice orchestration |
| 10 | [DocFusion](projects/document-pipeline/README.md) | OCR, layout, table and document-graph parsing |
| 11 | [TraceLens](projects/observability/README.md) | Token, cost, latency and failure telemetry |
| 12 | [LocalServe](projects/local-llm/README.md) | GPU-hosted compatible inference |
| 13 | [ApproveAgent](projects/approval-agent/README.md) | Durable tools and human approval gates |
| 14 | [RedTeamBench](projects/red-team/README.md) | Jailbreak and prompt-injection evaluation |
| 15 | [SynthFactory](projects/synthetic-data/README.md) | Controlled privacy-filtered dataset generation |
| 16 | [AWS GenAI Control Plane](projects/bedrock-sagemaker-genai/README.md) | Bedrock Converse and SageMaker inference |
| 17 | [VisionRAG](projects/multimodal-rag/README.md) | Multimodal retrieval and reciprocal-rank fusion |
| 18 | [GraphWeaver](projects/graph-rag/README.md) | Entity-aware multi-hop GraphRAG context |
| 19 | [ToolMesh Agent](projects/toolmesh-agent/README.md) | Governed tool calling and auditable execution |
| 20 | [ReviewPilot](projects/code-review-agent/README.md) | AST-based AI-assisted code review |
| 21 | [DriftWatch](projects/driftwatch/README.md) | PSI-based feature drift and retraining signals |

## Repository contract

Every project contains:

- a technical architecture and implementation runbook
- a deterministic, credential-free executable demo
- automated contract tests
- explicit production-hardening requirements

## Execute a project

```bash
cd projects/multimodal-rag
python demo.py
python -m pytest -q
```

## Interactive portfolio

[reethika.in/ai-engineering-lab](https://reethika.in/ai-engineering-lab)
