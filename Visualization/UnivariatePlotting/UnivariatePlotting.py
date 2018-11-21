import pandas as pd
import matplotlib.pyplot as plt
reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

#(reviews['province'].value_counts().head(10)/len(reviews)).plot.bar()
'''
reviews['points'].value_counts().sort_index().plot.bar()
reviews['points'].value_counts().sort_index().plot.line()
reviews['points'].value_counts().sort_index().plot.area()
'''
#reviews[reviews['price'] < 200]['price'].plot.hist()

print(reviews[reviews['price'] > 1500].head(4))

plt.show()
