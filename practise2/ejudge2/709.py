a = int(input())
num = list(map(int, input().split()))
max_num = max(num)
min_num = min(num)
for x in num:
    if x == max_num:
        print(min_num, end = ' ')
        continue
    print(x, end = ' ')