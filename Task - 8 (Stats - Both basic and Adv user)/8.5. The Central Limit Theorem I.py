import math
w = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

musum= n * mu
sigmasum = math.sqrt(n) * sigma

def dist_fun(w, mu, sigma):
    Z = (w - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(dist_fun(w, musum, sigmasum), 4))