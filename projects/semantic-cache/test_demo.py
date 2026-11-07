import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("reset account password")
        self.assertTrue(result["hit"])


if __name__ == "__main__":
    unittest.main()
