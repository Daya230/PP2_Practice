a = int(input())
surnames = list()
counter =0
for i in range(a):
    b = input()
    surnames.append(b)
uniq = set(surnames)
print(len(uniq))