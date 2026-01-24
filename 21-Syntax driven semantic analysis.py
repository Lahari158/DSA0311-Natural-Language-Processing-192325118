import spacy

nlp = spacy.load("en_core_web_sm")
text = "The intelligent student solved the problem"

doc = nlp(text)

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
