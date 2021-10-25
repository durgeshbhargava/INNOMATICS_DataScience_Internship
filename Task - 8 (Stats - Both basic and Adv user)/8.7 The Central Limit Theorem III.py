mu, sigma = 500, 80
muS, sigmaS = mu, sigma/(100**(1/2))

a = mu - (1.96*sigmaS)
b = mu + (1.96*sigmaS)

print(round(a,2), round(b,2), sep = "\n")
