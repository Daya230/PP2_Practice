
n_commands = int(input())

g, n = 0, 0

for _ in range(n_commands):
    line = input().split()
    if not line: continue
    
    scope = line[0]
    value = int(line[1])
    
    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
print(g, n)