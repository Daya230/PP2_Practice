import datetime

a = input()
b = input()
d_1 = datetime.datetime.strptime(a, "%Y-%m-%d UTC%z")
d_2 = datetime.datetime.strptime(b, "%Y-%m-%d UTC%z")

delta = d_1 - d_2
print(abs(delta).days)