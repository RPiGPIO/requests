from collections import defaultdict
import string

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.split()

def build_inverted_index(documents):
    index = defaultdict(set)

    for doc_id, text in documents.items():
        words = preprocess(text)

        for word in words:
            index[word].add(doc_id)

    return index

def search(index, query):
    terms = preprocess(query)
    result = None

    for term in terms:
        if term in index:
            if result is None:
                result = index[term]
            else:
                result = result.intersection(index[term])
        else:
            return set()

    return result if result else set()


documents = {
    1: "Information retrieval is important",
    2: "Search engines use retrieval",
    3: "Deep learning improves search",
    4: "Information retrieval uses indexing"
}

# Build index
index = build_inverted_index(documents)

# Display index alphabetically
print("Inverted Index:")
for term in sorted(index):
    print(term, "->", sorted(index[term]))

# Unique terms
print("\nTotal unique indexed terms:", len(index))

# Query retrieval
query = input("\nEnter query: ")
result = search(index, query)

print("Matching documents:", sorted(result))
