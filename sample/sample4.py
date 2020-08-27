import turtle

turtle.speed(10)
for _ in range(100):
    for _ in range(3):
        turtle.forward(50)
        turtle.right(120)
    turtle.right(33)

input("終了するにはENTERキーを押してください")