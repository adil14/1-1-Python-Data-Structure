import numpy as np 
n1 = np.array([[1, 2 , 3 , 4] , [5, 6 , 7 , 8]]) 
print(n1.shape) 

n1.shape = (4 , 2) 
print(n1.shape) 


 
n3 = np.array([[1, 2 , 3] , [4, 5 , 6]])
print(n3) 
print(n3.shape) 

n3.shape = (3 , 2)
print(n3) 
print(n3.shape) 