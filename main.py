from turtle import Turtle, Screen
import random


race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="Who's the bet?", prompt="Chose the color: ").lower()
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
turtles = []

y = -125
count = 0
for n in range(0, 6):
    n = Turtle(shape="turtle")
    n.color(colors[count])
    n.penup()
    n.goto(-230, y)
    y += 50
    count += 1
    turtles.append(n)


while race_on:

    for n in turtles:
        if n.xcor() > 230:
            winner = n.pencolor()
            race_on = False
            if user == winner:
                print(f"You Won! The {winner} turtle is first!")
            else:
                print(f"You Loose! The {winner} turtle is first!")
        ran_mov = random.randint(0, 10)
        n.forward(ran_mov)

# def forward():
#     wachin.forward(10)
#
#
# def backward():
#     wachin.backward(10)
#
#
# def left():
#     wachin.left(10)
#
#
# def right():
#     wachin.right(-10)
#
#
# def reset():
#     wachin.reset()
#
#
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=backward)
# screen.onkey(key="a", fun=left)
# screen.onkey(key="d", fun=right)
# screen.onkey(key="c", fun=reset)
#
# screen.listen()
screen.exitonclick()
