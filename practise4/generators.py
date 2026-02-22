def Get_Num():
    while True:
        a = input("Enter number: ")
        try:
            a = int(a)
            return a
        except ValueError:
            print("Enter a NUMBER: ")        

def Ex1(): #Create a generator that generates the squares of numbers up to some number N

    def squares(N):
        for i in range(1, N+1):
            yield i**2

    N = Get_Num()
    for sq in squares(N):
        print(sq, end = ' ')
    print()
    


def Ex2():
    def Even_Num(N):
        for i in range(0,N+1,2):
            yield i
    N = Get_Num()
    print(*Even_Num(N), sep = ', ')
def Ex3():
    def Div(N):
        for i in range(N+1):
            if i%12 ==0:
                yield i
    N = Get_Num()
    l = Div(N)
    print(*l, sep = ', ')

def Ex4():
    def Squares(a,b):
        for i in range(a,b+1):
            yield i**2
    a = Get_Num()
    b = Get_Num()
    if a>b:
        b,a = a,b
    print(*Squares(a,b),sep = ' ')


def Ex5():
    def Rev_sort(a):
        for i in range(a,-1,-1):
            yield i
    a = Get_Num()
    print(*Rev_sort(a), sep = ' ')

def Gen_Ex(x):
    match x:
        case 1:
            Ex1()
        case 2:
            Ex2()
        case 3:
            Ex3()
        case 4:
            Ex4()
        case 5:
            Ex5()

while True:
    a = input("\nPress any button to start or 'q' to quit: ")
    if a.lower() == 'q':
        break

    while True:
        try:
            b = int(input("Choose ex 1-5: "))
            if 1 <= b <= 5:
                Gen_Ex(b)
                break
            else:
                print("Enter number 1-5 ")
        except ValueError:
            print("Enter a NUMBER")