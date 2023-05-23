# import datetime
from datetime import datetime

# mytime = datetime.time(20)
# a =mytime.minute
# b = mytime.hour
# c = mytime.microsecond

# today1 = datetime.date.today()
# print(today1.ctime())


# print(mytime,a,b,c)


mydatetime = datetime(2022,8,11,2,21,50,2)
print(mydatetime)
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)