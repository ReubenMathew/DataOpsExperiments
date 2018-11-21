#used to look up syn atonym def for words

from nltk.corpus import wordnet
#list
#syns = wordnet.synsets("program")

#print(syns)

#lemmatize synonym
#print(syns[0].lemmas()[0].name())

#def
#print(syns[0].definition())

#examples
#print(syns[0].examples())

#synonyms = []
#antonyms = []

#for syn in wordnet.synsets("good"):

#	for l in syn.lemmas():
#		print("l:",l)
#		synonyms.append(l.name())
#		if l.antonyms():
#			antonyms.append(l.antonyms()[0].name())
#print(set(synonyms))
#	print(set(antonyms))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
w3 = wordnet.synset("car.n.01")

#comparing similarity
print(w1.wup_similarity(w2))
print(w1.wup_similarity(w3))