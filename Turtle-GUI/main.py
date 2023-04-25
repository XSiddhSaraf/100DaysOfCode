from turtle import Turtle, Screen
from random import choice
import random

tim = Turtle()
tim.shape('turtle')


colors = ["spring green", "dark orange", "red", "violet",
          "gold", "dark violet", "orchid", "royal blue"]


# def shape_n(n_sides):
#     angle = 360 / n_sides
#     for _ in range(n_sides):
#         tim.forward(100)
#         tim.right(angle)


# for shape_step in range(3, 11): #since range will take second argument as num+1 if we need range(1,num)
#     tim.color(choice(colors))
#     shape_n(shape_step)


direction = [0, 90, 180, 270]
tim.pensize(15)
for _ in range(200):
    tim.color(choice(colors))
    tim.forward(30)
    tim.setheading(choice(direction))
