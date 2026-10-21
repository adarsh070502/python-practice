from langchain_community.document_loaders import PyPDFLoader
from nltk.tokenize import sent_tokenize
import nltk
from sentence_transformers import SentenceTransformer
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
model = SentenceTransformer('all-MiniLM-L6-v2')


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text = " ".join([doc.page_content for doc in documents])
    return text


def split_text(text, chunk_size=500):
    sentences = sent_tokenize(text)
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) <= chunk_size:
            chunk += " " + sentence
        else:
            chunks.append(chunk)
            chunk = sentence
    if chunk:
        chunks.append(chunk)
    return chunks


def create_embeddings(chunks):
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings


def save_embeddings(chunks, embeddings, filename='embeddings.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump((chunks, embeddings), f)


# Load and process the document
text = load_pdf("ELURI_ADARSH.pdf")
chunks = split_text(text)

# Generate embeddings and save
embeddings = create_embeddings(chunks)
save_embeddings(chunks, embeddings)

