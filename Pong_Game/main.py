#By end of the day we will make the pong game in python by  using he turtle grapics documentation.
import turtle 
from turtle import Screen,Turtle
from paddle import Paddle 
from ball import Ball
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(width =800, height = 600)
screen.bgcolor("black")
screen.title("Welcome to my pong game")
screen.tracer(0)
screen = turtle.Screen()
image = "Pong_Game/background.gif"
screen.addshape(image)
turtle.shape(image)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5,stretch_len=1)
# paddle.penup()
# paddle.goto(350,0)#(Here 350 at X axis & 0 at Y axis)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))# top_paddle = Paddle((100, 100))#we can make many paddle as just write like this beoz of the paddle class.
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)#0.07#
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()#needs to bounce

    #Detect collision with r_paddle 
    if ball.distance(r_paddle)< 50 and ball.xcor() > 320 or ball.distance(l_paddle)< 50 and ball.xcor() < -320:
        ball.bounce_x()#needs to bounce

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        













screen.exitonclick()