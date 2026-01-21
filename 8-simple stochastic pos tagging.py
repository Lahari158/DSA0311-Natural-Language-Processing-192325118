import random
words = ["I", "run", "cats"]
pos_tags = ["NN", "VB", "JJ", "PRP"]

tagged = [(w, random.choice(pos_tags)) for w in words]
print(tagged)
