from turtle import *
import random

tommy = Turtle()
myscreen = Screen()
myscreen.bgcolor("black")

tommy.shape("turtle")
tommy.hideturtle()

flag_color = ["orange" , "white" , "green"]

rainbow_color = ["violet" , "blue" , "green" , "yellow" , "orange" , "red"]
random.shuffle(rainbow_color)

myscreen.colormode(255)

for i in range(int(360)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    tommy.speed("fastest")
    tommy.color(rainbow_color[i%len(rainbow_color)])
    tommy.pensize(1)
    tommy.forward(i)
    tommy.left(59)


myscreen.exitonclick()


