import re
n = int(input())
for i in range(n):
    s = input()
    spl = s.split()
  
    pattern = r"#[a-fA-F0-9]{3,6}"
    
    if len(spl)>1 and "{" not in spl :
        spl = re.findall(pattern, s)
        for i in spl:
            print(i)