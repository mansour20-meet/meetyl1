import random

from turtle import *
colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return(r,g,b)

class square(turtle):
    def __init__(self,size):
        turtle.__init__(self)
        self.size = size
        self.shape("square")
        self.shapesize(size)
        self.color(random_color())

square = square(5)
