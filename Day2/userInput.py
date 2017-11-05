import datetime

today = datetime.date.today()
print(datetime.date.today())

# print(datetime.date.today().weekday())
# print(datetime.date.today().isoweekday())

timeDelta = datetime.timedelta(days=20)
print(datetime.date.today() - timeDelta)
print(today + timeDelta)

bday = datetime.date(2017, 9, 26)
print(bday)

print(bday - today)