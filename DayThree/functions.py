# pass
def hello():
    pass

hello()
##########################


# just to print
def hello_world():
    print("Hello world")

hello_world()
##########################


# return and type(string)
def hello_world2():
    return "Hello World"

print(hello_world2())
print(type(hello_world2()))
print(len(hello_world2()))
print(type(hello_world2))
# print(len(hello_world2))
###########################


# argument
def hello_name(name):
        return "Hello, {}".format(name)

print(hello_name("Jack"))
print(hello_name("class"))
###########################


# default value
def name_and_age(name, age = 15):
    return "{}, you are {} years old!".format(name, age)

print(name_and_age("Ryo", 16))
print(name_and_age("Ryo"))
##########################


def addone(number):
    '''add one to the number and returns it'''
    return number + 1

print(help(addone))

num1 = 7
num2 = addone(num1)
print(num2)

###########################
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# list and index
def get_element(list, index):
    return list[index]

print(get_element(list1, 4))
