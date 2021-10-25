import numpy
n,m  = tuple(map(int, input().split()))
a = numpy.array([input().split() for i in range(n)], dtype = int)
b= numpy.array([input().split() for i in range(n)],dtype=int)


print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)

print(a**b)