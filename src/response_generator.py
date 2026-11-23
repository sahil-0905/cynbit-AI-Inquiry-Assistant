
import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------------------
# 1. Load environment variables
# -----------------------------------

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file."
    )


# -----------------------------------
# 2. Initialize Groq client
# -----------------------------------

client = Groq(api_key=API_KEY)


# -----------------------------------
# 3. Generate customer response
# -----------------------------------

def generate_customer_response(inquiry, analysis):

    budget = analysis.get("budget")
    timeline = analysis.get("timeline")

    budget_text = (
        f"₹{budget:,}" if budget is not None else "Not provided"
    )

    timeline_text = (
        timeline if timeline and timeline != "Not specified"
        else "Not provided"
    )

    prompt = f"""
    You are a professional business customer support assistant.

    Write a polite, personalized and professional reply
    to the customer's inquiry.

    Customer Inquiry:
    {inquiry}

    Inquiry Analysis:
    Category: {analysis['category']}
    Budget: {budget_text}
    Timeline: {timeline_text}
    Urgency: {analysis['urgency']}
    Lead Priority: {analysis['priority']}

    Instructions:
    1. Always start the response with "Hello,"
    2. Never ask for or invent the customer's name.
    3. Never use [Customer Name] or any placeholder.
    4. Thank the customer for contacting us.
    5. Acknowledge their actual project requirements.
    6. Mention budget only if the customer provided it.
    7. Mention timeline only if the customer provided it.
    8. Suggest discussing the next steps.
    9. Do not promise delivery dates or pricing.
    10. Keep the response concise and professional.
    11. Do not invent services or project requirements.
    """

    try:

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional business "
                        "customer support assistant. "
                        "Never invent customer information."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_completion_tokens=500
        )

        generated_text = response.choices[0].message.content

        if not generated_text:
            raise ValueError(
                "Groq returned an empty response."
            )

        return {
            "response": generated_text.strip(),
            "source": "Groq AI",
            "success": True
        }

    except Exception as error:

        print("Groq API Error:", error)

        fallback_response = f"""
Hello,

Thank you for contacting us regarding your
{analysis['category']} requirements.

We appreciate your interest in our services.
Our team will review your requirements and
get back to you to discuss the next steps.

Best regards,
Business Support Team
"""

        return {
            "response": fallback_response.strip(),
            "source": "Fallback Template",
            "success": False
        }


# -----------------------------------
# 4. Test response generator
# -----------------------------------

if __name__ == "__main__":

    sample_inquiry = (
        "We need an AI chatbot for our startup. "
        "Budget is ₹150000. "
        "Delivery within 30 days. Urgent."
    )

    sample_analysis = {
        "category": "AI Automation",
        "budget": 150000,
        "timeline": "30 days",
        "urgency": "High",
        "priority": "High"
    }

    result = generate_customer_response(
        sample_inquiry,
        sample_analysis
    )

    print("\n" + "=" * 50)
    print("GENERATED CUSTOMER RESPONSE")
    print("=" * 50)

    print(result["response"])

    print("\nSource:", result["source"])
    print("Success:", result["success"])
