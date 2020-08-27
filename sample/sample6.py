import turtle

turtle.speed(10)
for i in range(100):
    if i % 2 == 0:
        turtle.right(90)
    else:
        turtle.left(35)
    turtle.forward(40)

input("終了するにはENTERキーを押してください")