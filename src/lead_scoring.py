
def calculate_lead_score(budget, urgency, project_scope):
    breakdown = {}

    # 1. Budget score
    if budget is None:
        budget_score = 20  # Neutral score when budget is missing
        breakdown["Budget"] = {
            "score": budget_score,
            "reason": "Budget not provided; neutral score"
        }
    elif budget >= 100000:
        budget_score = 40
        breakdown["Budget"] = {
            "score": budget_score,
            "reason": "Budget is ₹1,00,000 or above"
        }
    elif budget >= 50000:
        budget_score = 30
        breakdown["Budget"] = {
            "score": budget_score,
            "reason": "Budget is ₹50,000–₹99,999"
        }
    elif budget >= 10000:
        budget_score = 20
        breakdown["Budget"] = {
            "score": budget_score,
            "reason": "Budget is ₹10,000–₹49,999"
        }
    else:
        budget_score = 10
        breakdown["Budget"] = {
            "score": budget_score,
            "reason": "Budget is below ₹10,000"
        }

    # 2. Urgency score
    urgency = (urgency or "low").lower()

    if urgency == "high":
        urgency_score = 30
    elif urgency == "medium":
        urgency_score = 20
    else:
        urgency_score = 10

    breakdown["Urgency"] = {
        "score": urgency_score,
        "reason": f"{urgency.title()} urgency"
    }

    # 3. Project scope score
    project_scope = (project_scope or "not specified").lower()

    if project_scope == "large":
        scope_score = 30
    elif project_scope == "small":
        scope_score = 10
    else:
        scope_score = 20

    breakdown["Project Scope"] = {
        "score": scope_score,
        "reason": (
            "Not specified; neutral Medium score used"
            if project_scope == "not specified"
            else f"{project_scope.title()} project scope"
        )
    }

    total_score = budget_score + urgency_score + scope_score

    if total_score >= 75:
        priority = "High"
    elif total_score >= 50:
        priority = "Medium"
    else:
        priority = "Low"

    return {
        "lead_score": total_score,
        "priority": priority,
        "breakdown": breakdown
    }
