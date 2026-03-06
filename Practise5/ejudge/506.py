import re

text = input()

x = re.search(r'\S+@\S+\.\S+', text)

if x:
    print(x.group())
else:
    print("No email")