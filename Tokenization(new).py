# import libraries
from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# specify the url
quote_page = 'https://ikman.lk/en/ad/5d-premium-full-tempered-for-iphone-for-sale-colombo-1'

# query the website and return the html to the variable ‘page’
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of description and get its value
text_box = soup.find('div', attrs={'class': 'item-description'})

#After we have the tag, we can get the data by getting its text
description = text_box.text.strip() # strip() is used to remove starting and trailing



stop_words = set(stopwords.words("english"))

word = word_tokenize(description)

filtered_sentence = []

filtered_sentence = [w for w in word if not w in stop_words]

print(filtered_sentence)



for index, sentence in enumerate(filtered_sentence):
    if 'screen' in sentence:
       	if index is not None:
       		print('The screen is scratched')

       		#print("A") if a > b else print("B")