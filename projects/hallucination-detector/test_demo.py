import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("Warranty lasts five years.", "Warranty lasts five years.")
        self.assertEqual(result["decision"], "allow")


if __name__ == "__main__":
    unittest.main()
