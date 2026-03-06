import re

s = input()

x = re.match(r"Hello",s)

print("Yes" if x else "No")