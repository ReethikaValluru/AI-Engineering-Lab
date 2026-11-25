# DriftWatch

A model-monitoring reference that calculates population stability index (PSI), assigns operational severity, and produces a machine-readable retraining recommendation.

## Run

```bash
python demo.py
python -m pytest -q
```

Production extensions: windowed metrics, concept-drift tests, label-delay handling, alert deduplication, dashboards, and automated retraining gates.
