import fetch_data
import unittest
import requests

class FetchDataTest(unittest.TestCase):
    '''FetchData formed correctly with valid URL input'''


    def test_fetch_data_object_returned_with_quotes_when_instantiated(self):
        #Ensure a valid FetchData object is returned
        nfdo = fetch_data.FetchData()
        self.assertEqual(type(nfdo), fetch_data.FetchData)
        self.assertFalse(len(nfdo.quotes) == 0)


class FetchDataBadInput(unittest.TestCase):
    '''Test fetch_data object with invalid inputs'''

    html_mockup = '<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork"><span class="text" itemprop="text">“Test quote”</span></div>'

    def test_fetch_data_bad_url_format(self):
        '''should fail with a missformed URL'''
        self.assertRaises(requests.exceptions.MissingSchema, fetch_data.FetchData, "a")

    def test_fetch_data_object_none_with_invalid_url(self):
        '''should raise requests.RequestException when URL is invalid'''
        self.assertRaises(requests.ConnectionError, fetch_data.FetchData, "http://www.8hi34qygfd87ctgyqer7yfvw3hrea8fdyfcuays87qygw.com")

    def test_response_is_bs_object_when_valid(self):
        '''should return BeautifulSoup object if valid URL'''
        fdo = fetch_data.FetchData()
        self.assertEqual(type(fdo.response), requests.Response)

    def test_parse_html_returns_string_when_valid(self):
        '''should pass if the BeautifulSoup & html.parser return strings of the quotes'''
        quote = '<span class="text" itemprop="text">“Test quote”</span>'
        self.assertEqual(quote, str(fetch_data.parse_html(self.html_mockup)[0]))


if __name__ == "__main__":
    unittest.main()