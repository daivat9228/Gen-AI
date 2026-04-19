from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter

data = TextLoader(r"g:\AI\Sheriyans part 2\text splitter\note.txt")
docs = data.load()

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=5,
    chunk_overlap=1
)

chunks = splitter.split_documents(docs)

print(chunks[0].page_content)

for i in chunks:
    print(i.page_content)
    print()