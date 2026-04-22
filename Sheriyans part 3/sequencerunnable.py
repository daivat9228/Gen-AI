from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
model = ChatMistralAI(model="mistral-small-2506")

# 3. Output Parser
parser = StrOutputParser()

# step-by-setp manual flow

# # format the prompt
# formatted_prompt = prompt.format_messages(topic = "machine learning")

# #call the model manually
# response = model.invoke(formatted_prompt)

# #parse the output manually
# final_output = parser.parse(response.content)
# print(final_output)

# now using LCEL

chain = prompt | model | parser

final_output = chain.invoke({"topic": "machine learning"})
print(final_output)