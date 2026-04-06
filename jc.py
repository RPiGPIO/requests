import re

# ==========================================
# N-GRAM GENERATION
# ==========================================
def generate_ngrams(text, n):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    words = text.split()

    ngrams = list(zip(*[words[i:] for i in range(n)]))
    return ngrams


# ==========================================
# JACCARD COEFFICIENT USING N-GRAMS
# ==========================================
def jaccard_similarity(text1, text2, n):
    grams1 = set(generate_ngrams(text1, n))
    grams2 = set(generate_ngrams(text2, n))

    intersection = grams1.intersection(grams2)
    union = grams1.union(grams2)

    score = len(intersection) / len(union)

    return intersection, union, score


# ==========================================
# MAIN
# ==========================================
s1 = "The quick brown fox"
s2 = "The quick brown dog"

n = 2   # Bigram

print("Sentence 1:", s1)
print("Sentence 2:", s2)

print("\nN-grams of Sentence 1:")
print(generate_ngrams(s1, n))

print("\nN-grams of Sentence 2:")
print(generate_ngrams(s2, n))

inter, uni, score = jaccard_similarity(s1, s2, n)

print("\nIntersection:", inter)
print("Union:", uni)
print("Jaccard Similarity =", round(score, 4))
