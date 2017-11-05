age = 12


if age > 16:
    print("You can drive")
else:
    print("You cannot drive")

if age >= 21:
    print("You can drink")
else:
    print("You cannot drink")


######################

if age > 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teen")
else:
    print("You are a kid")

#####################

print("\nTrue & True =", True & True)
print("\nTrue & False =", True & False)
print("\nFalse & False =", False & False)
print("\nTrue | True =", True | True)
print("\nTrue | False =", True | False)
print("\nFalse | False =", False | False)
print("\n!True =", not True)
print("\n!False =", not False)


####################

if ((age >= 1) & (age <= 18)):
    print("\nYou're somewhere between 1~18")
elif (age == 21) | (age >= 80):
    print("your 21 or 80+")
elif not (age == 30):
    print("Youre not 30")
else:
    print("ehhh whatever")
