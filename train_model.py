import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# STEP 1: Load dataset
data = pd.read_csv("dataset.csv")

# STEP 2: Remove empty rows
data = data.dropna()

# STEP 3: Split into input and output
X = data["input"]
y = data["output"]

# STEP 4: Convert text into numerical form
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# STEP 5: Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_vectorized, y)

# STEP 6: Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved successfully!")