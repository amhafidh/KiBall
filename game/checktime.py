import time


last_time = get_last_time()
now = time.time() - last_time
minute = now % 60
seconds = now / 60
print(seconds)


2
>>> import time
>>> then = time.time()
>>> now = time.time()
>>> diff = now - then
>>> diff
6.54801607131958

3
last_time = get_last_time()
time_diff = round(time.time() - last_time)
minute = time_diff / 60
seconds = time_diff % 60  # Same as time_diff - (minutes * 60)
print 'Next time you add blood is '+minute+':'+seconds

4
lapTime = round(time.time() - lastTime, 2)
➍         totalTime = round(time.time() - startTime, 2)
➎         print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')


  >>> import datetime
➊ >>> datetime.datetime.now()
➋ datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
➌ >>> dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
➍ >>> dt.year, dt.month, dt.day
   (2015, 10, 21)
➎ >>> dt.hour, dt.minute, dt.second
   (16, 29, 0)


The datetime module also provides a timedelta data type, which represents a duration of time rather than a moment in time. Enter the following into the interactive shell:

➊ >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
➋ >>> delta.days, delta.seconds, delta.microseconds
   (11, 36548, 0)
   >>> delta.total_seconds()
   986948.0
   >>> str(delta)
   '11 days, 10:09:08'
