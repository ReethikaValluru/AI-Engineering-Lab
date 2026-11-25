# ToolMesh Agent

A framework-neutral tool-calling agent that demonstrates registry-based tools, risk classification, human approval gates, and structured audit traces. Its contracts map naturally to MCP-style tool servers.

## Run

```bash
python demo.py
python -m pytest -q
```

Production extensions include JSON Schema validation, signed tool manifests, retry budgets, sandboxed execution, OpenTelemetry traces, and durable approval workflows.
