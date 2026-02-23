import datetime

now = datetime.datetime.now()

def Ex1():    

    delta = datetime.timedelta(days = 5)
    print(f"Current date: {now}")
    print(f"subtract 5 days: {now - delta}")

def Ex2():
    delta = datetime.timedelta(days = 1)
    yesterday = now - delta
    tomorrow = now+delta
    print(f'yesterday: {yesterday.strftime("%d %B %Y")}\ntoday: {now.strftime("%d %B %Y")}\ntomorrow: {tomorrow.strftime("%d %B %Y")}')

def Ex3():
    n_micro = now.replace(microsecond = 0)
    print(f"with microsec: {now}")
    print(f"without microsec: {n_micro}")
    
def Ex4():
    date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
    date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")

    delta = date2 - date1
    print(f"difference in seconds: {abs(int(delta.total_seconds()))}")


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