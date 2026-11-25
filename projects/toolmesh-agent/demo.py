"""ToolMesh: policy-governed tool calling agent with an auditable execution trace."""
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Tool:
    name: str
    handler: Callable[..., Any]
    risk: str = "low"

class Agent:
    def __init__(self, tools: list[Tool], approve: Callable[[Tool], bool] = lambda _: False):
        self.tools = {t.name: t for t in tools}; self.approve = approve; self.trace = []

    def call(self, name: str, **arguments) -> Any:
        tool = self.tools[name]
        if tool.risk == "high" and not self.approve(tool):
            self.trace.append({"tool": name, "status": "blocked"})
            raise PermissionError(f"Approval required for {name}")
        result = tool.handler(**arguments)
        self.trace.append({"tool": name, "arguments": arguments, "status": "ok"})
        return result

if __name__ == "__main__":
    agent = Agent([Tool("search", lambda query: [f"result:{query}"])])
    print(agent.call("search", query="agent safety")); print(agent.trace)
