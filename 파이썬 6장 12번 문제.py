import turtle
import math

t= turtle.Turtle()
t.shape("turtle")
t.color("red")

for i in range(360):
    sine=math.sin(math.pi*i/180)
    print(sine)
    t.goto(i,sine*100)
