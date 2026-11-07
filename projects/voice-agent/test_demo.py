import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("weather tomorrow")
        self.assertTrue(result["sla_met"])


if __name__ == "__main__":
    unittest.main()
