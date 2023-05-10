import turtle

window = turtle.Screen()
window.title("Flag of Vietnam")
window.bgcolor("white")

t = turtle.Turtle()
t.speed(2)
t.penup()
t.goto(-200, 100)
t.pendown()

t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(400)
    t.right(90)
    t.forward(266)
    t.right(90)
t.end_fill()
t.penup()
t.goto(-50, 0)
t.pendown()
t.color("yellow")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()

t.hideturtle()
window.exitonclick()
