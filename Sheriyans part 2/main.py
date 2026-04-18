from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

model = ChatMistralAI(model_name="mistral-small-2506")

data = TextLoader(r"g:\AI\Sheriyans part 2\document loader\test.txt")  
doc = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{data}"),
])

prompt = template.format_messages(data = doc[0].page_content)

response = model.invoke(prompt)
print(response.content)



# load_dotenv() : jenahi .env file avi gai
# data ma text file nopath apyo
# doc = data.load() : text file ne doc banavi load kari 
# doc[0].page_content : text file ni content avi gai
# data ne ChatPromptTemplate ma pass kari 
# prompt = template.format_messages(data = doc[0].page_content) : prompt ma text file ni content pass kari 
# ChatPromptTemplate ma system and user role add karya
# system role ma assistant ni content pass kari 
# user role ma text file ni content pass kari 

# prompt ma text file ni content pass kari 
# model ma prompt pass kari 
# response ma model ni content pass kari 
# print ma model ni content pass kari 