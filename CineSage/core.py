from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

import os
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506", api_key = os.getenv("MISTRAL_API_KEY"))
prompt = ChatPromptTemplate.from_messages([("system",
"""
You are an intelligent information extraction assistant.

Your task is to analyze the given text and extract key information in a clean, structured, human-readable format.

### Instructions:
- Extract only relevant and factual information from the text.
- Do NOT invent or assume missing details.
- Keep answers concise and clear.
- If any information is not available, write "Not specified".
- Maintain consistent formatting.

### Output Format:

Title: 
Type: 
Genre: 
Release Year: 
Director: 
Cast: 
Setting: 
Plot Summary: 
Themes: 
Notable Features: 
Ratings: 
Verdict: 

Short Summary:
(Write a 2–3 sentence simplified summary of the text)

### Input Text:
{input_text}

### Output:
Return the result exactly in the above format. Do not add extra commentary.
"""
),
("user",
"""
Extract the information from the following text:
{input_text}
"""
)
])

para =  input("enter the paragraph: ")

final_prompt = prompt.invoke(

    {"input_text" : para}

)


response = model.invoke(final_prompt)

print(response.content)