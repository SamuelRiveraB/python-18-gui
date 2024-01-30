import random
from turtle import Turtle, Screen
import turtle as t
t.colormode(255)

colors = [(209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (254, 230, 0), (20, 166, 126), (211, 232, 236), (244, 223, 50), (27, 197, 219), (162, 184, 171)]

timmy = Turtle()
timmy.shape('turtle')
timmy.width(20)
timmy.speed(0)
x = -390
y = -300
timmy.teleport(x, y)

for i in range(0, 10):
    for i in range(0, 10):
        timmy.color(random.choice(colors))
        timmy.up()
        timmy.forward(70)
        timmy.dot()
    y += 70
    timmy.teleport(x, y)

screen = Screen()
screen.exitonclick()

