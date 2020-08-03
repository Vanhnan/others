from turtle import *
import time

shape("turtle")

FACTOR = False

def up():
    setheading(90)
    forward(100)
    FACTOR = True

def down():
    setheading(270)
    forward(100)
    FACTOR = False

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)

##def blue_screen():
##    bgcolor(0.7, 1.0, 1.0)
##
##def white_screen():
##    bgcolor(1.0, 1.0, 1.0)


if FACTOR == True:
    bgcolor("green")
elif FACTOR == False:
    bgcolor("red")

onkey(up, "Up")
onkey(down, "Down")
onkey(left, "Left")
onkey(right, "Right")


    
listen()

