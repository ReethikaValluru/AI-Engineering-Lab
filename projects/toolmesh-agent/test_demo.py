import pytest
from demo import Agent, Tool

def test_high_risk_tool_is_blocked():
    agent = Agent([Tool("send", lambda: True, risk="high")])
    with pytest.raises(PermissionError): agent.call("send")
    assert agent.trace[-1]["status"] == "blocked"
