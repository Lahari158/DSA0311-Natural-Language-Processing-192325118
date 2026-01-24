from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

documents = [
    "I love machine learning",
    "Machine learning is fun",
    "Python is great for machine learning"
]

query = ["machine learning"]

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents + query)

cosine_sim = np.dot(tfidf[-1].toarray(), tfidf[:-1].toarray().T)
print("Document Ranking:", cosine_sim)
