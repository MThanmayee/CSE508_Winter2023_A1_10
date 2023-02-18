import os
import pickle
from nltk import word_tokenize

directory = 'D:\CSE508_Winter2023_Dataset'

doc = 0
bi_postings = {}
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        HTMLFileToBeOpened = open(f, "r")
        contents = HTMLFileToBeOpened.read()
        HTMLFileToBeOpened.close()
        tokens = word_tokenize(contents)
        #bi-gram inverted index
        for i in range(len(tokens)-1):
            tup = (tokens[i],tokens[i+1])
            if tup in bi_postings:
                if doc not in bi_postings[tup]:
                    bi_postings[tup].append(doc)
            else:
                bi_postings[tup] = [doc]
        doc += 1
print(bi_postings)

with open('bigram_postings', 'wb') as fh:
   pickle.dump(bi_postings, fh)










