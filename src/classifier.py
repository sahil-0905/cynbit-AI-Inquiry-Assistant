
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)


# 1. Load dataset
df = pd.read_csv("data/business_inquiries.csv")

X = df["inquiry"]
y = df["category"]


# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 3. Define three ML models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Naive Bayes": MultinomialNB(),

    "Linear SVM": LinearSVC()
}


results = []
trained_models = {}


# 4. Train and evaluate each model
for name, algorithm in models.items():

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            sublinear_tf=True
        )),
        ("classifier", algorithm)
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(
        y_test, predictions, average="macro", zero_division=0
    )
    recall = recall_score(
        y_test, predictions, average="macro", zero_division=0
    )
    f1 = f1_score(
        y_test, predictions, average="macro", zero_division=0
    )

    results.append({
        "Model": name,
        "Accuracy": round(accuracy * 100, 2),
        "Precision": round(precision * 100, 2),
        "Recall": round(recall * 100, 2),
        "Macro F1": round(f1 * 100, 2)
    })

    trained_models[name] = pipeline

    print(f"\n{'=' * 45}")
    print(f"MODEL: {name}")
    print(f"{'=' * 45}")
    print(f"Accuracy:  {accuracy * 100:.2f}%")
    print(f"Precision: {precision * 100:.2f}%")
    print(f"Recall:    {recall * 100:.2f}%")
    print(f"Macro F1:  {f1 * 100:.2f}%")

    print("\nClassification Report:")
    print(classification_report(
        y_test, predictions, zero_division=0
    ))


# 5. Compare models
comparison = pd.DataFrame(results)
comparison = comparison.sort_values(
    by="Macro F1", ascending=False
)

print("\n MODEL COMPARISON ")
print(comparison.to_string(index=False))


# 6. Select best model using Macro F1
best_model_name = comparison.iloc[0]["Model"]
best_model = trained_models[best_model_name]

os.makedirs("models", exist_ok=True)

# Save all trained models
joblib.dump(
    trained_models,
    "models/all_models.pkl"
)

# Save selected best model
joblib.dump(
    best_model,
    "models/best_classifier.pkl"
)

comparison.to_csv(
    "models/model_comparison.csv",
    index=False
)

print("All models saved successfully!")

comparison.to_csv(
    "models/model_comparison.csv", index=False
)

print("\n BEST MODEL ")
print("Selected Model:", best_model_name)
print("Best Macro F1:", comparison.iloc[0]["Macro F1"], "%")
print("Saved: models/best_classifier.pkl")


# 7. Test best model with new inquiry
sample = [
    "I want to develop an AI chatbot for my startup"
]

prediction = best_model.predict(sample)

print("\nNew Inquiry:", sample[0])
print("Predicted Category:", prediction[0])
