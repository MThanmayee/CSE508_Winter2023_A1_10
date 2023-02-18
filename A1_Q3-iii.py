import re
from nltk.corpus import stopwords
from nltk import word_tokenize
from Boolean_Queries import AND_merge
import pickle
pickle_off = open("positional_postings", 'rb')
positional_index = pickle.load(pickle_off)

pickle_off = open("bigram_postings", 'rb')
bigram_index = pickle.load(pickle_off)

pickle_off1 = open("DOC-ID Mapping", 'rb')
doc_ids = pickle.load(pickle_off1)


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


def process_positional(query,k):
  not_present=0
  for word in query:
    if word not in positional_index:
      not_present = 1
      break
  count = 0
  doc_list = []
  if not_present == 0:
    for doc in positional_index[query[0]][1]:
      for occurance in positional_index[query[0]][1][doc]:
        found = 1
        ptr=1
        for i in range(1,len(query)):
          if doc not in positional_index[query[i]][1].keys() or (occurance+ptr) not in positional_index[query[i]][1][doc]:
            found = 0
            break
          ptr+=1
        if found == 1:
          count+=1
          doc_list.append(doc)
          break
  print("Number of documents retrieved for query ",k," using positional index:",count)
  print("Number of documents retrieved for query ",k," using positional index:",end="")
  position = ""
  for doc in doc_list:
    position += doc_ids[doc]+","
  print(position)

def process_bigram(query,k):
  not_present=0
  for i in range(len(query)):
    if query[i] not in bigram_index:
      not_present = 1
      break
  fdocl = []
  if not_present == 0:
    fdocl = bigram_index[query[0]]
    for i in range(1,len(query)):
      fdocl,c = AND_merge(fdocl,bigram_index[query[i]])

  print("Number of documents retrieved for query ",k," using bigram inverted index:",len(fdocl))
  print("Names of documents retrieved for query ",k," using bigram inverted index:",end=" ")
  position = ""
  if len(fdocl) == 0:
    print("NULL")
  else:
    for doc in fdocl:
      position += doc_ids[doc]+","
    print(position)


N = int(input("Enter number of queries:"))
queries = []
for i in range(N):
  print("Query ",i+1,":",end=" ")
  x = input()
  queries.append(x)

cnt=0

for query in queries:
  query = lowercase(str(query))# preprocess query and extract words
  txt_punc = remove_punc(query)
  word_tokens = word_tokenize(txt_punc)
  wl = remove_stopwords(word_tokens)
  wl = remove_spaces(wl)
  cnt += 1
  list_of_tup = []
  for i in range(len(wl) - 1):
    list_of_tup.append((wl[i], wl[i + 1]))
  process_bigram(list_of_tup, cnt)
  process_positional(wl,cnt)
