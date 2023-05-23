import datetime

def count_saturdays(year):
    num_saturdays = 0
    date = datetime.date(year, 1, 1)
    while date.year == year:
        if date.weekday() == 5:
            num_saturdays += 1
        date += datetime.timedelta(days=1)
    return num_saturdays

print(count_saturdays(2000))