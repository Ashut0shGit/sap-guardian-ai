import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st

from agents.transport_agent import TransportAgent
from agents.risk_analysis_agent import RiskAnalysisAgent


st.set_page_config(
    page_title="SAP Guardian AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SAP Guardian AI")
st.subheader(
    "AI-Powered SAP Transport Risk Analyzer"
)

transport_id = st.text_input(
    "Enter SAP Transport ID",
    placeholder="Example: DEVK900451"
)

if st.button("Analyze Transport"):

    if not transport_id:
        st.warning(
            "Please enter a transport ID."
        )

    else:

        with st.spinner(
            "Analyzing transport..."
        ):

            data = (
                TransportAgent.analyze_transport(
                    transport_id
                )
            )

            analysis = (
                RiskAnalysisAgent.analyze(
                    data["transport"],
                    data["incidents"]
                )
            )

        st.success(
            "Analysis completed successfully."
        )

        # ----------------------------
        # Risk Level Extraction
        # ----------------------------

        risk_level = "UNKNOWN"

        if "HIGH" in analysis:
            risk_level = "HIGH"

        elif "MEDIUM" in analysis:
            risk_level = "MEDIUM"

        elif "LOW" in analysis:
            risk_level = "LOW"

        # ----------------------------
        # Dashboard Metrics
        # ----------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Risk Level",
                risk_level
            )

        with col2:
            st.metric(
                "Transport ID",
                transport_id
            )

        # ----------------------------
        # Colored Status Banner
        # ----------------------------

        if risk_level == "HIGH":
            st.error(
                "🔴 HIGH RISK TRANSPORT"
            )

        elif risk_level == "MEDIUM":
            st.warning(
                "🟡 MEDIUM RISK TRANSPORT"
            )

        elif risk_level == "LOW":
            st.success(
                "🟢 LOW RISK TRANSPORT"
            )

        # ----------------------------
        # Transport Information
        # ----------------------------

        with st.expander(
            "Transport Details",
            expanded=True
        ):
            st.json(
                data["transport"]
            )

        # ----------------------------
        # Historical Incidents
        # ----------------------------

        with st.expander(
            "Historical Incidents",
            expanded=False
        ):
            st.json(
                data["incidents"]
            )

        # ----------------------------
        # Final AI Analysis
        # ----------------------------

        st.markdown("---")

        st.markdown(
            "## AI Risk Analysis Report"
        )

        st.markdown(
            analysis
        )