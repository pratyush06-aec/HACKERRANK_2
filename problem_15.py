import calendar

year= int(input())
month= int(input())
day= int(input())

day_num= calendar.weekday(year, month, day)
print(calendar.day_name[day_num])