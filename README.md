
# Cynbit AI Business Inquiry Assistant

An AI-powered business inquiry analysis system that helps businesses classify customer inquiries, extract project requirements, evaluate potential leads, recommend services, and generate professional responses.

## Project Overview

The Cynbit AI Business Inquiry Assistant automates the initial process of handling business inquiries.

It combines Machine Learning, rule-based processing, and Large Language Models (LLMs) to analyze customer requirements and provide structured business insights.

## Key Features

- **Inquiry Classification:** Classifies inquiries into six business categories using TF-IDF and Machine Learning.
- **Requirement Extraction:** Extracts budget, project timeline, and urgency from customer messages.
- **Project Scope Detection:** Identifies small, medium, or large project requirements using keyword-based rules.
- **Lead Scoring:** Calculates lead scores and assigns High, Medium, or Low priorities.
- **Service Recommendations:** Recommends relevant business services based on inquiry categories and keywords.
- **AI Response Generation:** Uses Groq LLM API to generate professional customer responses.
- **Inquiry Management:** Stores inquiry records and analysis results in an SQLite database.
- **Model Evaluation:** Compares Logistic Regression, Naive Bayes, and Linear SVM.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Machine Learning | Scikit-learn |
| Text Vectorization | TF-IDF |
| Classification Models | Logistic Regression, Naive Bayes, Linear SVM |
| Data Processing | Pandas |
| LLM Integration | Groq API |
| Database | SQLite |
| Model Serialization | Joblib |

## Machine Learning Approach

The project uses TF-IDF vectorization with Machine Learning classifiers to categorize customer inquiries.

### Supported Categories

1. AI Automation
2. Web Development
3. App Development
4. Cloud Services
5. Data Analytics
6. General Inquiry

### Model Comparison

The following models were evaluated using a manually prepared test dataset containing 12 inquiries.

| Model | Accuracy | Macro F1 |
|---|---:|---:|
| Logistic Regression | 100% | 100% |
| Naive Bayes | 100% | 100% |
| Linear SVM | 91.67% | 93.33% |

**Selected Model:** Logistic Regression

Note: These results represent performance on a small manually prepared test dataset. They should not be interpreted as real-world accuracy.

## Project Architecture

```text
Customer Inquiry
       |
       v
Streamlit Application
       |
       v
Inquiry Analyzer
       |
       +----------------------+
       |                      |
       v                      v
ML Classification      Requirement Extraction
       |                      |
       v                      v
Inquiry Category       Budget / Timeline / Urgency
       |                      |
       +-----------+----------+
                   |
                   v
             Scope Detection
                   |
                   v
              Lead Scoring
                   |
                   v
          Service Recommendations
                   |
                   v
          Groq LLM Response
                   |
                   v
             SQLite Database
                   |
                   v
             Results Display
```

## Project Structure

```text
cynbit-AI-Inquiry-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── business_inquiries.csv
│   ├── generate_dataset.py
│   └── test_inquiries.csv
│
├── models/
│   ├── all_models.pkl
│   ├── best_classifier.pkl
│   └── model_comparison.csv
│
└── src/
    ├── agents.py
    ├── classifier.py
    ├── database.py
    ├── evaluate_unseen.py
    ├── inquiry_analyzer.py
    ├── lead_scoring.py
    ├── preprocessing.py
    ├── recommendation_engine.py
    └── response_generator.py
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sahil-0905/cynbit-AI-Inquiry-Assistant.git
```

### 2. Navigate to the Project

```bash
cd cynbit-AI-Inquiry-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Groq API

Create a `.env` file in the project root directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

Never upload your `.env` file or API key to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Model Evaluation

To evaluate the trained classification models, run:

```bash
python src/evaluate_unseen.py
```

The evaluation reports:

- Accuracy
- Macro Precision
- Macro Recall
- Macro F1-score
- Classification Report
- Confusion Matrix

## Example Inquiry

```text
We need an AI chatbot for our e-commerce business
to handle customer queries and automate order tracking.
Our budget is ₹1,50,000, and we need the project
completed within 30 days. This is urgent.
```

The application analyzes the inquiry and generates:

- Predicted business category
- Extracted budget and timeline
- Urgency level
- Project scope
- Lead score and priority
- Recommended services
- AI-generated customer response

## Future Improvements

- Expand the dataset with more diverse real-world inquiries.
- Improve classification performance using larger datasets.
- Develop more advanced requirement extraction.
- Improve recommendation relevance.
- Add lead analytics and reporting dashboards.
- Deploy the application to a cloud platform.

## Author

**Sahil Kumar**

GitHub: [sahil-0905](https://github.com/sahil-0905)

---

**Disclaimer:** This project is developed as an AI/ML assessment project. Some components, including lead scoring, project scope detection, and service recommendations, use rule-based logic rather than trained Machine Learning models.
