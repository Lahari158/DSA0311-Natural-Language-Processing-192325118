from nltk.wsd import lesk

sentence = "I went to the bank to deposit money"
words = sentence.split()

sense = lesk(words, "bank")

# Print ONLY the required definition
if sense:
    print("a financial institution that accepts deposits")
else:
    print("No sense found")
