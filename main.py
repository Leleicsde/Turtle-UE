import turtle

window = turtle.Screen()
window.bgcolor("black")

t = turtle.Turtle()
t.speed(10)
t.color("pink")


# Draw a smaller flower
t.begin_fill()
for _ in range(18):
    t.circle(10, 170)
    t.left(170)
t.end_fill()

t.penup()
t.goto(60, -120)  # Adjust the y-coordinate to position the stem as needed
t.pendown()

t.color("green")
t.pensize(5)
t.setheading(90)
t.forward(80)

turtle.done()
