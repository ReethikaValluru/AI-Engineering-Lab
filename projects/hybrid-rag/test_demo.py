import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("records retained years")
        self.assertTrue(result["citations"])


if __name__ == "__main__":
    unittest.main()
