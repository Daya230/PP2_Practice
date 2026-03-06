import re

a = input()
x = re.findall(r"\d",a)
y = " ".join(x)
print(y)