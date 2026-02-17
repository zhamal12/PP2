#1
from datetime import date

d = date(2026, 2, 18)
print(d)
print(d.year)
print(d.month)
print(d.day)

#2
from datetime import datetime

now = datetime.now()
print(now)

#3
dt = datetime(2026, 2, 18, 14, 30, 00)
print(dt)

#4
now = datetime.now()
print(now.strftime("%d/%m/%Y"))

#5
print(now.strftime("%Y-%m-%d %H:%M:%S"))
