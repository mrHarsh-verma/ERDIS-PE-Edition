import streamlit as st

# ERDIS PE Edition: Public Deployment Configuration
st.set_page_config(page_title="ERDIS | Portfolio Governance", layout="wide")

# Header
st.title("ERDIS: Portfolio Governance Command")
st.caption("Value Creation Intelligence | 27 Feb 2026")

# Section 1: Portfolio Health Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Weekly Stability Score", "1.58", "-0.12 (Stabilizing)")
col2.metric("Active EBITDA Exposure", "$233.2M", "Priority: HIGH")

# 1️⃣ Adjustment: Adding Data Source Layer Line
with col3:
    st.metric("System Status", "OPERATIONAL")
    st.caption("Data Source Layer: Simulated ERP Feed (Demo Mode)")

st.divider()

# Section 2: Executive Narrative
st.subheader("Latest Executive Briefing")
st.markdown("""
<div style="background-color: #ffffff; padding: 15px; border: 1px solid #e6e9ef; border-radius: 5px;">
    <h4 style="color: #000000; margin-top: 0;">Portfolio Governance Alert: EBITDA Bridge Integrity</h4>
    <p><b>EBITDA Bridge Impact:</b> <span style="color: #b00020;">Estimated -$1.2M (90-day)</span></p>
    <p><b>Analysis:</b> Detection of a high-value manual ledger adjustment ($1.1B) alongside systematic procurement bypasses and internal communication silos in EMEA operations.</p>
    <p><b>Exit Readiness Risk:</b> <span style="color: #b00020;">CRITICAL</span></p>
    <hr>
    <h4 style="color: #000000;">Critical Decision: CFO Intervention</h4>
    <p>Immediate audit intervention required to validate the $1.1B manual entry prior to period-end disclosure to prevent potential material weakness findings.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 2️⃣ Adjustment: Adding Subtle Monitoring Scope Box
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
