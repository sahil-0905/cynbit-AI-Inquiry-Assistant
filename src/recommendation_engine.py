
def recommend_services(category, inquiry):
    """
    Recommend business services based on inquiry category
    and customer requirements.
    """

    category = category.lower()
    inquiry = inquiry.lower()

    recommendations = {
        "ai automation": [
            "AI Chatbot Development",
            "Workflow Automation",
            "LLM Integration",
            "AI Customer Support Systems"
        ],
        "web development": [
            "Custom Website Development",
            "E-commerce Development",
            "Payment Gateway Integration",
            "Admin Dashboard Development"
        ],
        "app development": [
            "Android App Development",
            "iOS App Development",
            "Cross-Platform App Development",
            "Mobile API Integration"
        ],
        "cloud services": [
            "AWS Cloud Migration",
            "Cloud Infrastructure Setup",
            "Cloud Security",
            "Cloud Backup and Monitoring"
        ],
        "data analytics": [
            "Business Intelligence Dashboard",
            "Data Visualization",
            "Sales Analytics",
            "Data Reporting Automation"
        ],
        "general inquiry": [
            "Business Consultation",
            "Software Development Consultation",
            "Digital Transformation Services"
        ]
    }

    # Get recommendations for predicted category
    suggested_services = recommendations.get(
        category,
        recommendations["general inquiry"]
    )

    # Additional keyword-based recommendations
    keyword_services = {
        "chatbot": "AI Chatbot Development",
        "automation": "Workflow Automation",
        "e-commerce": "E-commerce Development",
        "payment": "Payment Gateway Integration",
        "android": "Android App Development",
        "ios": "iOS App Development",
        "aws": "AWS Cloud Migration",
        "dashboard": "Business Intelligence Dashboard",
        "analytics": "Data Analytics Consultation"
    }

    extra_recommendations = []

    for keyword, service in keyword_services.items():
        if keyword in inquiry and service not in suggested_services:
            extra_recommendations.append(service)

    # Combine recommendations without duplicates
    final_recommendations = list(
        dict.fromkeys(
            suggested_services + extra_recommendations
        )
    )

    return {
        "recommended_services": final_recommendations[:5],
        "primary_category": category.title()
    }


# Test the recommendation engine
if __name__ == "__main__":

    sample_inquiry = """
    We need an e-commerce website with payment gateway
    and an admin dashboard for our clothing brand.
    """

    result = recommend_services(
        category="Web Development",
        inquiry=sample_inquiry
    )

    print("\nBUSINESS SERVICE RECOMMENDATIONS")
    print("=" * 40)

    print("Category:", result["primary_category"])

    for index, service in enumerate(
        result["recommended_services"],
        start=1
    ):
        print(f"{index}. {service}")
