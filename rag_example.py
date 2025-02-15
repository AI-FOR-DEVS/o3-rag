from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_pinecone import PineconeVectorStore, Pinecone


embeddings = OpenAIEmbeddings()

def create_vectorstore():
  loader = DirectoryLoader("data", glob="*.txt")
  documents = loader.load()

  text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
  chunks = text_splitter.split_documents(documents)

  Pinecone.from_documents(chunks, embeddings, index_name="bike-berlin-demo")


def search_in_vectorstore(query):
  vectorstore = PineconeVectorStore(index_name="bike-berlin-demo", embedding=embeddings)
  docs = vectorstore.similarity_search(query, k=1)
  return docs[0].page_content