# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 13:10:46 2025

@author: Monika201103
"""
import streamlit as st
import pandas as pd

data = {
    "Client": ["NEXT", "Loreal", "FinTrust", "HealthGen", "RetailMax"],
    "Industry": ["Finance", "Healthcare", "Banking", "Utilies", "Retail"],
    "Revenue (M USD)": [200, 300, 150, 400, 250],
    "Current Solution": ["Manual reporting", "Legacy claim processing", "Excel analytics", "Paper records", "No personalization"],
    "Top Challenge": ["Real-time analytics", "Faster claims", "Fraud detection", "Paper to digital", "Increase basket size"],
}
df = pd.DataFrame(data)

ai_solutions = {
    "Real-time analytics": "Deploy AI-powered real-time dashboards & anomaly detection.",
    "Faster claims": "Automate claims intake with OCR and AI triage workflow.",
    "Fraud detection": "Implement predictive fraud scoring with ML models.",
    "Paper to digital": "Digitize records using document AI & NLP extraction.",
    "Increase basket size": "Personalized product recommendations using customer analytics.",
}

st.title("EXL Client Value Navigator (Demo)")

client = st.selectbox("Select Client", df["Client"])
row = df[df["Client"] == client].iloc[0]

st.write(f"**Industry:** {row['Industry']}")
st.write(f"**Current Solution:** {row['Current Solution']}")
st.write(f"**Top Challenge:** {row['Top Challenge']}")

st.markdown("---")
st.subheader("AI Opportunity Recommendation")
st.write(ai_solutions[row["Top Challenge"]])

st.markdown("---")
with st.expander("Show All Clients & Challenges"):
    st.dataframe(df)
