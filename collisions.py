from turtle import *
import random
import math

class Ball(Turtle):
    def __init__( self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1 = Ball(15, "red", 40)
ball2 = Ball(8, "blue" , 50)

def check_collision(ball1, ball2):
    x2=ball2.pos()[0]
    x1=ball1.pos()[0]
    y2=ball2.pos()[1]
    y1=ball1.pos()[1]
    if ball1.radius + ball2.radius >= math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)):
        print ("collision")





