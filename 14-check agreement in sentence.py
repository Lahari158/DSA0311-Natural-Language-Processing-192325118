sentence = "He runs"
words = sentence.split()
if words[0] == "He" and words[1].endswith('s'):
    print("Agreement correct")
else:
    print("Agreement incorrect")
