import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline(["hello"])
        self.assertGreater(result["tokens_per_second"], 0)


if __name__ == "__main__":
    unittest.main()
