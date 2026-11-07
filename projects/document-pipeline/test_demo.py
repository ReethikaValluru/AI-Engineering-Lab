import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("A\n\fB")
        self.assertEqual(result["pages"], 2)


if __name__ == "__main__":
    unittest.main()
