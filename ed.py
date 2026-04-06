# ==========================================
# EDIT DISTANCE 1: RECURSIVE EDIT DISTANCE
# ==========================================

def recursive_edit_distance(str1, str2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return recursive_edit_distance(str1, str2, m - 1, n - 1)

    return 1 + min(
        recursive_edit_distance(str1, str2, m, n - 1),
        recursive_edit_distance(str1, str2, m - 1, n),
        recursive_edit_distance(str1, str2, m - 1, n - 1)
    )


# Example
print("Recursive:", recursive_edit_distance("cat", "cut", 3, 3))


# ==========================================
# EDIT DISTANCE 2: DYNAMIC PROGRAMMING
# ==========================================

import numpy as np


def dynamic_edit_distance(s1, s2):
    rows = len(s1) + 1
    cols = len(s2) + 1

    matrix = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    print("Dynamic Matrix:\n", matrix)
    return matrix[rows - 1][cols - 1]


# Example
print("Dynamic:", dynamic_edit_distance("cat", "cut"))


# ==========================================
# EDIT DISTANCE 3: WEIGHTED / LEVENSHTEIN
# ==========================================


def weighted_edit_distance(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1

    matrix = np.zeros((size_x, size_y), dtype=int)

    for x in range(size_x):
        matrix[x][0] = x
    for y in range(size_y):
        matrix[0][y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1],
                    matrix[x][y - 1] + 1
                )
            else:
                matrix[x][y] = min(
                    matrix[x - 1][y] + 1,
                    matrix[x - 1][y - 1] + 1,
                    matrix[x][y - 1] + 1
                )

    print("Weighted Matrix:\n", matrix)
    return matrix[size_x - 1][size_y - 1]


# Example
print("Weighted:", weighted_edit_distance("cat", "dog"))


# ==========================================
# EDIT DISTANCE 4: WORD LEVEL EDIT DISTANCE
# ==========================================


def word_edit_distance(sent1, sent2):
    words1 = sent1.split()
    words2 = sent2.split()

    rows = len(words1) + 1
    cols = len(words2) + 1

    matrix = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            if words1[i - 1] == words2[j - 1]:
                cost = 0
            else:
                cost = 1

            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            )

    print("Word Matrix:\n", matrix)
    return matrix[rows - 1][cols - 1]


# Example
print("Word Level:", word_edit_distance(
    "I love natural language processing",
    "I enjoy learning language processing"
))
