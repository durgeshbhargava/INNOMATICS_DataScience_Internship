n = 5
xy = [map(int, input().split()) for _ in range(n)]
sum_x, sum_y, sum_x2, sum_xy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y / n) - b * (sum_x / n)

print('{:.3f}'.format(a + b * 80))
