# Customer-Churn-Predictor
# 📉 Customer Churn Predictor

A Machine Learning project that predicts whether a telecom customer is likely to churn (leave the service) based on customer demographics, account information, contract details, and service usage.

The project uses a Random Forest Classifier trained on the Telco Customer Churn Dataset and includes data cleaning, exploratory data analysis (EDA), feature engineering, model evaluation, and deployment-ready model serialization.

---

## 🚀 Project Overview

Customer churn is one of the most important business problems for subscription-based companies. Acquiring new customers is often more expensive than retaining existing ones.

This project helps identify customers who are likely to leave the company so that proactive retention strategies can be implemented.

---

## ✨ Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- One-Hot Encoding of Categorical Features
- Random Forest Classification
- Model Evaluation using Multiple Metrics
- Confusion Matrix Visualization
- Feature Importance Analysis
- Model Serialization using Pickle
- Deployment-Ready Prediction Pipeline

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries Used
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Pickle

---

## 📊 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer information such as:

- Gender
- Senior Citizen Status
- Partner & Dependents
- Tenure
- Phone Service
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

### Target Variable

| Value | Meaning |
|---------|---------|
| 0 | Customer Retained |
| 1 | Customer Churned |

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

- Removed `customerID` column
- Converted `TotalCharges` from object to numeric
- Handled missing values using median imputation
- Checked and removed inconsistencies
- Verified data types
- Removed remaining null values

---

## 📈 Exploratory Data Analysis (EDA)

Several visualizations were created to understand customer behavior:

- Churn Distribution
- Churn by Contract Type
- Churn by Gender
- Churn by Internet Service
- Monthly Charges Distribution
- Customer Tenure Distribution
- Tenure vs Churn Analysis

### Key Insights

- Customers with month-to-month contracts tend to churn more.
- Customers with shorter tenure are more likely to leave.
- Internet service type impacts churn behavior.
- Monthly charges show correlation with customer retention.

---

## ⚙️ Feature Engineering

### Steps Performed

1. Converted target variable:
   - Yes → 1
   - No → 0

2. Identified categorical features.

3. Applied One-Hot Encoding using:

```python
pd.get_dummies(drop_first=True)
```

4. Generated a fully numeric dataset suitable for machine learning.

---

## 🤖 Machine Learning Model

### Algorithm Used

**Random Forest Classifier**

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

### Why Random Forest?

- Handles non-linear relationships
- Robust against overfitting
- Works well with mixed feature types
- Provides feature importance scores

---

## 📂 Train-Test Split

```python
test_size = 0.20
random_state = 42
stratify = y
```

- Training Data: 80%
- Testing Data: 20%

---

## 📏 Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix

```python
accuracy_score()
precision_score()
recall_score()
f1_score()
classification_report()
```

---

## 📌 Feature Importance

The Random Forest model identifies the most influential factors affecting customer churn.

Examples of important features include:

- Contract Type
- Tenure
- Monthly Charges
- Total Charges
- Internet Service

---

## 💾 Model Saving

The trained model is saved using Pickle:

```python
customer_churn_model.pkl
```

Feature names are also stored:

```python
feature_columns.pkl
```

This allows seamless deployment without retraining.

---

## 📁 Project Structure

```bash
Customer-Churn-Predictor/
│
├── app.py
├── customer_churn_model.pkl
├── feature_columns.pkl
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── requirements.txt
├── README.md
│
└── notebooks/
    └── churn_analysis.ipynb
```

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-predictor.git
```

### Navigate to Project

```bash
cd customer-churn-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

or

```bash
python app.py
```

depending on your deployment setup.

---

## 🔮 Future Improvements

- XGBoost Implementation
- Hyperparameter Tuning
- Cross Validation
- Model Explainability using SHAP
- Real-Time Customer Monitoring Dashboard
- Cloud Deployment

---

## 📷 Application Preview

Add screenshots of your dashboard here:

```markdown
![Dashboard Screenshot](images/dashboard.png)
```

---

## 🎯 Business Impact

By identifying customers likely to churn, businesses can:

- Improve customer retention
- Reduce revenue loss
- Increase customer lifetime value
- Design targeted retention campaigns

---

## 👨‍💻 Author

**Devam Dadhia**

Aspiring Engineer | Machine Learning Enthusiast | Python Developer

---

## ⭐ If you found this project useful, consider giving it a star!
