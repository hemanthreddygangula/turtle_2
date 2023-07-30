from turtle import Turtle,Screen
from tkinter import *
from tkinter import messagebox
import random

colors = ['red', 'blue', 'yellow', 'green', 'violet', 'indigo', 'orange']
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place Your Bet", prompt="Which Turtle will win the Race? Choose the color(VIBGYOR): ")

turtles = []
a = [0, 50, -50, 100, -100, 150, -150]
for i in range(7):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(colors[i])
        new_turtle.goto(x=-230, y= a[i])
        turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
      for turtle in turtles:
            if turtle.xcor() >230:
                    is_race_on = False
                    winning_color = turtle.pencolor().lower()
                    if winning_color[0] == bet.lower():
                        messagebox.showinfo(title='RESULT', message=f"You WON!!. {winning_color} won the race.")
                    else:
                        messagebox.showinfo(title='RESULT', message=f"You LOST!!. {winning_color} won the race.")
                    
            dist = random.randint(0,10)
            turtle.fd(dist)

screen.exitonclick()
