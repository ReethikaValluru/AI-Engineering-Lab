from demo import report

def test_shifted_distribution_is_flagged():
    assert report(list(range(100)), list(range(200, 300)))["status"] == "drifted"


def test_space_reports_valid_results_and_field_errors():
    from app import evaluate

    assert evaluate("0,1,2,3,4", "0,1,2,3,4")["status"] == "stable"
    assert evaluate("0,1,2,3,4", "10,11,12,13,14")["status"] == "drifted"
    assert evaluate("0,1", "0,NaN") == {
        "error": "Current window must contain only finite numbers."
    }
    assert evaluate("0,,1", "0,1") == {
        "error": "Reference window must contain comma-separated numbers."
    }


def test_distribution_preserves_cut_boundaries_and_empty_bins():
    from demo import _distribution

    assert _distribution([-1, 0, 0, 1, 2, 3], [0, 0, 2]) == [
        3 / 6, 1e-6, 2 / 6, 1 / 6
    ]
