import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords


paragraph = "iPhone 6 Plus Display Original Used. Replacement will be done In front of you. Duration: Just 25 minutes. Removed from used iPhones But 100% Original Display"

sentence = sent_tokenize(paragraph)
tokens = word_tokenize(paragraph)
tagging = pos_tag(tokens)

#Filter stop words
stop_words = set(stopwords.words('english'))

filter_sentence = [w for w in tokens if not w in stop_words]

filtered_sentence = []

for w in tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
    
#filter using parts of speech tagging
data = []
for sent in sentence:
    data = data + pos_tag(word_tokenize(sent))

for word in data:
    if 'JJ' in word[1]:
        print(word)

print(sentence)
print(tokens)
print(tagging)
