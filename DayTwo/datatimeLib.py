import datetime

print(dir(datetime))
# working with year, month, date
# setting the date
day = datetime.date(2017, 8, 25)
print(day)

# today()
today = datetime.date.today()
print(today)

# year()
year = datetime.date.year
print(year)

# week day 1
weekDay1 = datetime.date.today().isoweekday()
print(weekDay1)
'''
Monday = 1 
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
'''

# week day 2
weekDay2 = datetime.date.today().weekday()
print(weekDay2)
'''
Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6
'''

timeDelta = datetime.timedelta(days=7)

print(today + timeDelta)

print(today - timeDelta)

bday = datetime.date(2017, 9, 26)

daysleft = bday - today
print(daysleft.days)
print(daysleft.total_seconds())

#####################################

# working with hour, min, sec, microsec


time = datetime.time(10, 56, 43, 0)
print(time)
print(time.hour)

####################################

# Everything

dateTime = datetime.datetime(2017, 8, 12, 22, 57, 38, 0)
print(dateTime)
print(dateTime.hour)
print(dateTime.minute)

print(dateTime + timeDelta)

timeDelta2 = datetime.timedelta(hours=12)

print(dateTime + timeDelta2)

#####################################

# Different stuff
dateTime_today = datetime.datetime.today()
dateTime_now = datetime.datetime.now()
dateTime_utc = datetime.datetime.utcnow()

print(dateTime_today)
print(dateTime_now)
print(dateTime_utc)

#####################################

print(today.strftime("%A, %B, %d, %Y"))