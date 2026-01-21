import random
text = "I like to play football and I like to read books"
words = text.split()
bigrams = {words[i]: words[i+1] for i in range(len(words)-1)}

word = words[0]
for _ in range(5):
    print(word, end=' ')
    word = bigrams.get(word, random.choice(words))
