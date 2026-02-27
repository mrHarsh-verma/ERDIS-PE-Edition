import streamlit as st
from pyairtable import Api

# ERDIS PE Edition: Public Deployment Configuration
st.set_page_config(page_title="ERDIS | Portfolio Governance", layout="wide")

# Section: Secure Credential Management
AIRTABLE_API_KEY = st.secrets["AIRTABLE_API_KEY"]
BASE_ID = st.secrets["BASE_ID"]
api = Api(AIRTABLE_API_KEY)
table = api.table(BASE_ID, "Executive Briefs")

# Header
st.title("ERDIS: Portfolio Governance Command")
st.caption("Value Creation Intelligence | 27 Feb 2026")

# Section 1: Portfolio Health Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Weekly Stability Score", "1.58", "-0.12 (Stabilizing)")
col2.metric("Active EBITDA Exposure", "$233.2M", "Priority: HIGH")
with col3:
    st.metric("System Status", "OPERATIONAL")
    st.caption("Data Source Layer: Simulated ERP Feed (Demo Mode)")

st.divider()

# Section 2: Executive Narrative Brief
st.subheader("Latest Executive Briefing")

# This part pulls the live data from your Airtable
records = table.all(sort=["-Brief Date"])
if records:
    narrative = records[0]['fields'].get('Narrative Output', "Waiting for next briefing cycle...")
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 15px; border: 1px solid #e6e9ef; border-radius: 5px;">
        {narrative}
    </div>
    """, unsafe_allow_html=True)
else:
    st.info("Connected to governance engine. Awaiting primary signals.")

st.divider()

# Section 3: Monitoring Scope
st.subheader("Monitoring Scope")
scope_col1, scope_col2 = st.columns(2)
with scope_col1:
    st.write("• ERP journal entries")
    st.write("• Procurement overrides")
    st.write("• Intercompany adjustments")
with scope_col2:
    st.write("• CapEx approvals")
    st.write("• Working capital anomalies")

st.divider()
st.caption("INTERNAL USE ONLY | Simulated data for demonstration purposes.")
