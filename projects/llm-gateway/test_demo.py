import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("reason")
        self.assertEqual(result["route"], "cloud-large")


if __name__ == "__main__":
    unittest.main()
