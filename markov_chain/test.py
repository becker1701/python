import unittest
import fetch_data

class MarkovChainTest(unittest.TestCase):

    def test_assert_true(self):
        self.assertTrue(True)

    def test_url(self):
        self.assertEqual(fetch_data.url, "http://quotes.toscrape.com/")


if __name__ == "__main__":
    unittest.main(verbosity=2)