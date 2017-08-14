def fibonacci(limit):
    '''function that makes a list of fibonacci numbers.
    argument 'limit' will set the limit'''

    # a, b, c
    a = 0
    b = 1
    c = 0
    fibonacciList = []

    while True:
        c = a + b
        if c > limit:
            break

        fibonacciList.append(c)
        a = b
        b = c

    return fibonacciList

print(fibonacci(1000))