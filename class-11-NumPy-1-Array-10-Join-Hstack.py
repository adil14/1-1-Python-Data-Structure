
# Horizantal Stack
import numpy as np 
n1 = np.array([1, 2, 3])
n2 = np.array([4, 5, 6])

n3 = np.hstack((n1,n2)) 

print(n3) 
print(n3.shape)    # why shape (6,) 