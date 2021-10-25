import numpy as np
n,m = tuple(map(int, input().split()))
arr = np.array([input().split() for i in range(n)], dtype = int)

a =  (np.min(arr, axis = 1))
print(np.max(a))