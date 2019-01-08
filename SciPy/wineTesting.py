import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.externals import joblib
from sklearn import tree
from sklearn import datasets

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
data = pd.read_csv(dataset_url, delimiter=';', encoding="utf-8-sig")
data.columns = data.columns.str.strip()

y = data.quality
x = data.drop('quality',1)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=529, stratify=y)

scaler = preprocessing.StandardScaler().fit(X_train)

X_train_scaled = scaler.transform(X_train)

pipeline = make_pipeline(preprocessing.StandardScaler(), RandomForestRegressor(n_estimators=100))

hyperparameters = { 'randomforestregressor__max_features' : ['auto', 'sqrt', 'log2'],
                  'randomforestregressor__max_depth': [None, 5, 3, 1]}

clf = tree.DecisionTreeClassifier()
 

clf.fit(X_train, Y_train)

pred = clf.predict(X_test)

print(accuracy_score(Y_test, pred))
 

joblib.dump(clf, 'rf_regressor.pkl')
