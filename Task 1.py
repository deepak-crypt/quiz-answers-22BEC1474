import turtle
a = turtle.Turtle()
b = ["violet","blue","green","yellow","orange","red"]
turtle.bgcolor("black")

for i in range(36):
    a.pencolor(b[i%6])
    a.forward(70)
    a.left(10)
    a.forward(60)
    a.right(20)
    a.goto(0,0)



turtle.done()
