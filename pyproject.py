import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("Drawing lines Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(2)
my_turtle.shape("circle")
my_turtle.forward(100)

for i in range(0,8):
    my_turtle.forward(100)
    my_turtle.backward(100)
    my_turtle.left(45)
    
my_turtle.hideturtle()
my_turtle.done()
    
