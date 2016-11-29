from bs4 import BeautifulSoup
import requests

class FetchData(object):

    def __init__(self, url="http://quotes.toscrape.com/"):

        self.url = url
        self.response = requests.get(self.url)

        if self.response is not None:
            self.quotes = parse_html(self.response.text)
        else:
            self.quotes = None


def parse_html(fd_obj_text):
    '''Parse the FetchData.response object and return the text within the span.text elements'''

    if fd_obj_text is not None:
        result = BeautifulSoup(fd_obj_text, "html.parser")
        return result.find_all('span', class_='text')
    
    else:
        return None
