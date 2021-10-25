import numpy as np

n,m = tuple(map(int, input().split()))
arr = np.array([input().split() for i in range(n)], dtype = int)
arr1 = np.sum(arr, axis = 0) 
print (np.prod(arr1) )
