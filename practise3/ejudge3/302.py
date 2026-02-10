def isUsual(num):
    if num%2 ==0:
        return isUsual(num/2)
    elif num%3==0:
        return isUsual(num//3)
    elif num%5==0:
        return isUsual(num//5)
    elif num==1:
        return True
    else:
        return False
a = int(input())
if isUsual(a):
    print("Yes")
else:
    print("No")

        