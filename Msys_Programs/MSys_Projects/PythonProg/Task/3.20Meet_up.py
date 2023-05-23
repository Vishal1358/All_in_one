import datetime

def meetup_date(year, month):
    
    d = datetime.date(year, month, 1)
    while d.weekday() != 3:
        d += datetime.timedelta(1)
    d += datetime.timedelta(weeks=3)
    return d

print(meetup_date(2023,3))