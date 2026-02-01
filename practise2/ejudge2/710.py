a = int(input())
num = list(map(int, input().split()))
num.sort(reverse = True)
for x in num:
    print(x, end = ' ')