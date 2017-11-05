def is_it_prime(number):
    '''get a number and if the number is a prime number, it will retrun True
    and it will return False if the number is not a prime number'''
    if number == 2 or number == 3:
        return True

    for x in range(2, number - 1):
        if number % x == 0:
            return False
    return True


primeList = []

for number in range(2, 100):
    if is_it_prime(number):
        primeList.append(number)

print(primeList)
