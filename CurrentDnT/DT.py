from datetime import date , time, datetime

today = date.today()
now = datetime.now()
print("Today's date is", today)
print("The current date and time is", now)

print("\nDate components", today.year, today.month, today.day)