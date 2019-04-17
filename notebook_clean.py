

# Importing requests, BeautifulSoup and nltk

import requests
from bs4 import BeautifulSoup
import nltk


# Getting the HTML for Jane Austen's books
url = 'http://www.gutenberg.org/files/21839/21839-h/21839-h.htm'
r = requests.get(url)

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
print(html[0:2000])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html)

# Getting the text out of the soup
text = soup.get_text()

# Printing out text between characters 32000 and 34000
print (text[32000:34000])

# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens
print(tokens[0:8])

# A new list to hold the lowercased words
words = []

# Looping through the tokens and make them lower case
for word in tokens:
    words.append(word.lower())

# Printing out the first 8 words / tokens
print(words[0:8])

# Getting the English stop words from nltk
nltk.download('stopwords')
sw = nltk.corpus.stopwords.words('english')

print(sw[0:8])

# A new list to hold Sense and Sensibility with No Stop words
words_ns = []
# Appending to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

    

# Printing the first 5 words_ns to check that stop words are gone

print(words_ns[0:5])

# Creating the word frequency distribution
freqdist = nltk.FreqDist(words_ns)

# Plotting the word frequency distribution
freqdist.plot(25)



