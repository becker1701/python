
"""

The markov chain program will read quotes from http://www.goodreads.com/quotes/tag/being.

The user will type in a word, and the program will search through all of the quotes pulled off www.goodreads.com and return a random string that immediatly proceeds that user entered word.

The program functions like this:

1. Setup program:
    a: GET HTML page of quotes
    b: parse all quotes into a local file
2. Program prompts user for word to search for
3. Program looks for the word in the quotes saved into the local file of quotes
    a: Program creates a list of possible text; that is text that succeeds the user entered word
    b: program will randomly select one of the found phrases
    c: program prints the user enetered word and the random phrase
    d: if the word isn't found, three randomly selected words are picked from the file and used a suggestions for the user
    e: program will display the number of times the word was found in the file text
4. Program repeats until user quits

"""

import fetch_data
import markov_python.cc_markov


def format_generated_quote(quote):
    return " ".join(quote).capitalize() + "."


data = fetch_data.FetchData()

if data.response is not None:
    with open("data.txt", "w") as f:
        print("Writing parsed data to file...")
        
        for quote in data.quotes:
            f.write(quote.get_text())

    print("Generating quote...")
    mc = markov_python.cc_markov.MarkovChain()
    mc.add_file("data.txt")
    generated_quote = format_generated_quote(mc.generate_text())

    print(generated_quote)

else:
    print("Exiting...")

