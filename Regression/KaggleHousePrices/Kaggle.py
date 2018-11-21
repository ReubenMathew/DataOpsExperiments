import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv("train.csv")

test = pd.read_csv("test.csv")

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10,6)

#target = np.log(train.SalePrice)

numeric_features = train.select_dtypes(include=[np.number])

corr = numeric_features.corr()

# top correlating values to Sale Price
print(corr['SalePrice'].sort_values(ascending=False)[:7],'\n')

train = train[train['GarageArea'] < 1200]

target = np.log(train.SalePrice)

nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'

print(nulls)

categoricals = train.select_dtypes(exclude = [np.number])

print(categoricals.describe())

print(train.Street.value_counts(),"\n")

train['enc_street'] = pd.get_dummies(train.Street, drop_first=True)
test['enc_street'] = pd.get_dummies(test.Street, drop_first=True)

print(train.enc_street.value_counts(),"\n")

def encode(x): return 1 if x == 'Partial' else 0

train['enc_condition'] = train.SaleCondition.apply(encode)
test['enc_condition'] = test.SaleCondition.apply(encode)

data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

y = np.log(train.SalePrice)
X = data.drop(['SalePrice','Id'],axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)

lr = linear_model.LinearRegression()
model = lr.fit(X_train,y_train)

submission = pd.DataFrame()
submission['Id'] = test.Id

feats = test.select_dtypes(include=[np.number]).drop(['Id'], axis = 1).interpolate()

predictions = model.predict(feats)

final_predictions = np.exp(predictions)

submission['SalePrice'] =  final_predictions

print(submission.head())

#submission.to_csv('submissionKNN.csv',index = False)


'''
#sale condition pivot table
condition_pivot = train.pivot_table(index = 'enc_condition',
	values = 'SalePrice', aggfunc=np.median)
condition_pivot.plot(kind='bar',color='blue')
plt.xlabel('Encoded Sale Condition')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)
plt.show()
'''


'''
plt.scatter(x=train['GarageArea'], y=target)
plt.ylabel('SalePrice')
plt.xlabel('GarageArea')
plt.show()
'''
