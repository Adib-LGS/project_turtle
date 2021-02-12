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


def carre(tall):
    for i in range(0, 5):
        leftfor(tall)


# calling steps function dynamically
steps(40, 6)
carre(30)

turtle.done()