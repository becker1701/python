import unittest
import fetch_data
import requests
import bs4


class FetchDataTest(unittest.TestCase):

    def test_fetch_data_object_returned_with_quotes_when_instantiated(self):
        #Ensure a valid FetchData object is returned
        nfdo = fetch_data.FetchData()
        self.assertEqual(type(nfdo), fetch_data.FetchData)
        self.assertFalse(len(nfdo.quotes) == 0)

    def test_fetch_data_object_none_with_invalid_url(self):
        fdo = fetch_data.FetchData(" ")
        self.assertRaises(requests.RequestException)

    def test_response_is_bs_object_when_valid(self):
        fdo = fetch_data.FetchData()
        self.assertEqual(type(fdo.response), requests.Response)


if __name__ == "__main__":
    unittest.main()