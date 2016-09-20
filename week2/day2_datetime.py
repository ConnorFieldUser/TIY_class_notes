

import datetime

# 3-1-2015

day = datetime.datetime(year=2015, month=3, day=1)

print(day - datetime.timedelta(hours=12))

now = datetime.datetime.now()
print(now.weekday())
print(now.day)
print(now)
now_formatted = (now.strftime("%A, %B %d, %Y, %H:%M.%S"))

# print(now_formatted)

now_obj = (datetime.datetime.strptime(now_formatted, "%A, %B %d, %Y, %H:%M.%S"))
print(type(now_obj))
print(now_obj)

now_formatted = (now.strftime("%A, %B %d, %Y, %H:%M.%S"))
