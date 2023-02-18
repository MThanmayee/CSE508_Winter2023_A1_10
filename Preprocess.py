from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
import re
import pandas as pd
#nltk.download('punkt')
#nltk.download('stopwords')
doc = 0
def lowercase(string):
    return string.lower()
def remove_punc(string):
    txt = re.sub(r'[^\w\s]', '', string)
    return txt
def remove_stopwords(wlist):
    wcontent = []
    stop_words = set(stopwords.words('english'))
    for w in wlist:
        if w not in stop_words:
            wcontent.append(w)
    return wcontent
def remove_spaces(wlist):
    for ele in wlist:
        if ele == " ":
            wlist.remove(ele)
    return wlist

def print_output():
    c = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and c!=5:
            c=c+1
            h_file = open(f, "r")
            cont = h_file.read()
            h_file.close()
            print(cont)
            print("\n")
        else:
            break;
directory = 'D:\CSE508_Winter2023_Dataset'

print("Before Preprocessing:\n")
print_output()

for filename in os.listdir(directory):
     f = os.path.join(directory, filename)
     if os.path.isfile(f):
        proc_file = open(f,'r')
        content = proc_file.read()
        proc_file.close()
        content = lowercase(content)
        print("After Converting to lowercase:\n")
        print_output()
        txt_punc = remove_punc(content)
        print("After Removing the punctuations:\n")
        print_output()
        word_tokens = word_tokenize(txt_punc)
        print("After tokenizing the words:\n")
        print_output()
        wl = remove_stopwords(word_tokens)
        print("After removing the stop words:\n")
        print_output()
        wl = remove_spaces(wl)
        print("After Removing extra spaces:\n")
        print_output()
        listToStr = ' '.join(map(str, wl))
        proc_file1 = open(f,'w')
        proc_file1.write(listToStr)
        proc_file1.close()

print("After Preprocessing:\n")
c=0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and c!=5:
        c=c+1
        h_file = open(f, "r")
        cont = h_file.read()
        h_file.close()
        print(cont)
        print("\n")
    else:
        break;

