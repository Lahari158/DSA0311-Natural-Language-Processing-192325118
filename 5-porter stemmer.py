from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

words = ["running", "flies", "cats"]
for w in words:
    print(w, "->", stemmer.stem(w))
