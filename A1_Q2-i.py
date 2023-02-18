import os
import pickle
from nltk import word_tokenize

directory = 'D:\CSE508_Winter2023_Dataset'
doc = 0
postings = {}
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        HTMLFileToBeOpened = open(f, "r")
        contents = HTMLFileToBeOpened.read()
        tokens = word_tokenize(contents)
        for token in tokens:
            if token in postings:
                if doc not in postings[token]:
                    postings[token].append(doc)
            else:
                postings[token]=[doc]
        doc += 1
print(postings)

with open('unigram_postings', 'wb') as fh:
   pickle.dump(postings, fh)








