def Squares(a,b):
    for i in range(a,b+1):
        yield i*i

a,b = map(int,input().split())
for x in Squares(a,b):
    print(x)