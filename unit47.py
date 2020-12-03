import time

d = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(d)

import datetime

d = datetime.datetime.today()
print(d)

d= datetime.datetime(2020, 10, 1)
print(d)

d= datetime.datetime.strptime('2018-05-10', '%Y-%m-%d')
print(d)

d = datetime.datetime(2019, 10, 21)
from datetime import timedelta
d = d - timedelta(days=20)
print(d)

eval('print(1, 2)')
