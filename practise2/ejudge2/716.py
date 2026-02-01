a = int(input())
numbers = set() 
arr = list(map(int, input().split())) 

for b in arr:
    if b not in numbers:
        print("YES")
        numbers.add(b)
    else:
        print("NO")
