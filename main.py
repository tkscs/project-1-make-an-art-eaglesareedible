from turtle import *
import numpy as np
speed(0)

def drawarc(size, angle):
    for i in range(size):
        forward(50)
        left(angle*90/8)
def drawEye():
    begin_fill()
    circle(30)
    end_fill()
drawEye()
penup()
forward(300)
pendown()
drawEye()
penup()
setposition(425, 200)
pendown()
setheading(90)
circle(250, 180)
right(60)
drawarc(17, 1)
penup()
setposition(425, 200)
setheading(-30)
pendown()
drawarc(17, -1)
print(position())
exitonclick()