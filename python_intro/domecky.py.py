from turtle import forward, backward, right, left, speed,shape,bgcolor, exitonclick,goto, penup, pendown
from math import sqrt
from random import randint

def house(a):
    u =sqrt(2*a**2)
    left(90)
    forward(a)
    right(135)
    forward(u)
    left(135)
    forward(a)
    left(90)
    forward(a)
    right(135)
    forward(u/2)
    right(90)
    forward(u/2)
    right(90)
    forward(u)
    left(135)
    forward(a)


shape("turtle")
penup()
goto(-400,0)
pendown()
for i in range (0,10):
    house(randint(10,100))
exitonclick()