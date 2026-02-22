def Power(n):
    for i in range(n+1):
        yield 2**i

n = int(input())
for x in Power(n):
    print(x, end = ' ')