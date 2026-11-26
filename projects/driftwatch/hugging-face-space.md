---
title: DriftWatch
sdk: gradio
app_file: app.py
---

# DriftWatch

Compare two feature windows using the population stability index (PSI). The app displays PSI, drift status, and a retraining flag. Use the sample inputs to see stable and drifted results. The repeated-values example shows that tied reference values remain stable when the current window is identical.

For deployment, copy this file to the Space as `README.md` and place `app.py` and `demo.py` alongside it. The examples use synthetic data and run without a model checkpoint.

The thresholds are illustrative. Validate them against historical data before using the retraining flag in production.
