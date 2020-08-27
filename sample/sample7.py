import turtle
import random

turtle.speed(10)
turtle.colormode(255)
turtle.width(2)

def random_color():
    color = (random.randint(0,255) for _ in range(3))
    return tuple(color)

for i in range(100):
    turtle.color(random_color())
    if i % 2 == 0:
        turtle.right(90)
    else:
        turtle.left(35)
    turtle.forward(40)

input("終了するにはENTERキーを押してください")