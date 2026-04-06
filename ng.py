def ngrams(text,n):
    text=text.lower().split()
    return [tuple(text[i:i+n]) for i in range(len(text)-n+1)]

def jaccard(a,b):
    a,b= set(a), set(b)
    return len(a&b)/len(a|b)

s1= input("Enter Text 1")
s2= input("Enter Text 2")

b1= ngrams(s1,2)
b2= ngrams(s2,2)

print("Bigram 1:",b1)
print("Bigrams 2:",b2)

print("Jaccard:",jaccard(b1,b2))


