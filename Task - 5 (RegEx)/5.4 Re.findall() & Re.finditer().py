import re
s = input()
vowel = "[oeiua]"
con = "[BCDFGHJKLMNPQRSTVWXYZ]"
ans = re.findall(r"{con}({vowel}{{2,}})(?={con})".format(con = con, vowel = vowel), s, re.IGNORECASE)
if ans:
    print("\n".join(ans))
else:
    print(-1)