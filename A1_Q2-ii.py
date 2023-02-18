import os
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from Boolean_Queries import *
import pickle

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


pickle_off = open("unigram_postings", 'rb')
postings = pickle.load(pickle_off)
doc_map={}
i=0
doc_names = ""
directory = 'D:\CSE508_Winter2023_Dataset'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        doc_map[i]=filename
        i += 1

with open('DOC-ID Mapping', 'wb') as fh:
   pickle.dump(doc_map, fh)
def process_query(query,operators):
    total_comparisons = 0
    for i, op in enumerate(operators):
        if i == 0:  # for the first word in the query
            if op == "AND":
                docs, comparisons = AND_merge(postings[query[i]].copy(), postings[query[i + 1]].copy())
            elif op == "OR":
                docs, comparisons = OR_merge(postings[query[i]].copy(), postings[query[i + 1]].copy())
            elif op == "AND NOT":
                docs, comparisons = ANDNOT_merge(postings[query[i]].copy(), postings[query[i + 1]].copy())
            elif op == "OR NOT":
                docs, comparisons = ORNOT_merge(postings[query[i]].copy(), postings[query[i + 1]].copy())
            else:
                print("Invalid Query!!!")
                return
        else:  # for the next query words, check with previous result got in docs 
            if op == "AND":
                docs, comparisons = AND_merge(docs.copy(), postings[query[i + 1]].copy())
            elif op == "OR":
                docs, comparisons = OR_merge(docs.copy(), postings[query[i + 1]].copy())
            elif op == "AND NOT":
                docs, comparisons = ANDNOT_merge(docs.copy(), postings[query[i + 1]].copy())
            elif op == "OR NOT":
                docs, comparisons = ORNOT_merge(docs.copy(), postings[query[i + 1]].copy())
            else:
                print("Invalid Query!!!")
                return
        total_comparisons += comparisons

    return docs, total_comparisons

N = int(input("Enter the number of queries: "))  # number of queries
queries = []
operator_list = []
for p in range(N):
    print("Query ", p + 1, ":")
    x = input("Enter input sequence: ")
    queries.append(x)
    x = input("Enter operation sequence: ")
    operator_list.append(x)
for k in range(N):  # for each query
    query = queries[k]
    query = lowercase(str(query))# preprocess query and extract words
    txt_punc = remove_punc(query)
    word_tokens = word_tokenize(txt_punc)
    wl = remove_stopwords(word_tokens)
    wl = remove_spaces(wl)
    operators = operator_list[k]
    operators = operators.upper().split(",")
    print("Query ",k+1,":",end=" ")
    if(len(wl) != (len(operators)+1)):
        print("Invalid query")
    else:
        for i in range(len(wl)-1):
            print(wl[i]+" "+operators[i]+" ",end="")
        print(wl[len(wl)-1])
        docs, comparisons = process_query(wl, operators)
        print("Number of documents retrieved for query ",k+1,": ", len(docs))
        doc_names=""
        for i in docs:
            doc_names += doc_map[i]+ ", "
        print("Names of documents retrieved for query ",k+1,": ", doc_names)
        print("No. of comparisons required for query ",k+1,": ", comparisons)