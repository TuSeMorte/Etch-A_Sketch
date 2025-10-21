from turtle import Turtle, Screen

lo = Turtle()
screen = Screen()

screen.listen()
screen.setup(800, 600)

def move_forwards():
    lo.forward(10)

def move_backwards():
    lo.backward(10)

def turn_left():
    new_heading = lo.heading() +  10
    lo.setheading(new_heading)

def turn_right():
    new_heading = lo.heading() + 10
    lo.setheading(new_heading)

def clear():
    lo.clear()
    lo.penup()
    lo.home()
    lo.pendown()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
