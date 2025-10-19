import turtle
t=turtle.Turtle()
t.speed(0)
turtle.bgcolor("navy")
t.color("yellow")

def star(size,depth):
    if depth==0:
        return
    for i in range(5):
        t.forward(size)
        star(size/2,depth-1)
        t.right(144)

t.penup()
t.goto(-100,-50)
t.pendown()
star(200,3)
turtle.done()
