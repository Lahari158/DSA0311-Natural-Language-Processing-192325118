words = ["He", "walks"]
tags = ["NN", "NN"]  # initial

# simple transformation: if word is "He", tag as PRP
tags = ["PRP" if w=="He" else t for w,t in zip(words, tags)]
print(list(zip(words, tags)))
