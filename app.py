
import streamlit as st
import sys
import os
import pandas as pd

# --------------------------------
# PATH CONFIGURATION
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)


# --------------------------------
# IMPORT PROJECT MODULES
# --------------------------------

from inquiry_analyzer import analyze_inquiry
from recommendation_engine import recommend_services

from database import (
    initialize_db,
    save_inquiry,
    get_all_inquiries,
    get_inquiry_count
)


# --------------------------------
# INITIALIZE DATABASE
# --------------------------------

initialize_db()


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Cynbit AI Inquiry Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------
# HEADER
# --------------------------------

st.title("🤖 Cynbit AI Business Inquiry Assistant")

st.markdown(
    """
    Analyze customer inquiries using Machine Learning,
    extract project requirements, calculate lead priority,
    recommend business services and generate AI-powered responses.
    """
)

st.divider()


# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.title("🤖 About Project")

    st.write(
        """
        **Cynbit AI Business Inquiry Assistant**

        Features:

        - Customer inquiry classification
        - Budget extraction
        - Timeline extraction
        - Urgency detection
        - Project scope detection
        - Lead scoring and prioritization
        - Business service recommendations
        - AI-generated customer responses
        - SQLite inquiry management
        """
    )

    st.divider()

    st.caption("Technology Stack")

    st.write(
        """
        - Python
        - Streamlit
        - Scikit-learn
        - TF-IDF
        - Logistic Regression
        - Groq API
        - SQLite
        - Pandas
        """
    )

    st.divider()

    st.metric(
        "Total Saved Inquiries",
        get_inquiry_count()
    )


# --------------------------------
# APPLICATION TABS
# --------------------------------

tab1, tab2 = st.tabs(
    ["📝 Analyze Inquiry", "📂 Inquiry History"]
)


# ================================================
# TAB 1: ANALYZE CUSTOMER INQUIRY
# ================================================

with tab1:

    st.subheader("📝 Customer Inquiry")

    inquiry = st.text_area(
        "Enter the customer's business inquiry:",
        height=180,
        placeholder=(
            "Example: We need an e-commerce website for our clothing "
            "brand with product listings, shopping cart and payment "
            "gateway. Our budget is ₹80000 and delivery is required "
            "within 45 days."
        ),
        key="customer_inquiry"
    )

    if st.button(
        "🔍 Analyze Inquiry",
        type="primary",
        key="analyze_button"
    ):

        if not inquiry.strip():

            st.warning("Please enter a customer inquiry first.")

        else:

            try:

                # --------------------------------
                # INQUIRY ANALYSIS
                # --------------------------------

                with st.spinner("Analyzing customer inquiry..."):

                    result = analyze_inquiry(inquiry)

                st.success("Inquiry analyzed successfully!")

                st.divider()

                # --------------------------------
                # MAIN ANALYSIS RESULTS
                # --------------------------------

                st.subheader("📊 Inquiry Analysis")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Category",
                        result["category"]
                    )

                with col2:

                    budget = result["budget"]

                    budget_display = (
                        f"₹{budget:,}"
                        if budget is not None
                        else "Not Provided"
                    )

                    st.metric(
                        "Budget",
                        budget_display
                    )

                with col3:

                    st.metric(
                        "Lead Score",
                        f'{result["lead_score"]}/100'
                    )

                st.divider()

                # --------------------------------
                # PROJECT DETAILS
                # --------------------------------

                st.subheader("📌 Project Details")

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f'**Timeline:** {result["timeline"]}'
                    )

                    st.write(
                        f'**Urgency:** {result["urgency"]}'
                    )

                with col2:

                    st.write(
                        f'**Project Scope:** {result["project_scope"]}'
                    )

                    st.write(
                        f'**Priority:** {result["priority"]}'
                    )

                # --------------------------------
                # LEAD PRIORITY
                # --------------------------------

                if result["priority"] == "High":

                    st.success("🟢 High Priority Lead")

                elif result["priority"] == "Medium":

                    st.warning("🟡 Medium Priority Lead")

                else:

                    st.info("🔵 Low Priority Lead")

                st.divider()

                # --------------------------------
                # SERVICE RECOMMENDATIONS
                # --------------------------------

                st.subheader("💡 Recommended Business Services")

                recommendation_result = recommend_services(
                    category=result["category"],
                    inquiry=inquiry
                )

                recommended_services = (
                    recommendation_result["recommended_services"]
                )

                st.write(
                    f'Recommendations for: '
                    f'**{recommendation_result["primary_category"]}**'
                )

                for index, service in enumerate(
                    recommended_services,
                    start=1
                ):

                    st.write(f"{index}. {service}")

                st.divider()

                # --------------------------------
                # LEAD SCORE BREAKDOWN
                # --------------------------------

                st.subheader("🎯 Lead Score Breakdown")

                breakdown = result["score_breakdown"]

                for component, details in breakdown.items():

                    score = details["score"]
                    reason = details["reason"]

                    st.write(
                        f"**{component}:** "
                        f"{score} points — {reason}"
                    )

                st.progress(
                    result["lead_score"] / 100
                )

                st.caption(
                    f'Total Lead Score: '
                    f'{result["lead_score"]}/100'
                )

                st.divider()

                # --------------------------------
                # GROQ AI RESPONSE
                # --------------------------------

                st.subheader("🤖 AI-Generated Customer Response")

                ai_response = "AI response could not be generated."
                ai_source = "Unavailable"

                try:

                    from response_generator import (
                        generate_customer_response
                    )

                    with st.spinner("Generating AI response..."):

                        ai_result = generate_customer_response(
                            inquiry,
                            result
                        )

                    ai_response = ai_result["response"]
                    ai_source = ai_result["source"]

                    if ai_result["success"]:

                        st.success(
                            "AI response generated successfully!"
                        )

                    else:

                        st.warning(
                            "AI service unavailable. "
                            "Using fallback response."
                        )

                except Exception as ai_error:

                    st.error(
                        f"AI response generation failed: {ai_error}"
                    )

                st.text_area(
                    "Generated Customer Reply:",
                    value=ai_response,
                    height=220,
                    key="generated_reply"
                )

                st.caption(f"Source: {ai_source}")

                st.divider()

                # --------------------------------
                # SAVE TO SQLITE DATABASE
                # --------------------------------

                try:

                    save_inquiry(
                        inquiry=inquiry,
                        analysis=result,
                        recommendations=recommended_services,
                        ai_response=ai_response
                    )

                    st.success(
                        "✅ Customer inquiry saved to database!"
                    )

                    st.metric(
                        "Total Saved Inquiries",
                        get_inquiry_count()
                    )

                except Exception as db_error:

                    st.error(
                        f"Database saving failed: {db_error}"
                    )

                st.divider()

                st.caption(
                    "Cynbit AI Business Inquiry Assistant | "
                    "Machine Learning + Rule-Based Lead Scoring "
                    "+ Service Recommendations + Groq AI + SQLite"
                )

            except Exception as error:

                st.error(
                    f"Analysis failed: {error}"
                )

                st.info(
                    "Please check your model files, preprocessing "
                    "code and inquiry analyzer."
                )


