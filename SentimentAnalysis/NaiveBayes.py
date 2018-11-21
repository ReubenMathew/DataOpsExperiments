import nltk
import random
from nltk.corpus import movie_reviews
import pickle

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

featuresets = [(find_features(rev), category) for (rev,category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

#posterior = prio occurences x likelihood / evidence  ----> likelihood 

classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo accuracy percentage:",(nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)

#wb = write in bytes
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier,save_classifier)
save_classifier.close()

