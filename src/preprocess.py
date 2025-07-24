from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(texts):
    vectorizer = TfidfVectorizer(stop_words='english')
    features = vectorizer.fit_transform(texts)
    return vectorizer, features
