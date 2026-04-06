plays = {
    "Antony and Cleopatra": "Antony Brutus Caesar Cleopatra mercy worser",
    "Julius Caesar": "Antony Brutus Caesar Calpurnia",
    "The Tempest": "mercy worser",
    "Hamlet": "Caesar Brutus mercy worser",
    "Othello": "Caesar mercy worser",
    "Macbeth": "Antony Caesar mercy"
}

words = ["Antony", "Brutus", "Caesar", "Calpurnia", "Cleopatra", "mercy", "worser"]

# Create incidence matrix
matrix = [[0 for _ in range(len(plays))] for _ in range(len(words))]
texts = list(plays.values())

for i in range(len(words)):
    for j in range(len(texts)):
        if words[i].lower() in texts[j].lower():
            matrix[i][j] = 1

# Convert row bits to integer
vector = {}
for i in range(len(words)):
    bits = "".join(str(x) for x in matrix[i])
    vector[words[i]] = int(bits, 2)

print("Word vectors:", vector)

query = input("Enter Boolean Query: ")

for w in sorted(words, key=len, reverse=True):
    query = query.replace(w, str(vector[w]))

query = query.replace("AND", "&")
query = query.replace("OR", "|")
query = query.replace("NOT", "~")

result = eval(query)
ans = bin(result).replace("0b", "").zfill(len(plays))

print("Matching plays:")
play_names = list(plays.keys())
for i in range(len(ans)):
    if ans[i] == "1":
        print(play_names[i])
