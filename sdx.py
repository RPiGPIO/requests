def soundex(word):
    codes = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2",
        "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6"
    }

    word = word.upper()
    first_letter = word[0]

    result = first_letter
    prev_code = codes.get(first_letter, "")

    for ch in word[1:]:
        code = codes.get(ch, "")
        if code != prev_code and code != "":
            result += code
        prev_code = code

    result = result[:4].ljust(4, "0")
    return result


words = ["Robert", "Rupert", "Ruia", "Herman", "Hermann"]

for w in words:
    print(w, "->", soundex(w))
