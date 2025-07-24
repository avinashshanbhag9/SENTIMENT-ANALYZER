import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from preprocess import vectorize_text

# Load the dataset
df = pd.read_csv('data/sentiment_dataset.csv')  # Make sure the filename matches

# Use the correct column names
X = df['text']
y = df['airline_sentiment']

# Optional: Capitalize sentiment labels to match your frontend display
y = y.str.capitalize()

# Vectorize
vectorizer, X_vectorized = vectorize_text(X)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2)

# Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# Save Model and Vectorizer
pickle.dump(model, open('models/sentiment_model.pkl', 'wb'))
pickle.dump(vectorizer, open('models/vectorizer.pkl', 'wb'))

# Accuracy Check
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
