from secret import OPENAI_API_KEY, PINECONE_API_KEY
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["PINECONE_ENV"] = "gcp-starter"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
                                  

def populate_pinecone():
  loader = DirectoryLoader('../sources/', glob="*.pdf", loader_cls=PyPDFLoader)
  docs = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
  texts = text_splitter.split_documents(docs)
  embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
  pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENV"]
  )
  index_name = "reductions-ai-db"
  docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)

populate_pinecone()