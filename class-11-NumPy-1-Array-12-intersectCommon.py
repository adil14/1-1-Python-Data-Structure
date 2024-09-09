import numpy as np 
n1 = np.array([10, 20, 30, 40, 50, 60])
n2 = np.array([50, 60, 70, 80, 90])

n3 = np.intersect1d(n1,n2)

print(n3) 