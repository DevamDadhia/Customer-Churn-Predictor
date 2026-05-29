import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn (1).csv")
from sklearn.ensemble import RandomForestClassifier 
# ==========================================
# TRAIN MODEL USING ONLY 5 FEATURES
# ==========================================

selected_features = [
    "tenure",
    "MonthlyCharges",
    "Contract",
    "TechSupport",
    "OnlineSecurity"
]

df_small = df[selected_features + ["Churn"]].copy()

# Encode target
df_small["Churn"] = df_small["Churn"].map({
    "Yes": 1,
    "No": 0
})

# Separate X and y
X = df_small.drop("Churn", axis=1)
y = df_small["Churn"]

# One-hot encoding
X = pd.get_dummies(X, drop_first=True)

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Random Forest
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

# Save model
import pickle

with open("cust_churn_model.pkl", "wb") as file:
    pickle.dump(rf, file)

with open("feature_columns.pkl", "wb") as file:
    pickle.dump(X.columns.tolist(), file)

print("New 5-feature model saved successfully!")