
# in iris dataset sepal length petal length sepal width petal width is a continus data
# in iris dataset species is a catagorical data i.e : setosa , virginica and versicolor

from keras.datasets import iris 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns  
from sklearn import datasets


iris = datasets.load_iris() 
show_head = pd.read_csv('iris.csv')
print(iris.show_head)  