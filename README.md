# Credit Risk Modeling & Prediction

A production-style Machine Learning project for predicting customer credit risk using financial and demographic attributes.

This project implements an end-to-end credit risk assessment pipeline, including data preprocessing, exploratory analysis, model training, evaluation, and deployment through an interactive Streamlit application.

---

## Overview

Financial institutions rely heavily on accurate credit risk assessment to minimize loan defaults and optimize lending decisions.

This project uses supervised machine learning techniques to classify applicants as:

- **Good Credit Risk**
- **Bad Credit Risk**

The system is designed to simulate a practical credit risk prediction workflow used in banking and financial analytics.

---

## Features

- End-to-end machine learning pipeline
- Exploratory Data Analysis (EDA)
- Data preprocessing and feature encoding
- Multiple classification model evaluation
- Hyperparameter optimization
- Real-time prediction using Streamlit
- Model persistence using Joblib
- Clean and scalable project structure

---

## Tech Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Deployment | Streamlit |
| Model Serialization | Joblib |
| Development Environment | Jupyter Notebook |

---

## Machine Learning Models

The following models were trained and evaluated:

- Decision Tree Classifier
- Random Forest Classifier
- Extra Trees Classifier
- XGBoost Classifier

### Final Selected Model
**Extra Trees Classifier**

The model demonstrated the best overall predictive performance and was selected for deployment.

---

## Project Structure

```bash
credit-risk-modeling/
│
├── analysis_model.ipynb
├── app.py
├── german_credit_data.csv
├── extra_trees_credit_model.pkl
├── Sex_encoder.pkl
├── Housing_encoder.pkl
├── Saving_accounts_encoder.pkl
├── Checking_accounts_encoder.pkl
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/RutvijAhlaad/credit-risk-modeling.git
cd credit-risk-modeling
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application locally:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## Streamlit Application

The application allows users to provide:

- Age
- Sex
- Job Category
- Housing Status
- Saving Account Status
- Checking Account Status
- Credit Amount
- Loan Duration

The trained model then predicts the applicant’s credit risk category in real time.

---

## Key Objectives

- Automate credit risk assessment
- Improve lending decision efficiency
- Demonstrate practical machine learning deployment
- Build a real-world finance analytics project

---

## Future Improvements

- Probability-based risk scoring
- SHAP explainability integration
- API deployment using FastAPI
- Docker containerization
- Cloud deployment
- CI/CD integration
- Advanced feature engineering

---

## Author

### Rutvij Ahlaad

- GitHub: https://github.com/RutvijAhlaad

---

## License

This project is intended for educational and portfolio purposes.
