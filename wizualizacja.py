import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions

import os
from dotenv import load_dotenv
load_dotenv()

def knn_comparison(data, k):
    x = data[['X','Y']].values
    y = data['class'].astype(int).values
    clf = neighbors.KNeighborsClassifier(n_neighbors=k)
    clf.fit(x, y)# Plotting decision region
    plot_decision_regions(x, y, clf=clf, legend=2)# Adding axes annotations
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Knn with K='+ str(k))
    plt.show()


iris = os.getenv("IRIS")
df = pd.read_csv(iris, sep=',')

attributes = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df.columns = attributes
print(df.head())

# data1 = pd.read_csv(iris)
# for i in [1,5,20,30,40,80]:
#     knn_comparison(data1, i)
#
