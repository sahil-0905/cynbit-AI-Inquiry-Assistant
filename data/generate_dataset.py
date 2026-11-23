
import pandas as pd
import random

random.seed(42)

inquiries = {
    "AI Automation": [
        "I need an AI chatbot for my business",
        "We want to automate customer support using AI",
        "Build an AI-powered virtual assistant",
        "I need an automated lead generation system",
        "Looking for an AI solution for business operations"
    ],

    "Web Development": [
        "I need an e-commerce website",
        "Build a professional business website",
        "We need a custom web application",
        "Looking for a developer to create a website",
        "I want to develop an online shopping platform"
    ],

    "App Development": [
        "I need an Android mobile app",
        "Build an iOS application for my startup",
        "We want a cross-platform mobile app",
        "Develop a mobile app for our customers",
        "Looking for mobile application development"
    ],

    "Cloud Services": [
        "I need cloud server deployment",
        "Help us migrate our application to AWS",
        "Our cloud infrastructure needs optimization",
        "We need cloud hosting for our application",
        "Looking for cloud infrastructure management"
    ],

    "Data Analytics": [
        "I need a business analytics dashboard",
        "Analyze our sales data and generate reports",
        "Build a data visualization solution",
        "We need customer data analysis",
        "Create a predictive analytics system"
    ],

    "General Inquiry": [
        "Tell me about your company services",
        "What are your development charges?",
        "I want to discuss a business project",
        "How can I contact your team?",
        "Can you share your service details?"
    ]
}

rows = []

for category, samples in inquiries.items():
    for sample in samples:
        for variation in range(10):

            prefixes = [
                "Hello, ",
                "Hi team, ",
                "We are looking for help. ",
                "Our company needs this. ",
                "I am interested in your services. ",
                ""
            ]

            suffixes = [
                "",
                " Please contact me.",
                " Can you provide more details?",
                " We want to start soon.",
                " Please share the pricing."
            ]

            text = (
                random.choice(prefixes)
                + sample
                + random.choice(suffixes)
            )

            rows.append({
                "inquiry": text,
                "category": category
            })

df = pd.DataFrame(rows)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("data/business_inquiries.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print("\nCategory distribution:")
print(df["category"].value_counts())
print("\nUnique categories:", df["category"].nunique())
