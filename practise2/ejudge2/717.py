a = int(input())
all_numbers = list()
counter = 0
for i in range(a):
    b = input()
    all_numbers.append(b)
tel = set(all_numbers)
for x in tel:
    if all_numbers.count(x) == 3:
        counter +=1
print(counter)