#nltk.download("punkt_tab")
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

text = "This is a sample sentence showing stopword removal"

stop_words = set(stopwords.words("english"))

tokens = word_tokenize(text.lower())

filtered = [word for word in tokens if word not in stop_words]

print("Original:", tokens)
print("Filtered:", filtered)
