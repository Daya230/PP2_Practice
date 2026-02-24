import datetime

a, b = input().strip(), input().strip()

s_day = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S UTC%z")
e_day = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S UTC%z")

delta = abs((s_day - e_day).total_seconds())
print(int(delta))