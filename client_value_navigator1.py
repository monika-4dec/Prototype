import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Expanded dummy dataset for impactful demo
data = {
    "Client": [f"Client {chr(i)}" for i in range(65, 77)],  # Client A to Client L
    "Industry": ["Finance","Retail","Healthcare","Energy","Banking","Retail","Finance","Energy","Healthcare","Utilities","Banking","Finance"],
    "Revenue (M USD)": [220, 430, 310, 507, 265, 398, 212, 350, 416, 195, 324, 275],
    "Current Solution": [
        "Legacy ERP", "Custom Analytics", "Manual reporting", "Cloud CRM", "Self-service BI", "No personalization",
        "Automated workflow", "Legacy claim processing", "Paper records", "Excel analytics", "RPA", "ML scoring"
    ],
    "Top Challenge": [
        "Real-time analytics", "Increase basket size", "Faster claims", "Cost-to-serve reduction", "Fraud detection",
        "Customer churn", "Reg risk", "Paper to digital", "Process automation", "Real-time analytics", "Upsell", "Cost control"
    ],
    "Customer Satisfaction": [82, 75, 90, 77, 88, 69, 80, 73, 86, 85, 78, 76],
    "Year-over-Year Growth (%)": [4.1, 9.5, 3.2, 6.4, 5.0, 8.7, 3.9, 7.2, 2.7, 4.8, 7.4, 5.3],
    "AI Maturity Score": [2, 4, 3, 5, 2, 3, 2, 4, 1, 3, 5, 3],  # scale 1-5
    "Active Engagements": [1, 3, 2, 4, 1, 0, 2, 3, 2, 1, 2, 1],
    "Segment": ["Enterprise", "Mid-market", "Enterprise", "Corporate", "Mid-market","SMB","SMB","Corporate","Enterprise","SMB","Mid-market","SMB"]
}
df = pd.DataFrame(data)

ai_solutions = {
    "Real-time analytics": "Deploy AI-powered real-time dashboards & anomaly detection.",
    "Increase basket size": "Implement personalized product recommendations and basket analysis.",
    "Faster claims": "Automate claims intake with OCR and AI triage workflow.",
    "Cost-to-serve reduction": "AI-driven process efficiency and cost optimization.",
    "Fraud detection": "Predictive fraud scoring using machine learning.",
    "Customer churn": "Deploy churn prediction and targeted retention strategies.",
    "Reg risk": "Automate regulatory compliance tracking with NLP.",
    "Paper to digital": "Digitize documents using NLP and computer vision.",
    "Process automation": "RPA solutions for workflow automation.",
    "Upsell": "Use propensity models for upsell/cross-sell opportunities.",
    "Cost control": "AI-based spend analysis and forecasting."
}

st.title("🌟Client Value Navigator Prototype")
st.markdown("Select your client to see rich insights, KPIs, trends & tailored AI opportunity.")

client = st.selectbox("Choose your Client:", df["Client"])
row = df[df["Client"] == client].iloc[0]
st.header(f"Client Dashboard: {row['Client']}")

col1, col2, col3 = st.columns(3)
col1.metric("Industry", row["Industry"])
col2.metric("Revenue (M USD)", f"{row['Revenue (M USD)']:,}")
col3.metric("YOY Growth Rate (%)", f"{row['Year-over-Year Growth (%)']:.1f}")

col1.metric("AI Maturity Score", row["AI Maturity Score"])
col2.metric("Customer Satisfaction", f"{row['Customer Satisfaction']}%")
col3.metric("Engagements", row["Active Engagements"])

st.success(f"Current Solution: {row['Current Solution']}")
st.warning(f"Top Challenge: {row['Top Challenge']}")
st.info(f"Segment: {row['Segment']}")

st.subheader("AI Opportunity Recommendation")
st.markdown(ai_solutions.get(row["Top Challenge"], "AI Opportunity to be discussed."))

# Show satisfaction trend for this client
st.markdown("### KPI Trend (Last 3 Years Estimate)")
years = ["2023", "2024", "2025"]
satisfaction_vals = [
    row['Customer Satisfaction']-4,
    row['Customer Satisfaction']-2,
    row['Customer Satisfaction']
]
fig, ax = plt.subplots()
ax.plot(years, satisfaction_vals, marker='o', color='orange')
ax.set_ylabel("Satisfaction (%)")
ax.set_ylim(60, 100)
ax.set_title(f"{client} Satisfaction Trend")
st.pyplot(fig)

# Show downloadable summary table for this user only
st.markdown("---")
with st.expander("Download My Data Table"):
    summary_table = pd.DataFrame([row])
    st.dataframe(summary_table)
    st.download_button("Download CSV", summary_table.to_csv(index=False).encode('utf-8'), f"{client}_summary.csv")

# KPI comparison for Admin/User Exploration (optional for demo)
st.markdown("### Context: Industry-wide Growth Distribution")
show_context = st.checkbox("Show anonymous industry comparison")
if show_context:
    fig2, ax2 = plt.subplots()
    df.groupby("Industry")["Year-over-Year Growth (%)"].mean().plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Avg YOY Growth (%)")
    st.pyplot(fig2)

# Question answer section retained
st.markdown("## Ask a Question about your client")
question = st.text_input("Ask e.g.: What is my AI score? My segment? My growth?")
def simple_rule_answer(q):
    q = q.lower()
    if "revenue" in q:
        return f"{client}'s revenue is ${row['Revenue (M USD)']}M."
    elif "challenge" in q:
        return f"{client}'s top challenge is '{row['Top Challenge']}'."
    elif "industry" in q:
        return f"{client} operates in the '{row['Industry']}' industry."
    elif "satisfaction" in q or "score" in q:
        return f"{client}'s customer satisfaction is {row['Customer Satisfaction']}%."
    elif "solution" in q:
        return f"Current solution for {client}: {row['Current Solution']}"
    elif "maturity" in q or "ai score" in q:
        return f"{client}'s AI Maturity Score is {row['AI Maturity Score']}."
    elif "segment" in q:
        return f"{client}'s market segment is {row['Segment']}."
    elif "engagement" in q:
        return f"{client} has {row['Active Engagements']} active engagements."
    elif "growth" in q:
        return f"{client}'s year-over-year growth rate is {row['Year-over-Year Growth (%)']}%."
    else:
        return "Sorry, try asking about revenue, challenge, industry, satisfaction, maturity, segment, engagements, or growth."
if question:
    st.success(simple_rule_answer(question))