# train_model.py
import joblib
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# 1. Toy Dataset
data = [
    "I absolutely love this product, it is amazing",
    "This is the worst experience of my life",
    "Great quality and fast shipping",
    "Terrible customer service and broken item",
    "Highly recommended, will buy again",
    "Waste of money, do not buy"
]
labels = ["Positive", "Negative", "Positive", "Negative", "Positive", "Negative"]

# 2. Create a pipeline (Vectorizer + Classifier)
model = make_pipeline(CountVectorizer(), LogisticRegression())

# 3. Train the model
model.fit(data, labels)

# 4. Save the trained model to the ml_model app folder
save_path = os.path.join('ml_model', 'saved_model.joblib')
joblib.dump(model, save_path)
print(f"Model trained and saved to {save_path}!")