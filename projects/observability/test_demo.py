import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline([{"name":"x","latency_ms":10,"tokens":5}])
        self.assertTrue(result["trace_complete"])


if __name__ == "__main__":
    unittest.main()
