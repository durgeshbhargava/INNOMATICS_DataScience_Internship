import re
n = int(input())
for _ in range(n):
    p = input()
    name, email = p.split(" ")
    pattern = "<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern,email)):
        print(name, email)
    