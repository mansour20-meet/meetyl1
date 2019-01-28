import turtle
import time
import random
import math
from ball import Ball

turtle.colormode(255)

turtle.bgcolor("sky blue")
turtle.tracer(0)
turtle.hideturtle()
running=True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

my_ball = Ball(0,0,10,20,50,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))

number_of_balls=5

minimum_ball_radius = 10
maximum_ball_radius = 120

minimum_ball_dx = -5
maximum_ball_dx = 5

minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS=[]

for i in range(number_of_balls):
    x=random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)
    y=random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)

    dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    while (dx == 0):
    	dx=random.randint(minimum_ball_dx , maximum_ball_dx)

    dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    while (dy == 0):
    	dy=random.randint(minimum_ball_dy , maximum_ball_dy)

    r=random.randint(minimum_ball_radius , maximum_ball_radius)
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #print("color")
    new_ball = Ball(x,y,dx,dy,r,color)
    BALLS.append(new_ball)

def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width , screen_height)

def collide(ball_a,ball_b):
        if (ball_a==ball_b):
            return False
        if ball_a.r + ball_b.r >= ((ball_a.xcor()-ball_b.xcor())**2+(ball_a.ycor()-ball_b.ycor())**2)**.5:
            return True
        else:
            return False

def check_all_balls_collisions():
    global running
    all_balls = []
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)

    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a , ball_b):
                #print("COLLIDE")
                r1 = ball_a.r
                r2 = ball_b.r
                x = random.randint(-screen_width + maximum_ball_radius , screen_width - maximum_ball_radius)

                y = random.randint(-screen_height + maximum_ball_radius , screen_height - maximum_ball_radius)

                dx = random.randint( minimum_ball_dx , maximum_ball_dx )
                while (dx == 0):
                    dx = random.randint( minimum_ball_dx , maximum_ball_dx )

                dy = random.randint( minimum_ball_dy , maximum_ball_dy )
                while (dy == 0):
                    dy = random.randint( minimum_ball_dy , maximum_ball_dy )

                r = random.randint( minimum_ball_radius , maximum_ball_radius )

                color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

                if r1 > r2:
                    if ball_b == my_ball:
                        running = False
                        print ("game over")
                    else :
                        ball_b.new_Ball(x,y,dx,dy,r,color)
                        ball_a.r+=2
                        ball_a.shapesize(ball_a.r/10)
                else:
                    if ball_a == my_ball:
                        running = False
                        print ("game over")
                    else:
                        ball_a.new_Ball(x,y,dx,dy,r,color)
                        ball_b.r+=2
                        ball_b.shapesize(ball_b.r/10)
        
def move_around():
    x_coordinate=turtle.getcanvas().winfo_pointerx() - screen_width * 2
    y_coordinate=screen_height*1.4 - turtle.getcanvas().winfo_pointery()
    my_ball.goto(x_coordinate , y_coordinate)
    my_ball.x = x_coordinate
    my_ball.y = y_coordinate
    
    
while running == True:
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2
    #print("...")
    move_around()
    move_all_balls()
    check_all_balls_collisions()
    turtle.update()
    time.sleep(.1)

if my_ball.r >= 150:
    running = False
    print ("game over")
    turtle.write("YOU WON",move=False,align="center",font=("Arial",60,"normal"))
else:
    turtle.write("YOU FAILED",move=False,align="center",font=("Arial",60,"normal"))
        
    
turtle.mainloop()
