import math

dist_fun = lambda x: 0.5 * (1 + math.erf((x - mean) / std / 2 ** 0.5))
mean, std = 70, 10

print(round((1-dist_fun(80))*100,2),round((1-dist_fun(60))*100,2),round((dist_fun(60))*100,2),sep = "\n")