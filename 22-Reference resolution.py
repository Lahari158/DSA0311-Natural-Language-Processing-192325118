import spacy

nlp = spacy.load("en_core_web_sm")

text = "John went to the store. He bought milk."
doc = nlp(text)

last_noun = None
resolved_text = []

for token in doc:
    # Store last proper noun
    if token.pos_ == "PROPN":
        last_noun = token.text
        resolved_text.append(token.text)

    # Replace pronoun with last noun
    elif token.pos_ == "PRON" and last_noun is not None:
        resolved_text.append(last_noun)

    else:
        resolved_text.append(token.text)

print("Original Text:")
print(text)

print("\nResolved Text:")
print(" ".join(resolved_text))
