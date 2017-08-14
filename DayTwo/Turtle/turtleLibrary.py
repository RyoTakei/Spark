import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()
my_turtle.speed(20)

def square(dist, angle):
    for i in range(0, 4):
        my_turtle.forward(dist)
        my_turtle.left(angle)

for i in range(0, 200):
    my_turtle.left(7)
    square(100, 90)

my_turtle.done()