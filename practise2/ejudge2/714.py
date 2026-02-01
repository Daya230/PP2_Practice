a = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num] = 1

max_freq = max(freq.values())

c = list()
for num, count in freq.items():
    if count == max_freq:
        c.append(num)
print(min(c))