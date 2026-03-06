import re

a = input()
b = input()

x = re.search(b, a)

print("Yes" if x else "No")