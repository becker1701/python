from bs4 import BeautifulSoup
import requests

class FetchData(object):

    url = "http://quotes.toscrape.com/"

    def __init__(self):
        
        print("Attempting to open ", self.url)

        self.response = self.__get_response_from_url(self.url)
        self.soup = self.parse_html()

        if self.soup is not None:
            self.quotes = self.soup.find_all('span', class_='text')



    def __get_response_from_url(self, url):
        try:
            r = requests.get(self.url)

        except requests.Timeout:
            print("Connection timeout: ", self.url)
            r = None

        except requests.RequestException:
            print("An error prevented connection to ", self.url)
            r = None
        
        return r # r is a requests Request object


    def __response_text(self):    
        return self.response.text


    def parse_html(self):
        if self.__response_text is not None:
            print("Parsing HTML...")
            return BeautifulSoup(self.__response_text(), "html.parser")
        else:
            return None

    def get_text(self):
        return self.parse_html().get_text

    def print_parsed_data(self):
        print(self.parse_html())

    def __repr__(self):
        print("<class 'fetch_data.FetchData'>")
