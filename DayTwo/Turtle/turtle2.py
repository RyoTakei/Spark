import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.speed(20)

for i in range(100):
    my_turtle.circle(5 * i)
    my_turtle.circle(-5 * i)
    turtle.left(5)

my_turtle.done()

