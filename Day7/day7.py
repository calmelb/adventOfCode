import re

file = open("test.txt","r")
text = file.readlines()
plain_text = []


for i in text:
    tmplist = {}
    words = i.split()
    print(words)
    contents = ' '.join(words[4:]).split(", ")
    tmplist[' '.join(words[:3])] = contents
    plain_text.append(tmplist)


print(plain_text)
