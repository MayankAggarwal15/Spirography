from turtle import *
import random

tommy = Turtle()
myscreen = Screen()

tommy.shape("turtle")
tommy.hideturtle()

myscreen.colormode(255)

for i in range(int(1000)):
    
    tommy.speed("fastest")
    tommy.pensize(7.5)
    tommy.forward(i/300)

    tommy.left(2)



myscreen.exitonclick()

