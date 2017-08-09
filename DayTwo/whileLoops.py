i = 0

while i < 10:
    print(i)
    i += 1


############################
print()

isItDone = False
number = 10

while not isItDone:

    print("the number is", number)
    if number == 24:
        print("DONE!!!")
        isItDone= True
    else:
        number += 1

