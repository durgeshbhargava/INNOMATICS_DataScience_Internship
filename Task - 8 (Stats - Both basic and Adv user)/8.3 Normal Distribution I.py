import math
def dist_fun(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 20
std = 2
print(round(dist_fun(19.5, mean, std), 3))
print(round(dist_fun(22, mean, std) - dist_fun(20, mean, std), 3))