# ================================================
# TAB 2: INQUIRY HISTORY
# ================================================

with tab2:

    st.subheader("📂 Customer Inquiry History")

    try:

        records = get_all_inquiries()

        if records:

            st.metric(
                "Total Customer Inquiries",
                len(records)
            )

            # Prepare history table
            history_data = []

            for record in records:

                history_data.append({

                    "ID": record["id"],

                    "Category": record["category"],

                    "Budget": (
                        f'₹{record["budget"]:,}'
                        if record["budget"] is not None
                        else "Not Provided"
                    ),

                    "Timeline": record["timeline"],

                    "Urgency": record["urgency"],

                    "Scope": record["project_scope"],

                    "Lead Score": record["lead_score"],

                    "Priority": record["priority"],

                    "Created At": record["created_at"]

                })

            df = pd.DataFrame(history_data)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            # --------------------------------
            # VIEW INDIVIDUAL INQUIRY
            # --------------------------------

            st.subheader("🔍 View Inquiry Details")

            selected_id = st.selectbox(
                "Select Inquiry ID:",
                options=[record["id"] for record in records]
            )

            selected_record = next(
                record for record in records
                if record["id"] == selected_id
            )

            st.markdown("**Original Customer Inquiry**")

            st.write(selected_record["inquiry"])

            st.markdown("**Recommended Services**")

            import json

            services = json.loads(
                selected_record["recommended_services"] or "[]"
            )

            for service in services:

                st.write(f"• {service}")

            st.markdown("**Generated AI Response**")

            st.text_area(
                "Saved Customer Response:",
                value=selected_record["ai_response"] or "",
                height=180,
                disabled=True,
                key=f"saved_response_{selected_id}"
            )

        else:

            st.info(
                "No inquiries have been saved yet. "
                "Analyze a customer inquiry to get started."
            )

    except Exception as history_error:

        st.error(
            f"Unable to load inquiry history: {history_error}"
        )
