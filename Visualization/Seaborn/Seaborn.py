import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

reviews = pd.read_csv("winemag-data_first150k.csv")

#sns.countplot(reviews['points'])
#sns.kdeplot(reviews.query('price < 200').price)
#reviews[reviews['price'] < 200]['price'].value_counts().sort_index().plot.line()
sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))

plt.show()
