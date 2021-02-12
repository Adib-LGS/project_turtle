#  Import turtle + add first Object Turtle
import turtle

t = turtle.Turtle()


# creat function avoid repetition
def leftfor(tall):
    t.forward(tall)
    t.left(90)


def rightfor(tall):
    t.forward(tall)
    t.right(90)


# function to choose tall + number of steps
def steps(tall, number_of_steps):
    for i in range(0, number_of_steps):
        leftfor(tall)
        rightfor(tall)
        # Lower steps
        tall -= 5
    t.forward(tall)


# function to create a square
def square(tall):
    for i in range(0, 5):
        leftfor(tall)


# function to create a squares in square
def squares(starting_tall, numbers_of_squares):
    for i in range(1, numbers_of_squares):
        tall = i * starting_tall
        square(tall)


# calling steps function dynamically
steps(40, 6)
square(30)
squares(10, 10)


turtle.done()