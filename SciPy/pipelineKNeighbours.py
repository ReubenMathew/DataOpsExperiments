from scipy.spatial import distance

def euc(a,b):
	return distance.euclidean(a,b)

class ScrappyKNN():
	def predict(self,X_test):
		predictions = []
		for row in X_test:
			label = self.closest(row)
			predictions.append(label)
		return predictions
	def fit(self,X_train,Y_train):
		self.X_train = X_train
		self.Y_train = Y_train
	def closest(self,row):
		best_dist = euc(row,self.X_train[0])
		best_index = 0
		for i in range(1,len(self.X_train)):
			dist = euc(row,self.X_train[i])
			if dist < best_dist:
				best_dist = dist
				best_index = i
		return self.Y_train[best_index]
	
import numpy as np

from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
Y = iris.target


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

my_classifier.fit(X_train,Y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))