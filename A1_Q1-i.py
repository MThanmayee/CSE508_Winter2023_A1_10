import os
from bs4 import BeautifulSoup

directory = 'D:\CSE508_Winter2023_Dataset'
c=0
print("Before Text:\n")
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and c!=5:
        c=c+1
        h_file = open(f, "r")
        cont = h_file.read()
        print(cont)
        print("\n")
    else:
        break;

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        HTMLFileToBeOpened = open(f, "r")
        contents = HTMLFileToBeOpened.read()
        title=""
        text=""
        beautifulSoupText = BeautifulSoup(contents, 'html.parser')
        for tag in beautifulSoupText.findAll('title'):
           title = beautifulSoupText.find(tag.name).text
        for tag in beautifulSoupText.findAll('text'):
           text = beautifulSoupText.find(tag.name).text
        HTMLFileToBeOpened1 = open(f, "w")
        title = title.strip()
        text = text.strip()
        s = title +" "+ text
        HTMLFileToBeOpened1.write(s);
        HTMLFileToBeOpened1.close();

print("After Text:\n")
c=0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and c!=5:
        c=c+1
        h_file = open(f, "r")
        cont = h_file.read()
        print(cont)
        print("\n")
    else:
        break;