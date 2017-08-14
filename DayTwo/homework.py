number = input("Please pick a number between 1 to 10: ")

while True:
    if int(number) == 4:
        print("You are correct!!")
        break
    else:
        number = input("The number you entered {} was wrong. Try another: ".format(number))
