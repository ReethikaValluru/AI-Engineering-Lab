import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline([0.9, 0.91, 0.89])
        self.assertEqual(result["release_gate"], "pass")


    def test_invalid_batches_raise_clear_errors(self) -> None:
        with self.assertRaisesRegex(ValueError, "at least one"):
            run_pipeline([])
        for bad in (float("nan"), float("inf"), -0.01, 1.01, True, "0.9"):
            with self.subTest(score=bad), self.assertRaisesRegex(ValueError, "between 0 and 1"):
                run_pipeline([0.9, bad])

    def test_endpoints_are_valid(self) -> None:
        self.assertEqual(run_pipeline([0, 1])["candidate"], 0.5)


if __name__ == "__main__":
    unittest.main()
