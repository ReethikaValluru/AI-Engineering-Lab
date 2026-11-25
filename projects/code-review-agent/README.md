# ReviewPilot

An explainable AI-code-review foundation. It parses Python into an AST, detects security and maintainability risks, and emits structured findings that can be summarized by an LLM or posted as pull-request annotations.

## Run

```bash
python demo.py
python -m pytest -q
```

Production extensions: diff-aware review, Semgrep integration, repository context retrieval, false-positive feedback, GitHub Checks output, and evaluation against a curated defect set.
