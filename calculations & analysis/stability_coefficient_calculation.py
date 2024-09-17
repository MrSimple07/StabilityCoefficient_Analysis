
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_stability(responses, baseline):
    N = len(responses)
    similarities = [cosine_similarity([r], [baseline])[0][0] for r in responses]
    stability_coefficient = np.mean(similarities)
    return stability_coefficient

# Example usage:
# responses = [response_1, response_2, ..., response_N]
# baseline = baseline_response
# stability = calculate_stability(responses, baseline)
