# syahmi method

import datetime
from datetime import datetime as dt
date_format = "%b %d %Y %I:%M%p"
t1 = dt.strptime(input(), date_format)
t2 = dt.strptime(input(), date_format)
delta = t2 - t1
print(f"{delta.days} days,", end=' ')
print(str(delta).split(', ')[1])   