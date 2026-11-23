# AI Opportunity Report
## Cynbit AI Business Inquiry Assistant

**Prepared for:** Cynbit Technologies  
**Project:** AI Business Inquiry Assistant  
**Prepared by:** Sahil Kumar

---

## 1. Executive Summary

Cynbit Technologies provides AI automation, custom software development, cloud infrastructure, and SaaS solutions.

Businesses receiving multiple customer inquiries may spend significant time manually understanding requirements, identifying suitable services, prioritizing potential customers, and preparing responses.

The proposed AI Business Inquiry Assistant aims to streamline this process using Machine Learning, rule-based automation, and Large Language Models (LLMs).

The system analyzes incoming inquiries, identifies business requirements, assigns lead priorities, recommends services, and generates professional customer responses.

## 2. Business Problem

Manual inquiry management can create several operational challenges:

- Difficulty categorizing incoming customer inquiries.
- Time-consuming extraction of project requirements.
- Inconsistent lead prioritization.
- Delays in preparing customer responses.
- Difficulty maintaining organized inquiry records.

These challenges can affect response efficiency and the customer experience.

## 3. Proposed AI Opportunity

The proposed solution is an AI-powered Business Inquiry Assistant.

It processes customer messages and produces structured information to support business inquiry management.

### Core Capabilities

1. **Inquiry Classification:** Categorizes inquiries into AI Automation, Web Development, App Development, Cloud Services, Data Analytics, and General Inquiry.
2. **Requirement Extraction:** Identifies project budget, timeline, and urgency.
3. **Project Scope Detection:** Estimates whether a project is small, medium, or large using predefined rules.
4. **Lead Scoring:** Calculates a score and assigns High, Medium, or Low priority.
5. **Service Recommendations:** Suggests relevant Cynbit services.
6. **AI Response Generation:** Uses a Groq-hosted LLM to generate professional customer responses.
7. **Inquiry Management:** Stores inquiry details and analysis results in SQLite.

## 4. Proposed Technology

| Component | Technology |
|---|---|
| Programming | Python |
| Frontend | Streamlit |
| Text Processing | TF-IDF |
| Classification | Logistic Regression |
| Model Comparison | Naive Bayes, Linear SVM |
| Requirement Extraction | Python Regex |
| Lead Scoring | Rule-based logic |
| Service Recommendations | Rule-based logic |
| Response Generation | Groq LLM API |
| Database | SQLite |
| Data Processing | Pandas |
| Model Serialization | Joblib |

## 5. Expected Business Benefits

- Reduce repetitive manual inquiry analysis.
- Organize customer requirements in a structured format.
- Support consistent lead prioritization.
- Help identify relevant business services.
- Generate initial customer responses more efficiently.
- Maintain searchable inquiry records.

These are expected benefits; actual time savings and business impact require measurement in a real deployment.

## 6. Implementation Approach

The solution follows a modular architecture:

1. Customer submits an inquiry through the Streamlit interface.
2. The ML classifier predicts the inquiry category.
3. The requirement extraction module identifies budget, timeline, and urgency.
4. The scope detection module estimates project size.
5. The lead scoring module calculates the priority.
6. The recommendation engine suggests relevant services.
7. The Groq LLM generates a customer response.
8. SQLite stores the inquiry and its analysis.

## 7. Evaluation and Testing

Three classification algorithms were evaluated:

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Logistic Regression | 100% | 100% |
| Naive Bayes | 100% | 100% |
| Linear SVM | 91.67% | 93.33% |

The evaluation used a manually prepared dataset of 12 test inquiries.

Logistic Regression was selected for the application.

**Evaluation limitation:** The test dataset is small, and the results should not be interpreted as evidence of 100% real-world classification accuracy. Larger and more diverse datasets are required for reliable validation.

## 8. Risks and Limitations

- Synthetic training data may not represent real customer language.
- Small test datasets limit the reliability of evaluation results.
- Regex-based extraction may miss complex budget and timeline expressions.
- Rule-based lead scoring may not reflect actual sales conversion probability.
- Service recommendations depend on predefined categories and keywords.
- LLM-generated responses may occasionally require human review.
- API availability and usage limits may affect response generation.

## 9. Future Improvements

- Collect and label real customer inquiry data.
- Expand the evaluation dataset.
- Improve requirement extraction using NLP techniques.
- Refine lead scoring using historical business outcomes.
- Improve service recommendation relevance.
- Add inquiry analytics and reporting.
- Deploy the application for real-world pilot testing.

## 10. Conclusion

The Cynbit AI Business Inquiry Assistant demonstrates how Machine Learning, rule-based automation, and LLMs can work together to improve business inquiry management.

The Proof of Concept provides a functional foundation for inquiry classification, requirement extraction, lead prioritization, service recommendations, customer response generation, and inquiry storage.

Further testing with real business data would be necessary before production deployment.

---

**Project Repository:** https://github.com/sahil-0905/cynbit-AI-Inquiry-Assistant
