import unittest

from demo import run_pipeline


class PipelineTest(unittest.TestCase):
    def test_contract(self) -> None:
        result = run_pipeline("firmware upgrade bios")
        self.assertEqual(result["label"], "firmware_upgrade")


if __name__ == "__main__":
    unittest.main()
