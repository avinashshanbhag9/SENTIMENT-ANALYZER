import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from flask import Flask, request, render_template
from src.predict import predict_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['text']
    sentiment = predict_sentiment(input_text)
    return render_template('index.html', prediction=sentiment, text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
