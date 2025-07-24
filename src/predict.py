import pickle

model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

def predict_sentiment(text):
    x = vectorizer.transform([text])
    return model.predict(x)[0]
