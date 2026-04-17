from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature = 0.7, max_tokens = 90)

response = model.invoke("write me one math problem with solution")

print(response.content)