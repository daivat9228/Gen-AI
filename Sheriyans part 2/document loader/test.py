from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"g:\AI\Sheriyans part 2\document loader\test.txt")
documents = loader.load()
# print(documents)

print(documents[0])
# print(documents[0].page_content)
# print(documents[0].metadata)