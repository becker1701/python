from bs4 import BeautifulSoup
import requests

class FetchData(object):

    def __init__(self, url="http://quotes.toscrape.com/"):

        self.url = url
        self.response = self.__get_response_from_url(self.url)

        if self.response is not None:
            soup = self.parse_html()
            self.quotes = soup.find_all('span', class_='text')
        else:
            self.quotes = None



    def __get_response_from_url(self, url):
        try:
            return requests.get(self.url) # should be a requests Response object

        except requests.Timeout:
            print("Connection timeout: ", self.url)

        except requests.RequestException:
            print("An error prevented connection to ", self.url)


    def __response_text(self):
        return self.response.text



    def parse_html(self):
        if self.__response_text is not None:
            return BeautifulSoup(self.__response_text(), "html.parser")
        else:
            return None


    def print_parsed_data(self):
        print(self.parse_html())


    def __repr__(self):
        print("<FetchData>")
