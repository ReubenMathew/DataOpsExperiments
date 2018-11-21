import pandas as pd
import matplotlib.pyplot as plt

reviews = pd.read_csv("winemag-data_first150k.csv")

reviews[reviews['price'] < 100].sample(100).plot.scatter(x='price', y='points')
reviews[reviews['price'] < 100].sample(100).plot.hexbin(x='price', y='points', gridsize=15)

plt.show()
sns.kdeplot(reviews[reviews['price'] < 200].loc[:, ['price', 'points']].dropna().sample(5000))
