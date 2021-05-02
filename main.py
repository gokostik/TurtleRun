import turtle
from turtle import Turtle, Screen
import random

is_race_on=False

screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Hello", prompt="Color please:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range (0, 6):
    timmy = Turtle(shape='turtle', )
    timmy.color(colors[turtle_index])
    timmy.penup()
    timmy.goto(-200, y_pos[turtle_index])
    all_turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for tim in all_turtles:
        if tim.xcor() > 220:
            color_win = tim.pencolor()
            if color_win == user_bet:
                screen.textinput(title="You Win", prompt="Lets one more time?")

        rand_distance = random.randint(0, 15)
        tim.forward(rand_distance)


screen.exitonclick()