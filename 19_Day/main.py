from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = -120
all_turtles = []

for col in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(col)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis)
    all_turtles.append(new_turtle)
    y_axis += 50

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} color turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} color turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
