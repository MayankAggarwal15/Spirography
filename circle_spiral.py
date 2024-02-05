from turtle import *
import random

tommy = Turtle()
myscreen = Screen()
myscreen.bgcolor("black")

tommy.shape("turtle")
tommy.hideturtle()

myscreen.colormode(255)

for i in range(int(360/5)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    tommy.speed("fastest")
    tommy.color(r,g,b)
    tommy.pensize(1)
    tommy.circle(100)
    tommy.left(5)



myscreen.exitonclick()

