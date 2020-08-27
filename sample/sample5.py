import turtle

turtle.speed(10)
for _ in range(6):
    turtle.right(30)
    turtle.forward(50)
    turtle.left(30)
    turtle.circle(25,180)
    turtle.left(30)
    turtle.forward(50)
    turtle.left(150)
    turtle.right(60)
turtle.hideturtle()

input("終了するにはENTERキーを押してください")