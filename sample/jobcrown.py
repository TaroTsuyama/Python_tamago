import turtle
import time

def set_pos(x=0,y=0):
    turtle.penup()
    turtle.goto(x,y)
    turtle.right(turtle.heading())
    turtle.pendown()

mag = 12 # magnification

turtle.setup(width=500,height=500)
turtle.shape("turtle")
turtle.speed(10)

# time.sleep(10)

# グレーのところ
turtle.color("#454A45")
turtle.begin_fill()
set_pos(-0.2*mag,-10.4*mag)
turtle.circle(10*mag)
turtle.end_fill()


# 青いところ
turtle.color("#01B4EE")
turtle.begin_fill()
set_pos(0.2333*mag,0.3414*mag)
turtle.left(90)
turtle.circle(48.8945*mag,4)
turtle.circle(0.7896*mag,139)
turtle.circle(-1.2665*mag,281)
turtle.circle(0.7896*mag,139)
turtle.circle(-48.8945*mag,4)
turtle.right(turtle.heading())
turtle.circle(-9.9991*mag,125)
turtle.right(turtle.heading())
turtle.left(136)
turtle.circle(48.8945*mag,4)
turtle.circle(-0.1974*mag,138)
turtle.circle(1.8737*mag,279)
turtle.circle(-0.1974*mag,138)
turtle.circle(48.8945*mag,4.8)
turtle.end_fill()

# 緑のところ
turtle.color("#8FC31D")
turtle.begin_fill()
set_pos(-0.3708*mag,0.3087*mag)
turtle.left(90)
turtle.circle(48.8945*mag,4)
turtle.circle(0.1974*mag,138)
turtle.circle(-1.8737*mag,279)
turtle.circle(0.1974*mag,138)
turtle.circle(-48.8945*mag,4)
turtle.right(turtle.heading())
turtle.left(180)
turtle.circle(9.9991*mag,125)
turtle.right(turtle.heading())
turtle.left(41)
turtle.circle(-48.8945*mag,4)
turtle.circle(0.1974*mag,138)
turtle.circle(-1.8737*mag,279)
turtle.circle(0.1974*mag,138)
turtle.circle(48.8945*mag,5)
turtle.end_fill()

# オレンジのところ
turtle.color("#F7B52B")
turtle.begin_fill()
set_pos(-0.0434*mag,-0.1997*mag)
turtle.right(32)
turtle.circle(-48.8945*mag,4.8)
turtle.circle(0.7896*mag,139)
turtle.circle(-1.2665*mag,281)
turtle.circle(0.7896*mag,139)
turtle.circle(-48.8945*mag,4)
turtle.right(turtle.heading())
turtle.right(125)
turtle.circle(-9.9991*mag,110)
turtle.right(turtle.heading())
turtle.left(40)
turtle.circle(-48.8945*mag,4)
turtle.circle(0.7896*mag,139)
turtle.circle(-1.2665*mag,281)
turtle.circle(0.7896*mag,145)
turtle.circle(-48.8945*mag,5.2)
turtle.end_fill()



turtle.hideturtle()

input("終了するにはENTERキーを押してください")