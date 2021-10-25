import numpy
n,m= tuple(map(int, input().split(' ')))

output = str(numpy.eye(n, m))
print(output.replace('0',' 0').replace('1' , ' 1'))
