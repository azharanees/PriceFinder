from textblob import TextBlob

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

#import os
#import nltk
#import nltk.corpus

3#Feedback1 = " The phone is in working fine"
#Feedback2 = "The phone has terrible display"
#blob1= TextBlob(Feedback1)
#blob2= TextBlob(Feedback2)
#print(blob1.sentiment)
#print(blob2.sentiment)

#Feedback3 =  "iPhone 6 Plus Display Original Used. Replacement will be done In front of you. " \
#            "Duration: Just 25 minutes. Removed from used iPhones But 100% Original Display"
#Feedback4 = " The phone is not cracked"
#blob3= TextBlob(Feedback3)
#blob4= TextBlob(Feedback4)
#print(blob3.sentiment)
#print(blob4.sentiment)


##Here is the sentimental anaylisis

paragraph = "iPhone 6 Plus Display Original Used. Replacement will be done In front of you. " \
            "Duration: Just 25 minutes. Removed from used iPhones But 100% Original Display"


blob3= TextBlob(paragraph)
print(blob3.sentiment)

sentence = sent_tokenize(paragraph)
tokens = word_tokenize(paragraph)
tagging = pos_tag(tokens)

# Filter stop words
stop_words = set(stopwords.words('english'))

filter_sentence = [w for w in tokens if not w in stop_words]

filtered_sentence = []

for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

# filter using parts of speech tagging
data = []
for sent in sentence:
    data = data + pos_tag(word_tokenize(sent))

for word in data:
    if 'JJ' in word[1]:
        print(word)

print(sentence)
print(tokens)
print(tagging)

#print(os.listdir(nltk.data.find("corpora")))
#nltk.corpus.gutenberg.fileids()
