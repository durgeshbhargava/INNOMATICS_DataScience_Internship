import re
n = int(input())
patern = r"^[+-.]?[0-9]*\.[0-9]+$"
"""^ use for start with
[] for set of 
? for zero and one occurrance
* for one or more occurrance 
\ for special character 
+ use for match
$ use for end with"""

for i in range(n):
    value = input()
    print(bool(re.match(patern, value)))