# Stability Coefficient Analysis

## Project Overview
This project aims to evaluate and compare the stability of four models: **Vikhr**, **TinyLlama**, **Llama2**, and **Mistral**, across four distinct tasks: **CheGeka**, **LCS**, **RutEdox**, and **ruOpenBookQA**. 
The stability of each model is quantified using the **Stability Coefficient**, calculated based on cosine similarity between generated responses to various prompt variations.

## Goal
- **Analyze** how model responses change when prompts are slightly varied.
- **Identify** error-prone areas and factors that might strongly influence the model's responses, especially those factors that ideally should not.
- **Compute** a single stability score for each model-task combination.

## Formula for Stability Coefficient

## Stability Coefficient Formula

The Stability Coefficient is calculated using the cosine similarities between embeddings of responses. The formula for the Stability Coefficient is:

$$
\text{Stability Coefficient} = \left( \frac{\sum_{i \neq j} \text{similarity}_{ij} - n}{n \cdot (n - 1)} \right) \cdot P
$$

where:

- \(\text{similarity}_{ij}\) is the cosine similarity between the embeddings of response \(R_i\) and response \(R_j\).
- \(n\) is the number of prompt variations for each question (in this case, 10).
- The denominator \(n \cdot (n - 1)\) represents the number of unique pairs of responses.
- The condition \(i \neq j\) ensures that a response is not compared with itself.
- \(P\) is the answer probability calculated from the token probabilities in the response.

### Explanation

1. **Cosine Similarity Calculation**: The sum of cosine similarities is computed for all unique pairs of responses, ensuring that a response is not compared to itself.

2. **Normalization**: The numerator is normalized by the number of unique pairs \(n \cdot (n - 1)\).

3. **Incorporating Answer Probability**: The result is then multiplied by the probability \(P\) of the answer, which represents the likelihood of the response being correct based on the token probabilities.

  
### Process

1. **For each question:**
   - Take the 10 different prompts and their corresponding model responses.
   - Calculate the Stability Coefficient for this question using the formula above.

2. **Calculate the overall Stability Coefficient:**
   - Compute the mean of all question-specific Stability Coefficients to get the overall Stability Coefficient for the model.

3. **Repeat this process for each model being evaluated.**

   

# Embedding Model
We use the paraphrase-MiniLM-L6-v2 model from the Sentence-Transformers library for generating embeddings. This model is designed to create sentence embeddings that can be compared using cosine similarity.

Key features of this embedding model:
- It's a lightweight model (80MB) that produces 384 dimensional embeddings.
- It's trained on a large and diverse dataset of over 1 billion training pairs.
- It performs well on various semantic textual similarity tasks.

# Models
The project evaluates four different models:

1. Vikhr: A high-performance model tuned for general-purpose tasks.
2. TinyLlama: A lightweight version of Llama, optimized for speed and efficiency.
3. Llama3.2: A successor of Llama, focusing on improved accuracy.
4. Mistral: A model known for its interpretability and token-level precision.
   
Each model's response to prompt variations across the four tasks is analyzed in detail.

# Dataset Information
Each task in the project involves evaluating different models across four datasets:

- **CheGeka**: The task contains questions from the game “What? Where? When?" and is a question-and-answer task with a free answer.
- **LCS**: The longest common subsequence is an algorithmic task from BIG-Bench. This problem consists of pairs of strings as input, and language models are expected to predict the length of the longest common subsequence between them correctly.
- **RutEdox**: Russian Detoxification Diagnostic (ruDetox) is a parallel text detoxification corpus based on the RuSSE-Detox competition. Text detoxification is the task of text style transfer - changing the style of the text while maintaining the original meaning and fluency. 
- **ruOpenBookQA**: RuOpenBookQA is a QA dataset with multiple-choice elementary-level science questions, which probe understanding of 1k+ core science facts.

The datasets are preprocessed to create prompt variations for each question.


# Results & Conclusions
The results of the Stability Coefficient calculations can be found in the docs file. Key insights include:

- Which models showed the highest stability for each task.
- Factors that had the greatest influence on model stability.
- Recommendations for further improvements and experiments.

# References
- Sentence-Transformers: https://www.sbert.net/
- MERA Benchmark: https://mera.a-ai.ru
- Stability in NLP Models: Research papers and articles that delve deeper into understanding model stability across tasks.



# Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or find bugs.

# License
This project is licensed under the Apache 2.0 License. See the LICENSE file for details.
