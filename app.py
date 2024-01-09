import pandas as pd
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Nombre del modelo
modelo = "phi"

# Ubicación del CSV
csv_filepath = './data/listings.csv'

# Cargar el CSV
df = pd.read_csv(csv_filepath)
loader = CSVLoader(csv_filepath, source_column="id")
data = loader.load()

# Crear el vectorstore
embedding_model = OllamaEmbeddings(model=modelo)
db = Chroma.from_documents(data, embedding_model, persist_directory="./chroma_db")

# Crear el retriever
retriever_tool = db.as_retriever()