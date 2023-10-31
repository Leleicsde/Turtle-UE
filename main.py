import turtle

def star(x, y, size):
    t = turtle.Turtle()
    t.speed(10)
    t.color("yellow")

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

    t.hideturtle()


window = turtle.Screen()
window.bgcolor("dark blue")


pos = [
    (0, 150, 50),
    (129.90, 75.00, 30),
    (129.90, -75.00, 40),
    (0, -150, 35),
    (-129.90, -75.00, 25),
    (-129.90, 75.00, 45),
    (75.00, 129.90, 20),
    (-75.00, 129.90, 30),
    (-75.00, -129.90, 35),
    (75.00, -129.90, 40),
    (150, 0.00, 45),
    (-150, 0.00, 30)
]


for x, y, size in pos:
    star(x, y, size)

turtle.done()