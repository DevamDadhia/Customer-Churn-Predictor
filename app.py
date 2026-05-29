
import streamlit as st
import pickle
import pandas as pd

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

# =========================================
# LOAD MODEL
# =========================================

with open("cust_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("feature_columns.pkl", "rb") as file:
    feature_columns = pickle.load(file)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: #F4F7FC;
}

/* Header */

.main-header {
    background: linear-gradient(
        90deg,
        #06B6D4,
        #2563EB,
        #7C3AED
    );
    padding: 24px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
}

.main-header h1 {
    color: white;
    font-size: 44px;
    margin: 0;
    font-weight: 800;
}

/* Section Card */

.input-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Labels */

label,
.stSelectbox label,
[data-testid="stWidgetLabel"] {
    color: #111827 !important;
    font-size: 17px !important;
    font-weight: 700 !important;
}

/* Select Boxes */

div[data-baseweb="select"] > div {
    background: white !important;
    border: 2px solid #D1D5DB !important;
    border-radius: 12px !important;
    min-height: 50px;
}

div[data-baseweb="select"] span {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Button */

.stButton > button {
    width: 100%;
    height: 58px;
    border: none;
    border-radius: 14px;
    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );
    color: white;
    font-size: 20px;
    font-weight: 700;
    margin-top: 15px;
}

.stButton > button:hover {
    transform: scale(1.01);
}

/* Probability Card */

.prob-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    margin-top: 25px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.10);
}

.prob-title {
    color: #475569;
    font-size: 18px;
    font-weight: 600;
}

.prob-value {
    color: #2563EB;
    font-size: 68px;
    font-weight: 800;
}

/* Risk Cards */

.high-risk {
    background: #EF4444;
    color: white;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.medium-risk {
    background: #F59E0B;
    color: white;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.low-risk {
    background: #22C55E;
    color: white;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.markdown("""
<div class="main-header">
    <h1>Customer Churn Predictor</h1>
</div>
""", unsafe_allow_html=True)

# =========================================
# INPUT SECTION
# =========================================

st.markdown("### Customer Details")

col1, col2 = st.columns(2)

with col1:
    tenure_option = st.selectbox(
        "Tenure",
        [
            "Less than 6 Months",
            "6-12 Months",
            "1-2 Years",
            "2-5 Years",
            "More than 5 Years"
        ]
    )

with col2:
    monthly_option = st.selectbox(
        "Monthly Charges",
        [
            "Low",
            "Medium",
            "High",
            "Very High"
        ]
    )

col3, col4 = st.columns(2)

with col3:
    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-Month",
            "One Year",
            "Two Year"
        ]
    )

with col4:
    tech_support = st.selectbox(
        "Tech Support",
        [
            "Yes",
            "No"
        ]
    )

online_security = st.selectbox(
    "Online Security",
    [
        "Yes",
        "No"
    ]
)

# =========================================
# VALUE CONVERSION
# =========================================

tenure_map = {
    "Less than 6 Months": 3,
    "6-12 Months": 9,
    "1-2 Years": 18,
    "2-5 Years": 42,
    "More than 5 Years": 72
}

monthly_map = {
    "Low": 25,
    "Medium": 55,
    "High": 85,
    "Very High": 110
}

tenure = tenure_map[tenure_option]
monthly_charges = monthly_map[monthly_option]

# =========================================
# PREDICTION
# =========================================

if st.button("Predict Churn"):

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges

    if contract == "One Year":
        input_data["Contract_One year"] = 1

    elif contract == "Two Year":
        input_data["Contract_Two year"] = 1

    if tech_support == "Yes":
        input_data["TechSupport_Yes"] = 1

    if online_security == "Yes":
        input_data["OnlineSecurity_Yes"] = 1

    probability = model.predict_proba(input_data)[0][1]

    st.markdown(
        f"""
        <div class="prob-card">
            <div class="prob-title">
                Churn Probability
            </div>
            <div class="prob-value">
                {probability*100:.2f}%
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if probability >= 0.70:

        st.markdown(
            """
            <div class="high-risk">
            🔴 HIGH RISK CUSTOMER
            </div>
            """,
            unsafe_allow_html=True
        )

    elif probability >= 0.40:

        st.markdown(
            """
            <div class="medium-risk">
            🟠 MEDIUM RISK CUSTOMER
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="low-risk">
            🟢 LOW RISK CUSTOMER
            </div>
            """,
            unsafe_allow_html=True
        )

