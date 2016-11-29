
"""

This program will generate randomized quotes of words taken from a website.  For each word, the program will assign the next word in the generated quote by looking up the current word, generating a list of next word candidates, and return a random word from the list.

The cc_markov module will generate a list of words from quote scrapped from http://quotes.toscrape.com/.  

1. The program will open and scrape quotes.toscrape.com for the "quote" CSS span 'text' class.
2. The program will set a FetchData member variable 'quote' and set sanitized data to it
3. run.py will then write the FetchData quotes data to a file
4. A MarkovChain object is intantiated and the data file is passed in
5. The generated quote returned is 'humanized' by capitalizing the first word and adding a period.

****************************************
Python 3.5

Modules included:
requests - HTTP response/request
BeautifulSoup - HTML parser
markov_chain - included module from Codecademy

"""

import fetch_data
import markov_python.cc_markov

data_file = "data.txt"

def humanize(quote):
    # Capitalize sentence and add period to computer generated markov quote.
    return " ".join(quote).capitalize() + "."



data = fetch_data.FetchData() # Create a FetchData object to hold the scraped data


if data.quotes is not None:
    # If quotes exist, write the BeautifulSoup.text to the file
    with open(data_file, "w") as f:
        
        print("Writing parsed data to file...")
        
        for quote in data.quotes:
            f.write(quote.get_text())

    
    print("Generating quote...")

    #Create the Markov Chain object and pass in the text
    mc = markov_python.cc_markov.MarkovChain()
    mc.add_file(data_file)

    #Format and return the generated quote
    generated_quote = humanize(mc.generate_text())

    print(generated_quote)

else:
    # If there is no data in the file
    print("No data was retrived.")
    print("Exiting...")