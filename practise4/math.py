import math

def Ex1():
    a = float(input("Input degree: "))
    print(f"Output radian: {round(math.radians(a),5)}")


def Ex2():
    h = float(input("Height: "))
    b1 = float(input("Base, first value: "))
    b2 = float(input("Base, second value: "))

    print(f"Expected Output:{round((b1 + b2) / 2 * h,2)}")

def Ex3():
    n = int(input("Input number of sides: "))
    a = float(input("Input the length of a side: "))
    area = (n*a**2)/(4*math.tan(math.pi/n))
    print("The area of the polygon is:",round(area,2))
def Ex4():
    b = float(input("Length of base: "))
    h = float(input("Height of parallelogram: "))
    print(f"The area of the polygon is: {b*h}")

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

while True:
    a = input("\nPress any button to start or 'q' to quit: ")
    if a.lower() == 'q':
        break

    while True:
        try:
            b = int(input("Choose ex 1-4: "))
            print()
            if 1 <= b <= 5:
                Gen_Ex(b)
                break
            else:
                print("Enter number 1-4 ")
        except ValueError:
            print("Enter a NUMBER")


"""
    pow(num, power): возведение числа num в степень power

    sqrt(num): квадратный корень числа num

    ceil(num): округление числа до ближайшего наибольшего целого

    floor(num): округление числа до ближайшего наименьшего целого

    factorial(num): факториал числа

    degrees(rad): перевод из радиан в градусы

    radians(grad): перевод из градусов в радианы

    cos(rad): косинус угла в радианах

    sin(rad): синус угла в радианах

    tan(rad): тангенс угла в радианах

    acos(rad): арккосинус угла в радианах

    asin(rad): арксинус угла в радианах

    atan(rad): арктангенс угла в радианах

    log(n, base): логарифм числа n по основанию base

    log10(n): десятичный логарифм числа n

"""