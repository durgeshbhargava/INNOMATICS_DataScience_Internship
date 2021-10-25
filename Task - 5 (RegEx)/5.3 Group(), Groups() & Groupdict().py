import re
n = input()
pattern = r"([a-z A-Z 0-9])\1"
mat = re.search(pattern, n)
if mat:
    print(mat.groups()[0])

else:
    print(-1)
