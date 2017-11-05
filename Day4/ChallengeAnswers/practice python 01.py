import datetime
now = datetime.datetime.now()
name = input("whats your name:")
age = int(input("how old are you:"))
year = str((now.year - age)+100)
print("you will 100 years old in the year " + year)