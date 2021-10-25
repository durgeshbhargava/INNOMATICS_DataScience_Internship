import re
case = int(input())
for i in range(case):
    n = input()
    valid = re.match(r"[789]\d{9}$", n)
    if valid:
        print('YES')
    else:
        print('NO')
        