import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_index = [0,50,100]
#import iris dataset

for i in range(len(iris.target)):
	print ("Subject %d: label %s, features %s" % (i,iris.target[i],iris.data[i]))

train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index, axis=0)

test_target = iris.target[test_index]
test_data = iris.data[test_index]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data,train_target)
print(test_target)
print(clf.predict(test_data))