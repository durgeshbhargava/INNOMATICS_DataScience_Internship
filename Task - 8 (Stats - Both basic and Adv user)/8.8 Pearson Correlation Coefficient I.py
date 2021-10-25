n = int(input())
a = list(map(float,input().strip().split()))
b = list(map(float,input().strip().split()))
mu_x, mu_y= sum(a) / n, sum(b) / n
 

std_a = (sum([pow((i - mu_x),2) for i in a]) / n)**0.5
std_b = (sum([pow((i - mu_y),2) for i in b]) / n)**0.5


covariance = sum([(a[i] - mu_x) * (b[i] -mu_y) for i in range(n)])

correlation_coefficient = covariance / (n * std_a * std_b)

print(round(correlation_coefficient,3))