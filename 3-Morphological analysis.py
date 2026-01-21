import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

words = ["running", "flies", "cats"]
for w in words:
    print(w, "->", lemmatizer.lemmatize(w, pos='v'))  # verb
