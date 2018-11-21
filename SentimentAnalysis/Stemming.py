from nltk import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
	print(ps.stem(w))

new_text = "It is very important to be python while you are pythoning with python. All pythonders have pythoned at least once"

words = word_tokenize(new_text)

for w in words:
	print(ps.stem(w))