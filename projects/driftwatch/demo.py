"""DriftWatch: lightweight population stability monitoring for ML features."""
import math

def _distribution(values: list[float], cuts: list[float]) -> list[float]:
    counts = [0] * (len(cuts) + 1)
    for value in values:
        idx = sum(value > cut for cut in cuts); counts[idx] += 1
    total = max(len(values), 1)
    return [max(c / total, 1e-6) for c in counts]

def population_stability_index(reference: list[float], current: list[float], bins: int = 5) -> float:
    if not reference or not current:
        raise ValueError("Both sample windows must contain observations.")
    if not isinstance(bins, int) or isinstance(bins, bool) or bins < 2:
        raise ValueError("bins must be an integer of at least 2.")
    if not all(map(math.isfinite, reference)) or not all(map(math.isfinite, current)):
        raise ValueError("All observations must be finite.")
    ordered = sorted(reference)
    cuts = [ordered[min(int(len(ordered) * i / bins), len(ordered) - 1)] for i in range(1, bins)]
    expected, actual = _distribution(reference, cuts), _distribution(current, cuts)
    return sum((a - e) * math.log(a / e) for e, a in zip(expected, actual))

def report(reference: list[float], current: list[float]) -> dict:
    psi = population_stability_index(reference, current)
    level = "stable" if psi < .1 else "watch" if psi < .25 else "drifted"
    return {"psi": round(psi, 4), "status": level, "retrain_recommended": level == "drifted"}

def report_csv(reference: str, current: str) -> dict:
    """Evaluate comma-separated feature windows from an interactive form."""
    windows = []
    for label, raw in (("Reference", reference), ("Current", current)):
        try:
            values = [float(value.strip()) for value in raw.split(",")]
        except ValueError:
            raise ValueError(f"{label} window must contain comma-separated numbers.") from None
        if not all(map(math.isfinite, values)):
            raise ValueError(f"{label} window must contain only finite numbers.")
        windows.append(values)
    return report(*windows)


if __name__ == "__main__":
    print(report([1, 2, 3, 4, 5] * 20, [7, 8, 9, 10] * 25))
