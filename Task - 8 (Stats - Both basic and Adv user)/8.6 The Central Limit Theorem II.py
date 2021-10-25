import math

num_of_ticket = float(input())
num_of_student = float(input())
mu = num_of_student * float(input())
sigma = math.sqrt(num_of_student) * float(input())

print(round(0.5*(1+math.erf((num_of_ticket - mu)/(sigma * math.sqrt(2)))),4))