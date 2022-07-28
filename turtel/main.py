from turtle import *
import random
timmy_turtle = Turtle()
colors=["red","green","yellow"]
def draw_shape(numside):
    
    angle = 360/numside

    for _ in range(numside):
        timmy_turtle.shape("turtle")
        
        timmy_turtle.forward(100)
        timmy_turtle.right(angle)

for shapen in range(3,11):
    draw_shape(shapen)
    timmy_turtle.color(random.choice(colors))



















scree = Screen()
scree.exitonclick()