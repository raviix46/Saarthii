import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer, util
import os

# Paths
dataset_path = "data/lawbot/Final_Dataset.pkl"
embedding_path = "embeddings/lawbot/qa_embeddings.pkl"

# Load dataset
df = pd.read_pickle(dataset_path)

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load embeddings
if os.path.exists(embedding_path):
    with open(embedding_path, "rb") as f:
        qa_embeddings = pickle.load(f)
else:
    raise FileNotFoundError(f"❌ Embeddings not found at: {embedding_path}")

def get_best_match(query):
    query_embedding = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, qa_embeddings)[0]
    best_match_idx = scores.argmax().item()
    return df.iloc[best_match_idx]['response']