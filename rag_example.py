from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("data", glob="*.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

vectorstore = InMemoryVectorStore.from_documents(chunks, embeddings)

def search_bike_station(query):
  docs = vectorstore.similarity_search(query, k=1)
  return docs[0].page_content

