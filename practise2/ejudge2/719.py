n = int(input())
ep = {}

for i in range(n):
    s, k = input().split()
    k = int(k)
    if s in ep:
        ep[s] += k
    else:
        ep[s] = k

for d in sorted(ep):
    print(d, ep[d])
