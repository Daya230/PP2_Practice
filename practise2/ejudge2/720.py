import sys

a = {}
data = sys.stdin.read().splitlines()

n = int(data[0])
idx = 1

for _ in range(n):
    b = data[idx].split()
    idx += 1

    if b[0] == "set":
        a[b[1]] = b[2]
    else:  # get
        print(a.get(b[1], f"KE: no key {b[1]} found in the document"))