
import os
import joblib

from preprocessing import (
    extract_inquiry_details,
    detect_project_scope
)
from lead_scoring import calculate_lead_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best_classifier.pkl")

model = joblib.load(MODEL_PATH)


def analyze_inquiry(inquiry):
    if not inquiry or not inquiry.strip():
        raise ValueError("Customer inquiry cannot be empty.")

    category = model.predict([inquiry])[0]

    details = extract_inquiry_details(inquiry)

    budget = details.get("budget")
    if budget is not None:
        budget = int(str(budget).replace(",", ""))

    timeline = details.get("timeline") or "Not specified"
    urgency = details.get("urgency", "Low")

    project_scope = detect_project_scope(inquiry)

    score_result = calculate_lead_score(
        budget=budget,
        urgency=urgency,
        project_scope=project_scope
    )

    return {
        "category": category,
        "budget": budget,
        "timeline": timeline,
        "urgency": urgency,
        "project_scope": project_scope,
        "lead_score": score_result["lead_score"],
        "priority": score_result["priority"],
        "score_breakdown": score_result["breakdown"]
    }
