#1
import datetime

x = datetime.datetime.now()
new_date = x - datetime.timedelta(days=5)

print(new_date)

#2
import datetime

today = datetime.date.today()
yesterday =today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(today)
print(yesterday)
print(tomorrow)

#3
import datetime

x = datetime.datetime.now()
without_micro = x.replace(microsecond=0)

print(without_micro)

#4
import datetime

date1 = datetime.datetime(2026, 2, 19, 12, 0, 0)
date2 = datetime.datetime(2026, 2, 19, 14, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)