"""DriftWatch: lightweight population stability monitoring for ML features."""
import math

def _distribution(values: list[float], cuts: list[float]) -> list[float]:
    counts = [0] * (len(cuts) + 1)
    for value in values:
        idx = sum(value > cut for cut in cuts); counts[idx] += 1
    total = max(len(values), 1)
    return [max(c / total, 1e-6) for c in counts]

def population_stability_index(reference: list[float], current: list[float], bins: int = 5) -> float:
    ordered = sorted(reference)
    cuts = [ordered[min(int(len(ordered) * i / bins), len(ordered) - 1)] for i in range(1, bins)]
    expected, actual = _distribution(reference, cuts), _distribution(current, cuts)
    return sum((a - e) * math.log(a / e) for e, a in zip(expected, actual))

def report(reference: list[float], current: list[float]) -> dict:
    psi = population_stability_index(reference, current)
    level = "stable" if psi < .1 else "watch" if psi < .25 else "drifted"
    return {"psi": round(psi, 4), "status": level, "retrain_recommended": level == "drifted"}

if __name__ == "__main__":
    print(report([1, 2, 3, 4, 5] * 20, [7, 8, 9, 10] * 25))
