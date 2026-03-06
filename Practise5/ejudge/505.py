import re

a = input()  
x = re.match(r'^[A-Za-z].*[0-9]$', a)
print('Yes' if x else 'No')