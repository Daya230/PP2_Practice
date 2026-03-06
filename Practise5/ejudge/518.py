import re

text = input()
pattern = input()

count = len(re.findall(pattern, text))

print(count)