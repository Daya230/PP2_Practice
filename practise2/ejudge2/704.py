a = int(input())
numbers = list(map(int, input().split()))
sum = 0 
for b in numbers:
    if b > 0:
        sum+=1
print(sum)