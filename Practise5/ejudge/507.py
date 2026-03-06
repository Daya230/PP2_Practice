import re

text = input()      
y = input()     
x = input() 

result = re.sub(y, x, text)

print(result)