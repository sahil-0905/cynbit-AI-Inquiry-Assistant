
import re


def extract_inquiry_details(inquiry):
    """Extract budget, timeline and urgency from customer inquiry."""

    # -------------------------
    # 1. Extract Budget
    # -------------------------

    budget = None

    budget_patterns = [
        r"(?:₹|rs\.?|inr)\s*([\d,]+)",
        r"budget\s*(?:is|of|around|approximately)?\s*₹?\s*([\d,]+)"
    ]

    for pattern in budget_patterns:
        match = re.search(pattern, inquiry, re.IGNORECASE)

        if match:
            budget_text = match.group(1).replace(",", "")

            if budget_text.isdigit():
                budget = int(budget_text)
                break

    # -------------------------
    # 2. Extract Timeline
    # -------------------------

    timeline = None

    timeline_pattern = (
        r"(?:within|in|delivery in)?\s*"
        r"(\d+\s*(?:days?|weeks?|months?))"
    )

    timeline_match = re.search(
        timeline_pattern,
        inquiry,
        re.IGNORECASE
    )

    if timeline_match:
        timeline = timeline_match.group(1)

    # -------------------------
    # 3. Detect Urgency
    # -------------------------

    text = inquiry.lower()

    high_urgency = [
        "urgent",
        "asap",
        "immediately",
        "as soon as possible"
    ]

    medium_urgency = [
        "soon",
        "next month",
        "within a few weeks"
    ]

    if any(word in text for word in high_urgency):
        urgency = "High"

    elif any(word in text for word in medium_urgency):
        urgency = "Medium"

    else:
        urgency = "Low"

    return {
        "budget": budget,
        "timeline": timeline,
        "urgency": urgency
    }


# -------------------------
# 4. Detect Project Scope
# -------------------------

def detect_project_scope(inquiry):

    text = inquiry.lower()

    large_keywords = [
        "enterprise",
        "large scale",
        "large-scale",
        "multiple platforms",
        "end-to-end",
        "complex system",
        "multi-branch",
        "multiple integrations",
        "high traffic"
    ]

    small_keywords = [
        "landing page",
        "one page",
        "one-page",
        "basic website",
        "simple website",
        "minor changes",
        "small website",
        "single page"
    ]

    medium_keywords = [
        "e-commerce",
        "payment gateway",
        "admin dashboard",
        "user authentication",
        "api integration",
        "customer portal",
        "mobile app",
        "analytics dashboard"
    ]

    if any(keyword in text for keyword in large_keywords):
        return "Large"

    if any(keyword in text for keyword in small_keywords):
        return "Small"

    if any(keyword in text for keyword in medium_keywords):
        return "Medium"

    return "Not specified"
