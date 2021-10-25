from sklearn import linear_model as lm
m,n = [int(x) for x in input().strip().split(" ")]
data = [[float(x) for x in input().strip().split(" ")] for i in range(n)]
q = int(input().strip())
inq = [[float(x) for x in input().strip().split(" ")] for i in range(q)]
x = [[data[j][i] for i in range(m)] for j in range(n)]
y = [data[j][m] for j in range(n)]
model = lm.LinearRegression()

model.fit(x,y)
a = model.intercept_
b = model.coef_
result = [a+sum([b[i] * inq[j][i] for i in  range(m)]) for j in range(q)]
for y in result:
    print(y)
