import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("support", "u1")
        self.assertTrue(result["artifact_hash"].startswith("sha256:"))


if __name__ == "__main__":
    unittest.main()
