import calendar 

year, month, day= map(int, input().split())

day_number= calendar.weekday(year, month, day)

days= ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[day_number])