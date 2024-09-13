import numpy as np 
n_one = np.array([10, 20, 30, 40, 50, 60])
n_one = np.save('my_numpy_practice_one', n_one) 


n_two = np.load('my_numpy_practice_one.npy') 
print(n_two) 