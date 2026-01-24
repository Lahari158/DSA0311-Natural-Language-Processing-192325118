from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

sentences = [
    "Machine learning is powerful",
    "It is used in many applications",
    "The sky is blue"
]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(sentences)

score = cosine_similarity(tfidf[0], tfidf[1])
print("Coherence Score:", score[0][0])
