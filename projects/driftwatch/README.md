# DriftWatch

A model-monitoring reference that calculates population stability index (PSI), assigns operational severity, and produces a machine-readable retraining recommendation.

## Run

```bash
python demo.py
python -m pytest -q
```

Production extensions: windowed metrics, concept-drift tests, label-delay handling, alert deduplication, dashboards, and automated retraining gates.

## Kaggle and Hugging Face

Import `kaggle_drift_demo.ipynb` into Kaggle and run all cells to check stable, drifted, and invalid inputs. The notebook uses synthetic data and requires no downloads. For Hugging Face Spaces, see [the Space README](hugging-face-space.md).
