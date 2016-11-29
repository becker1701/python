import unittest
import run


class RunTest(unittest.TestCase):

    def test_humanize_returns_formatted_string(self):
        test_string = ["a", "dog", "is", "running"]
        self.assertEqual(run.humanize(test_string), "A dog is running.")

    def test_file_path_name_set(self):
        self.assertEqual(run.data_file, "data.txt")

if __name__ == "__main__":
    unittest.main(verbosity=2)


