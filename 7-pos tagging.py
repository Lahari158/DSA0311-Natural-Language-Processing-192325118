import nltk

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "I love Python programming"
words = sentence.split()

tags = nltk.pos_tag(words)
print(tags)
