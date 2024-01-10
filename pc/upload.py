import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Housekeeping
logging.info("Housekeeping...")
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from typing import Union
import os
import pinecone
import secret as secret

# Set up OpenAI shenanigans
logging.info("Setting up OpenAI...")
openai_embeddings = OpenAIEmbeddings(openai_api_key=secret.OPENAI_API_KEY)

# Set up Pinecone shenanigans
logging.info("Setting up Pinecone...")
pinecone.init(
    api_key=secret.PINECONE_API_KEY,
    environment=secret.PINECONE_ENV
)

# CONSTANTS
INDEX_NAME = "reductions-ai-db"

def load_pdf(filepath: str) -> Union[list[Document], None]:
    """Tries to load the PDF as a lang chain document, returning None if it doesn't exist"""
    try:
        loader = PyPDFLoader(filepath)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        return texts
    except FileNotFoundError:
        logging.error(f"Something went wrong when loading the PDF at {filepath}")
        return None

def upload_file(vss: Pinecone, filepath: str):
    """Loads the PDF and uploads it to the index"""
    logging.info(f"Uploading {filepath} to {INDEX_NAME}...")
    texts = load_pdf(filepath)
    if texts is None:
        logging.error(f"Could not load PDF at {filepath}")
        return
    vss.add_documents(texts)

def upload_folder(folder: str):
    """Loads all PDFs in the folder and uploads them to the index"""
    index = pinecone.Index(INDEX_NAME)
    vss = Pinecone(index, openai_embeddings, "texts")
    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder, filename)
            upload_file(vss, filepath)

def main():
    upload_folder("../source_docs")

if __name__ == "__main__":
    main()
