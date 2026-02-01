a = int(input())
while a >1:
    if a%2==0:
        a/=2
        continue
    else:
        print("NO")
        break
else:
    print("YES")