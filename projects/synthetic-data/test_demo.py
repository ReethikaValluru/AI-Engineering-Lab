import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline(3, 7)
        self.assertEqual(len(result["records"]), 3)


if __name__ == "__main__":
    unittest.main()
