import numpy
arr  = list(map(int, input().split(' ')))
my_array = numpy.array([arr])
my_array.shape = (3, 3)
print(my_array)