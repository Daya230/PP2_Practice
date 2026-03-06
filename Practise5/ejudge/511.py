import re

text = input()

up = re.findall(r'[A-Z]', text)

print(len(up))