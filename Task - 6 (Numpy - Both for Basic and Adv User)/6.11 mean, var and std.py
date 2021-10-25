import numpy as np

n,m =list(map(int, input().split()))
arr = np.array([input().strip().split() for i in range(n)], dtype = int)

print (np.mean(arr, axis = 1) )
print (np.var(arr, axis = 0) )
std_o = (np.std(arr) )
print(std_o.round(12))