from turtle import *
import random

tommy = Turtle()
myscreen = Screen()
myscreen.bgcolor("black")

tommy.shape("turtle")
tommy.hideturtle()


rainbow_color = ["blue" , "green" , "yellow" , "red"]
random.shuffle(rainbow_color)

myscreen.colormode(255)

for i in range(int(360)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    tommy.speed("fastest")
    tommy.color(rainbow_color[int(i/90)])
    tommy.pensize(1)
    tommy.forward(50+i)
    tommy.left(91)


myscreen.exitonclick()


