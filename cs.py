import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

def process(text):
    tokens = word_tokenize(text.lower())

    # Stopword removal
    stop_words = set(stopwords.words("english"))
    filtered = [w for w in tokens if w.isalpha() and w not in stop_words]

    # Term frequency
    freq = {}
    for word in filtered:
        freq[word] = freq.get(word, 0) + 1

    return freq

def cosine_similarity(dict1, dict2):
    all_words = list(set(dict1.keys()) | set(dict2.keys()))

    v1 = np.array([dict1.get(word, 0) for word in all_words])
    v2 = np.array([dict2.get(word, 0) for word in all_words])

    dot = np.dot(v1, v2)
    mag1 = np.linalg.norm(v1)
    mag2 = np.linalg.norm(v2)

    return dot / (mag1 * mag2)

text1 = "Shipment of gold damaged in a fire"
text2 = "Delivery of silver arrived in a silver truck"

d1 = process(text1)
d2 = process(text2)

score = cosine_similarity(d1, d2)
print("Similarity =", round(score, 4))
