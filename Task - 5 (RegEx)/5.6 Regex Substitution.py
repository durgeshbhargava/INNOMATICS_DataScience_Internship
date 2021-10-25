import re
pattern = re.compile(r"(?<= )(&&|\|\|)(?= )")
replace = lambda n: "and" if n.group()=="&&" else "or" 
for i in range(int(input())):
    string  = input()
    print(re.sub(pattern, replace, string))