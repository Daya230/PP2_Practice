def Rep(s,n):
    for _ in range(n):
        for i in s:
            yield i


s = input().split()
b = int(input())

for x in Rep(s,b):
    print(x, end= ' ')
