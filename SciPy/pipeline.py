import numpy as np
from sklearn import tree
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
Y = iris.target

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = .5)

my_classifier = tree.DecisionTreeClassifier()

my_classifier = my_classifier.fit(X_train,Y_train)

predictions = my_classifier.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))