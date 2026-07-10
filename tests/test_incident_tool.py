from app.tools.incident_tool import (
    get_related_incidents_tool
)

result = (
    get_related_incidents_tool(
        [
            "ZCL_PRICING_ENGINE",
            "ZI_CUSTOMER_PRICING"
        ]
    )
)

print(result)