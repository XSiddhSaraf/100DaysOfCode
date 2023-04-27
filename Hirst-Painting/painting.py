# import colorgram  ##This piece of code is to extract color from an image

# color = colorgram.extract('image.jpg', 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed('fastest')
tim.penup()
tim.hideturtle()

color_list = [(197, 165, 117), (142, 80, 55), (221, 202, 136), (59, 94, 120), (167, 153, 49), (136, 162, 181), (135, 33, 21), (70, 39, 31), (52, 118, 86), (194, 93, 76), (145, 177, 148), (18, 92, 68), (167, 143, 158),
              (114, 73, 79), (31, 59, 77), (229, 176, 163), (129, 29, 34), (179, 205, 176), (69, 35, 38), (24, 82, 90), (19, 68, 58), (87, 147, 127), (38, 66, 93), (221, 176, 181), (175, 98, 102), (179, 191, 207)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
