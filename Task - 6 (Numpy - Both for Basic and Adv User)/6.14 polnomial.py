import numpy as np
n = list(map(float,input().split()))
m = int(input())
print(np.polyval(n, m))
