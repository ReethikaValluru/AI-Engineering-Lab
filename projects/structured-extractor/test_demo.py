import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("Invoice 4431 EUR 819.40")
        self.assertTrue(result["valid"])


if __name__ == "__main__":
    unittest.main()
