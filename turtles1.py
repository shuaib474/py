import turtle
import math 
screen=turtle.Screen()
t=turtle.Turtle()
screen.setup(800,800)
screen.title("几何")
screen.bgcolor("black")
t.speed(0)
t.hideturtle()
t.pensize(2)
t.pencolor("yellow")
def draw_flower(rotate_angle):
    t.setheading(rotate_angle)
    t.penup
    for a in range(360):
        rad=math.radians(a)
        r=200*math.sin(6*rad+math.radians(rotate_angle*5))
        x=r*math.cos(rad)
        y=r*math.sin(rad)
        t.goto(x,y)
        t.pendown()
angle=0
def rotate_animation():
    t.clear
    global angle
    angle+=1
    draw_flower(angle)
    screen.ontimer(rotate_animation,30)
rotate_animation()
turtle.done()
    
    