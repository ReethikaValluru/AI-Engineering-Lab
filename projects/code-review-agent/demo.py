"""ReviewPilot: explainable static checks designed for AI-assisted review workflows."""
from dataclasses import dataclass, asdict
import ast

@dataclass
class Finding:
    rule: str
    line: int
    severity: str
    message: str

class Reviewer(ast.NodeVisitor):
    def __init__(self): self.findings: list[Finding] = []
    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.findings.append(Finding("PY001", node.lineno, "high", "Avoid bare except; catch a specific exception."))
        self.generic_visit(node)
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == "eval":
            self.findings.append(Finding("SEC001", node.lineno, "critical", "Do not evaluate untrusted input."))
        self.generic_visit(node)

def review(source: str) -> list[dict]:
    tree = ast.parse(source); reviewer = Reviewer(); reviewer.visit(tree)
    return [asdict(f) for f in reviewer.findings]

if __name__ == "__main__":
    print(review("try:\n    eval(user_input)\nexcept:\n    pass"))
