
# in iris dataset sepal length petal length sepal width petal width is a continus data
# in iris dataset species is a catagorical data i.e : setosa , virginica and versicolor


import pandas as pd 
iris = pd.read_csv('iris.csv')
iris.drop[(1,2,3), axis=0] # axis 1 means columns and axis 0 means rows   
print(iris) 