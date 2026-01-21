from nltk.corpus import wordnet

word = "bank"
synsets = wordnet.synsets(word)

for syn in synsets[:2]:
    print(syn.name(), syn.definition())
