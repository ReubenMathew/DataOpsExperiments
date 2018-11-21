import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

#use top 3000 words
word_features = list(all_words.keys())[:3000]

def find_features(document):
	#set makes 1 of each word rather than multiple instances
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words) #will be true of false if document contains word
	return features
	
print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev,category) in documents]