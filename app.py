import streamlit as st
import joblib
import pandas as pd
import numpy as np
#Load model and features
model = joblib.load("MTN_Churn_Model.pkl")
features = joblib.load("feature_list.pkl")

st.set_page_config(page_title="MTN Churn Predictor")
st.title("MTN Churn Prediction Dashboard")
st.markdown("Enter customer details here")

#Sidebar for User inputs
st.sidebar.header("Customer Profile")
age =st.sidebar.slider("Age",18,90,30)
revenue = st.sidebar.number_input("Total Revenue (\u20A6)",0,1000000,50000)
tenure = st.sidebar.number_input("Customer Tenure in months",0,120,24)
gender = st.sidebar.selectbox("Gender",["Male","Female"])
satisfaction = st.sidebar.slider("Satisfaction Score", 1,5,3)
zone = st.sidebar.selectbox("Geopolitical Zone",["South West","South East","North Central","North West","North East","South South"])
device = st.sidebar.selectbox("Device Type",["Mobile SIM Card","Broadband MiFi","5G Router"])

if st.button("Predict"):
    input_data = {
        "Age":age,
        "Customer Tenure in months":tenure,
        "Total Revenue":revenue,
        "Satisfaction Score":satisfaction,
        f"Geopolitical Zone_{zone}":1,
        f"Gender_{gender}":1
    }
    
    input_df = pd.DataFrame(0, index=[0], columns=features)

    for col,val in input_data.items():
        if col in features:
            input_df[col] = val
    
    if f"Geopolitical Zone_{zone}" in features:
        input_df[f"Geopolitical Zone_{zone}"] = 1
    if f"Gender_{gender}"in features:
        input_df[f"Gender_{gender}"] = 1
    if f"MTN Device_{device}" in features:
        input_df[f"MTN Device_{device}"] = 1

    input_df = input_df.reindex(columns=features, fill_value=0)

    risk_prob = model.predict_proba(input_df)[0,1]
    # display results
    st.subheader("Analysis Results")
    
    col1,col2 = st.columns(2)
    with col1:
        st.metric("Churn Probability",f"{risk_prob:.1%}")

    with col2:
        revenue_at_risk = risk_prob * revenue
        st.metric("Revenue at Risk",f"\u20A6{revenue_at_risk:,.2f}")
        
    if risk_prob > 0.40:
        st.error(f"High Risk: This customer is {risk_prob:.1%} likely to leave.")
        st.info("**Recommendation:** Offer 10GB Loyalty Data Bundle + 10% Discount on the next MiFi upgrade.")
    else:
        st.success(f"Low Risk: This customer is {risk_prob:.1%} likely to stay.")

st.info("Built for the MTN Churn Intelligence Portfolio Project")
