from turtle import *

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
left(90)
circle(250, 180)

for i in range(4):
    forward(10)
    right(90/4)

exitonclick()