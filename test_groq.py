from app.llm.groq_client import llm

response = llm.invoke(

    "Who are you?"

)

print(response.content)