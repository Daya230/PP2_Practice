import re

text = input()      
x = input()   

parts = re.split(x, text)  
print(','.join(parts))           