input_string = '2020-01-15 09:03:32.744178'

date_time = lambda data: tuple(input_string.split(" "))
date,time = date_time(input_string)
split_date = lambda data : date.split("-")
year,month,date = split_date(date)
print(f"Year: {year}") 
print(f"month: {month}") 
print(f"date: {date}") 
print(f"time: {time}")
