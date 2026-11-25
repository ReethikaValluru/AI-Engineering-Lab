from demo import review

def test_security_and_quality_findings():
    findings = review("try:\n eval(x)\nexcept:\n pass")
    assert {f["rule"] for f in findings} == {"PY001", "SEC001"}
