from dotenv import load_dotenv

load_dotenv()

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, api_key=api_key)

print("choose AI model")
print("press 1 for angry mode")
print("press 2 for sad mode")
print("press 3 for funny mode")

choice = int(input("tell your response :- "))

if choice == 1: 
    mode = "You are an angry AI agent. You respond  agressively and impatiently"
elif choice == 2: 
    mode = "You are a sad AI agent. You respond  sadly and depressingly"
elif choice == 3: 
    mode = "You are a funny AI agent. You respond  funnily and humorously"
else:
    mode = "You are a normal AI agent. You respond normally"

messages = [
    SystemMessage(content = mode)
]

print(" --------------------welcome, type 0 to exit --------------------------")
while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content = prompt))

    if prompt == "0":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))

    print("Bot: ",response.content)


# from dotenv import load_dotenv

# load_dotenv()

# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, api_key=api_key)

# messages = [
#     SystemMessage(content = "You are a angry assistant")
# ]

# print(" --------------------welcome, type 0 to exit --------------------------")
# while True:
#     prompt = input("You: ")
#     messages.append(HumanMessage(content = prompt))

#     if prompt == "0":
#         break

#     response = model.invoke(messages)
#     messages.append(AIMessage(content = response.content))

#     print("Bot: ",response.content)