from nltk.stem import WordNetLemmatizer
#lemmatizing is like stemming but usually ends up with a real word like a synonym
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))

#a for adjective
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos = "a"))
