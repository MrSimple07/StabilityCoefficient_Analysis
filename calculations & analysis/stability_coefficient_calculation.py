import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Function to calculate stability coefficient
def calculate_stability_coefficient(responses):
    embeddings = model.encode(responses)
    
    # Compute cosine similarity matrix between embeddings
    similarities = cosine_similarity(embeddings)
    
    # Calculate the stability coefficient
    n = similarities.shape[0]
    stability_coefficient = (np.sum(similarities) - n) / (n * (n - 1))
    
    return stability_coefficient

# Example
responses = [
    "The forest is cut down, causing global warming.",
    "Deforestation leads to climate change.",
    "Cutting down trees contributes to global warming.",
    "Deforestation increases the risk of global warming.",
    "Trees being cut down can cause an increase in temperature."
]

stability_coefficient = calculate_stability_coefficient(responses)
print(f"Stability Coefficient: {stability_coefficient:.4f}")
