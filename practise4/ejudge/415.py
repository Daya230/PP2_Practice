from datetime import datetime, timedelta

a = input().strip()
b = input().strip()

b_day = datetime.strptime(a, "%Y-%m-%d UTC%z")
c_day = datetime.strptime(b, "%Y-%m-%d UTC%z")

year = c_day.year
try:
    next_bday = datetime(year, b_day.month, b_day.day, tzinfo=b_day.tzinfo)
except ValueError:  
    next_bday = datetime(year, 2, 28, tzinfo=b_day.tzinfo)

if next_bday < c_day:
    year += 1
    try:
        next_bday = datetime(year, b_day.month, b_day.day, tzinfo=b_day.tzinfo)
    except ValueError:
        next_bday = datetime(year, 2, 28, tzinfo=b_day.tzinfo)

delta = next_bday - c_day
days = delta.days + (delta.seconds > 0)
print(days)