from app.models.llm import llm

response = llm.invoke(
    "What is SAP ABAP?"
)

print(
    response.content
)