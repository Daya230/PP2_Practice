import re

text = input()

seq = re.findall(r'\d{2,}', text)

print(' '.join(seq))