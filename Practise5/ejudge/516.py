import re

text = input()
match = re.search(r'Name: (.+), Age: (.+)', text)

if match:
    name, age = match.groups()
    print(name, age)