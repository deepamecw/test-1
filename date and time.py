import datetime as dt
current_date = dt.date.today()
print("current date: ",current_date)
new = dt.date(2021, 11, 6 )
print(new)
print("year: ",new.year)
print("month:",new.month)
print("day: ",new.day)
a = dt.time(8,15,34,5555)
print(a)
print("hour: ",a.hour)
print("minute: ",a.minute)
print("sec: ",a.second)
print("millisec: ",a.microsecond)
current_time = dt.datetime.now()
print(current_time)
current_date = dt.date.today()
new_year = dt.date(2021,12,25)
difference = new_year-current_date
print(difference)
current_date = dt.datetime.now()
s = current_date.strftime("%A,%B,%d,%Y,%j,%U,%p")
print(s)