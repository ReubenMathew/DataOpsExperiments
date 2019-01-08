from sklearn import tree
features = [[140,1],[130,1],[150,0],[170,0],[180,0]]
# 1 is smooth 0 is bumpy
labels = [0,0,1,1,1]
# 1 is orange 0 is apple

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[160,0]]))