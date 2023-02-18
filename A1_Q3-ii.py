import os
import pickle
import pandas as pd
from nltk import word_tokenize
from bs4 import BeautifulSoup
# assign directory
directory = 'D:\CSE508_Winter2023_Dataset'

posInd = {}
docNo = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        proc_file = open(f, 'r')
        content = proc_file.read()
        proc_file.close()
        #print(content)
        tokens = word_tokenize(content)
        for pos, name in enumerate(tokens):
            if name in posInd:  # if token already present in ds
                posInd[name][0] = posInd[name][0] + 1  # incr freq

                if docNo in posInd[name][1]:  # if fileno already present then add into pos list
                    posInd[name][1][docNo].append(pos)
                else:
                    posInd[name][1][docNo] = [pos]  # create new list
            else:  # create new list and dict
                posInd[name] = []
                posInd[name].append(1)
                posInd[name].append({})
                posInd[name][1][docNo] = [pos]

    docNo = docNo + 1
print(posInd)

with open('positional_postings', 'wb') as fh:
   pickle.dump(posInd, fh)