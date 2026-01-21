import nltk
import re

sentence = "Cats are running fast"
words = sentence.split()
tags = []
for w in words:
    if re.match(r'.*ing$', w):
        tags.append((w, 'VBG'))
    elif re.match(r'[A-Z].*', w):
        tags.append((w, 'NNP'))
    else:
        tags.append((w, 'NN'))
print(tags)
