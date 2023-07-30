from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def move_fd():
    tim.fd(10)
def move_bd():
    tim.bk(10)
def move_lt():
    tim.lt(10)
def move_rt():
    tim.rt(10)
def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(fun=move_fd, key="Up")
screen.onkey(fun=move_lt, key="Left")
screen.onkey(fun=move_rt, key="Right")
screen.onkey(fun=move_bd, key="Down")
screen.onkey(fun=clear, key="c")
screen.exitonclick()