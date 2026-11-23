# Technical Approach Report
## Cynbit AI Business Inquiry Assistant

**Prepared by:** Sahil Kumar  
**Project:** Cynbit AI Business Inquiry Assistant  
**Technology:** Python, Machine Learning, Streamlit, Groq API, SQLite

---

## 1. Introduction

The Cynbit AI Business Inquiry Assistant is a Proof of Concept designed to automate the initial analysis of customer business inquiries.

The application combines Machine Learning, rule-based processing, and Large Language Models to classify inquiries, extract project requirements, prioritize leads, recommend services, and generate customer responses.

## 2. System Architecture

The application follows a modular architecture consisting of the following components:

1. Streamlit frontend
2. Inquiry classification module
3. Requirement extraction module
4. Project scope detection module
5. Lead scoring module
6. Service recommendation engine
7. LLM response generation module
8. SQLite database

### Processing Workflow

```text
Customer Inquiry
       |
       v
Streamlit Frontend
       |
       v
Inquiry Classification
       |
       v
Requirement Extraction
       |
       v
Project Scope Detection
       |
       v
Lead Scoring
       |
       v
Service Recommendations
       |
       v
Groq LLM Response Generation
       |
       v
SQLite Database
       |
       v
Display Results
```

## 3. Machine Learning Classification

### 3.1 Dataset

A synthetic dataset was generated using Python for training and testing the inquiry classification system.

The dataset contains six categories:

- AI Automation
- Web Development
- App Development
- Cloud Services
- Data Analytics
- General Inquiry

The generated training dataset contains 300 records.

### 3.2 Text Preprocessing and Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert inquiry text into numerical features.

The classifier uses unigram and bigram features to capture individual words and short phrases.

### 3.3 Algorithms Evaluated

Three classification algorithms were compared:

- Logistic Regression
- Multinomial Naive Bayes
- Linear Support Vector Machine

Logistic Regression was selected for the current application because it achieved the same test performance as Naive Bayes and was chosen as the deployed classifier.

### 3.4 Evaluation Results

The models were evaluated on 12 manually prepared test inquiries.

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Logistic Regression | 100% | 100% |
| Naive Bayes | 100% | 100% |
| Linear SVM | 91.67% | 93.33% |

These results are limited to the small test dataset and do not establish real-world performance.

## 4. Requirement Extraction

The preprocessing module uses Python regular expressions to extract structured information from customer inquiries.

The extracted fields include:

- Budget
- Project timeline
- Urgency level

For example, the system can identify a budget of ₹1,50,000 and a timeline of 30 days from a customer message.

Urgency is identified using predefined keywords such as urgent, ASAP, and immediately.

## 5. Project Scope Detection

The project scope module uses keyword-based rules to estimate project complexity.

It identifies three levels:

- Small
- Medium
- Large

Keywords such as landing page and basic website indicate small projects.

Keywords such as payment gateway, e-commerce, and admin dashboard indicate medium projects.

Keywords such as enterprise, end-to-end, and multiple integrations indicate large projects.

This is rule-based detection, not a trained ML model.

## 6. Lead Scoring System

The lead scoring module assigns points based on budget, urgency, and project scope.

### Scoring Logic

| Factor | Condition | Score |
|---|---|---:|
| Budget | ₹1,00,000 or above | 40 |
| Budget | ₹50,000 or above | 30 |
| Budget | ₹10,000 or above | 20 |
| Budget | Below ₹10,000 | 10 |
| Budget | Not specified | 20 |
| Urgency | High | 30 |
| Urgency | Medium | 20 |
| Urgency | Low | 10 |
| Scope | Large | 30 |
| Scope | Medium or unspecified | 20 |
| Scope | Small | 10 |

### Priority Assignment

- Score 75 or above: High
- Score 50–74: Medium
- Score below 50: Low

The scoring system uses predefined business rules and is not trained on historical sales conversion data.

## 7. Service Recommendation Engine

The recommendation engine suggests services based on the predicted inquiry category and predefined keywords.

Examples include:

| Inquiry Category | Example Recommendations |
|---|---|
| AI Automation | AI Chatbot Development, Workflow Automation |
| Web Development | Website Development, E-commerce Development |
| App Development | Android, iOS, Cross-Platform Development |
| Cloud Services | AWS Migration, Cloud Infrastructure |
| Data Analytics | Business Intelligence, Data Visualization |
| General Inquiry | Business Consultation |

The current recommendation engine uses predefined rules rather than a trained recommendation model.

## 8. LLM Integration

The application integrates the Groq API to generate professional customer responses.

The response generation module:

1. Receives the original inquiry.
2. Uses the extracted requirements and predicted category.
3. Constructs a prompt for the LLM.
4. Generates a professional response.
5. Returns the response to the Streamlit interface.

A fallback response is provided when the API request fails.

The LLM is used for response generation, not for the primary inquiry classification.

## 9. Database Design

SQLite is used to store inquiry records.

The database contains the following fields:

| Field | Description |
|---|---|
| id | Unique inquiry identifier |
| inquiry | Original customer inquiry |
| category | Predicted inquiry category |
| budget | Extracted budget |
| timeline | Project timeline |
| urgency | Urgency level |
| project_scope | Estimated project scope |
| lead_score | Calculated lead score |
| priority | Assigned lead priority |
| recommended_services | Suggested services |
| ai_response | Generated customer response |
| created_at | Record creation timestamp |

The application also provides an inquiry history interface.

## 10. Testing and Validation

The project was tested using:

- Model evaluation on 12 manually prepared inquiries.
- Different business inquiry categories.
- Budget and timeline extraction examples.
- High and low urgency examples.
- Service recommendation examples.
- Groq response generation.
- SQLite database storage and retrieval.

Further testing with larger, independently collected datasets is required before production deployment.

## 11. Limitations

- The training dataset is synthetic.
- The unseen test dataset contains only 12 records.
- Regex extraction may fail on complex natural-language expressions.
- Lead scoring uses fixed rules.
- Service recommendations use predefined keywords.
- LLM output may require human review.
- Production deployment requires additional security, monitoring, and validation.

## 12. Future Enhancements

- Increase training and testing dataset diversity.
- Improve text classification using real business inquiries.
- Develop more robust NLP-based requirement extraction.
- Improve recommendation relevance.
- Train lead scoring models using historical sales outcomes.
- Add user authentication and role-based access.
- Deploy the application to a cloud platform.
- Add monitoring and analytics dashboards.

## 13. Conclusion

The Cynbit AI Business Inquiry Assistant demonstrates a modular approach to automating business inquiry management.

By combining Machine Learning, rule-based processing, LLM integration, and database storage, the system provides a functional Proof of Concept.

The current implementation establishes a foundation for future improvements and real-world pilot testing.

---

**GitHub Repository:** https://github.com/sahil-0905/cynbit-AI-Inquiry-Assistant
