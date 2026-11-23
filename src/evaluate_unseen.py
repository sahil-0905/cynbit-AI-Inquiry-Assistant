
import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

print("Starting Unseen Data Evaluation...")

# Load test dataset
df = pd.read_csv("data/test_inquiries.csv")

X_test = df["inquiry"]
y_test = df["category"]

print("Test records loaded:", len(df))

# Load trained models
models = joblib.load("models/all_models.pkl")

# Evaluate each model
for name, model in models.items():

    predictions = model.predict(X_test)

    print("\n" + "=" * 45)
    print("MODEL:", name)
    print("=" * 45)

    print("Accuracy:",
          round(accuracy_score(y_test, predictions) * 100, 2), "%")

    print("Precision:",
          round(precision_score(
              y_test, predictions,
              average="macro", zero_division=0
          ) * 100, 2), "%")

    print("Recall:",
          round(recall_score(
              y_test, predictions,
              average="macro", zero_division=0
          ) * 100, 2), "%")

    print("Macro F1:",
          round(f1_score(
              y_test, predictions,
              average="macro", zero_division=0
          ) * 100, 2), "%")

    print("\nClassification Report:")
    print(classification_report(
        y_test, predictions,
        zero_division=0
    ))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nIndividual Predictions:")

    for inquiry, actual, predicted in zip(
        X_test, y_test, predictions
    ):
        print("Inquiry:", inquiry)
        print("Actual:", actual)
        print("Predicted:", predicted)
        print("-" * 30)

print("\nEvaluation completed successfully!")
