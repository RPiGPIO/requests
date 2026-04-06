docs = {
    1: "I love natural language processing",
    2: "language processing is interesting",
    3: "I enjoy learning language"
}

index = {}

# Build inverted index
for doc_id, text in docs.items():
    for word in text.lower().split():
        if word not in index:
            index[word] = {}
        index[word][doc_id] = index[word].get(doc_id, 0) + 1

# Display alphabetical
print("Inverted Index:")
for term in sorted(index):
    print(term, ":", index[term])

# Query
q = input("Enter term: ").lower()

if q in index:
    print("Found in:", index[q])
else:
    print("Not found")
