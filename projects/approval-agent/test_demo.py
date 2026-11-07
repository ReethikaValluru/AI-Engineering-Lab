import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("issue refund")
        self.assertEqual(result["state"], "awaiting_approval")


if __name__ == "__main__":
    unittest.main()
