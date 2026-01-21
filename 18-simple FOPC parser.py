from nltk.wsd import lesk

# Input sentence
sentence = "I went to the bank to deposit money"

# Simple tokenization (no punkt needed)
words = sentence.split()

# Apply Lesk algorithm
sense = lesk(words, "bank")

# Display result
if sense:
    print(sense.name(), sense.definition())
else:
    print("No sense found")
