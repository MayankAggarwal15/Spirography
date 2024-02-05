from turtle import *
import random

tommy = Turtle()
myscreen = Screen()
myscreen.bgcolor("black")

tommy.shape("turtle")
tommy.hideturtle()

flag_color = ["orange" , "white" , "green"]
rainbow_color = ["blue" , "yellow" , "red"]

flag_color.reverse()
random.shuffle(rainbow_color)

myscreen.colormode(255)

for i in range(int(360)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    tommy.speed("fastest")
    tommy.color(flag_color[int(i/120)])
    tommy.pensize(1)
    tommy.forward(100+i)
    tommy.left(121)


myscreen.exitonclick()


