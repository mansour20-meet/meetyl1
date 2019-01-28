from turtle import*
import turtle
class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.dx=dx
        self.dy=dy
        self.r=r
        self.x=x
        self.y=y
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
    def move(self,screen_width,screen_height):
        new_x = self.x + self.dx
        new_y = self.y + self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        top_side_ball = new_y + self.r
        bottom_side_ball = new_y - self.r
        self.goto(new_x,new_y)
        self.x = new_x
        self.y = new_y
        if right_side_ball >= screen_width:
            self.dx = -self.dx
        if left_side_ball <= -screen_width:
            self.dx = -self.dx
        if top_side_ball >= screen_height:
            self.dy = -self.dy
        if bottom_side_ball <= -screen_height:
            self.dy = -self.dy
    def new_Ball(self,x,y,dx,dy,r,color):
        self.penup()
        self.goto(x,y)
        self.x = x
        self.y = y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)
        
        
        
            
        
        
        
        
                     
        
    
