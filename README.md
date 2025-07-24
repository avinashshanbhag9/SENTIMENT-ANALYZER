Sentiment Analyzer
A machine learning-based web application that predicts the sentiment (Positive, Negative, Neutral) of user input text. The project is built using Python (scikit-learn) for ML and Flask for the web interface. It is trained on a real-world Twitter sentiment dataset.

🚀 Features
Real-time sentiment prediction from user text input.

Trained on Twitter US Airline Sentiment dataset.

Achieves 76% accuracy with Logistic Regression & TF-IDF.

Responsive web interface built using Flask + HTML/CSS.

Clean folder structure and easy to execute.

🛠 Tech Stack
Python 3

scikit-learn, pandas, numpy

Flask (Backend)

HTML, CSS, Bootstrap (Frontend)

Pickle for saving ML models

⚙️ Installation & Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/avinashshanbhag9/SENTIMENT-ANALYZER.git
cd SENTIMENT-ANALYZER
2. Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # Windows
# OR
source venv/bin/activate    # Linux/Mac
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Train the Model
bash
Copy
Edit
python src/train.py
5. Run the Flask App
bash
Copy
Edit
python app/app.py
Open your browser and go to http://127.0.0.1:5000/.

📊 Model Performance
Accuracy: 76%

Model Used: Logistic Regression

Feature Extraction: TF-IDF Vectorization

🔮 Future Improvements
Use Deep Learning (LSTM, BERT) for better accuracy.

Add sentiment visualization (pie charts/word clouds).

Deploy on cloud (Render/Heroku).
