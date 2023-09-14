import turtle

def left():
    turtle.setheading(0)
    turtle.left(180)
    turtle.forward(50)
    turtle.stamp()
def right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def up():
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()
def down():
    turtle.setheading(0)
    turtle.right(90)
    turtle.stamp()
def restart():
    turtle.reset()
    
turtle.shape('turtle')
turtle.onkey(left,'a')
turtle.onkey(right,'d')
turtle.onkey(up,'w')
turtle.onkey(down,'s')
turtle.onkey(restart,'Escape')
turtle.listen()

#2022182015 박아연
