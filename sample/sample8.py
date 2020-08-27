import turtle

class Kame(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.colors = {
            "red":"#ff0000",
            "orange":"#ff8c00",
            "yellow":"#fff200",
            "green":"#40ff00",
            "skyblue":"#00ffe5",
            "blue":"#0000ff",
            "purple":"#c300ff",
        }

    def niji(self,distance,length=10):
        step = distance/length
        for i in range(int(step)):
            self.pencolor(list(self.colors.values())[i%len(self.colors)])
            self.forward(length)
        self.forward(step-int(step))
        self.pencolor("black")

    def dash(self,distance,length=10):
        step = distance/length
        for i in range(int(step)):
            self.forward(length)
            if self.isdown():
                self.penup()
            else:
                self.pendown()
        self.forward(step-int(step))
        self.pendown()


    def niji_dash(self,distance,length=10):
        step = distance/length
        for i in range(int(step)):
            self.pencolor([y for x in zip(self.colors.values(),self.colors.values()) for y in x][i%(len(self.colors)*2)])
            self.forward(length)
            if self.isdown():
                self.penup()
            else:
                self.pendown()
        self.pencolor([y for x in zip(self.colors.values(),self.colors.values()) for y in x][(i+1)%(len(self.colors)*2)])
        self.forward(step-int(step))
        self.pendown()
        self.pencolor("black")


kame = Kame()
kame.width(5)

kame.right(90)
kame.niji(150)
kame.right(90)
kame.forward(80)
kame.right(90)
kame.niji(120)
kame.penup()
kame.forward(50)
kame.pendown()
kame.forward(50)
kame.right(70)
kame.dash(120,20)
kame.dash(120)
kame.right(120)
kame.niji_dash(350,25)
kame.hideturtle()
