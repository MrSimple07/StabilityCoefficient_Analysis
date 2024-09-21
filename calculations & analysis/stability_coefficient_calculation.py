import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def calculate_stability_coefficient(responses):
    embeddings = model.encode(responses)
    similarities = cosine_similarity(embeddings)
    
    n = similarities.shape[0]
    stability_coefficient = (np.sum(similarities) - n) / (n * (n - 1))
    
    return stability_coefficient
