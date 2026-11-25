from demo import report

def test_shifted_distribution_is_flagged():
    assert report(list(range(100)), list(range(200, 300)))["status"] == "drifted"
