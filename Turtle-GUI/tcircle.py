import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ra_color = (r, g, b)
    return ra_color

# With this approach, the spirograph will be completed but after that also it will keep on drawing to complete 100 circles
# for _ in range(100):
#     tim.speed("fastest")
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 10)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
