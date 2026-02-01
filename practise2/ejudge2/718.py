a = int(input())
arr = list()
for i in range(a):
    b = input()
    arr.append(b)
uniq_arr = sorted(set(arr))
for x in uniq_arr:
    print(x, arr.index(x)+1)
