import datetime as dt;
import time as tm;

print(tm.time());

dtime=dt.datetime.fromtimestamp(tm.time())
print(dtime)

print(dtime.year)
print(dtime.month)
print(dtime.day)
print(dtime.hour)
print(dtime.minute)
print(dtime.second)

today=dt.date.today()
print(today)

print(dtime.now())
