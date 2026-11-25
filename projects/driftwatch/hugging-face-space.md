# DriftWatch Space draft

DriftWatch compares a reference feature window with a current window using the population stability index (PSI). The demo uses synthetic numbers and needs no model checkpoint or credentials.

Use `report(reference, current)` in `demo.py` as the inference function for a Space. Accept two comma-separated numeric input windows, parse them as floats, and surface validation errors next to the inputs. Display the returned PSI, status, and retraining flag. Use `0,1,2,3,4` in both inputs for a stable example and `10,11,12,13,14` for the current window to demonstrate drift.

The thresholds are illustrative. Validate them against historical data before using this signal for operational decisions.
