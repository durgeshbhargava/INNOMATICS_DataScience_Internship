import numpy

N, M = map(int, input().split(" "))
array = numpy.array([input().strip().split() for _ in range(N)], int)
print(array.transpose())
print(array.flatten())
