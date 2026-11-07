import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline([0.9, 0.91, 0.89])
        self.assertEqual(result["release_gate"], "pass")


if __name__ == "__main__":
    unittest.main()
