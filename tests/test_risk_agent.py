from agents.transport_agent import (
    TransportAgent
)

from agents.risk_analysis_agent import (
    RiskAnalysisAgent
)

data = (
    TransportAgent.analyze_transport(
        "DEVK900451"
    )
)

analysis = (
    RiskAnalysisAgent.analyze(
        data["transport"],
        data["incidents"]
    )
)

print(analysis)