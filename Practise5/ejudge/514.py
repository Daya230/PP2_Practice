import re

text = input()

pattern = re.compile(r'^\d+$') 

print("Match" if pattern.match(text) else "No match")
