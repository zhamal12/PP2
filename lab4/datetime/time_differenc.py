#1
import datetime

d1 = datetime(2026, 2, 18)
d2 = datetime(2026, 2, 10)

diff = d1 - d2
print(diff)

#2
from datetime import timedelta

future = datetime.now() + timedelta(days=10)
print(future)

#3
import datetime

d1 = datetime(2026, 2, 18)
d2 = datetime(2026, 2, 10)

diff = d1 - d2
print(diff)
print(diff.days)

#4
import datetime
past = datetime.now() - timedelta(hours=5)
print(past)

#5
d1 = datetime.now()
d2 = datetime(2026, 1, 1)

diff = d1 - d2
print(diff.total_seconds())
