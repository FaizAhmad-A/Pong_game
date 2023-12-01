import turtle
import time
win = turtle.Screen()
win.title("PONG GAME")
win.setup(800,600)
win.bgcolor("black")
win.tracer(0)

#left_paddle
left_pad = turtle.Turtle()
left_pad.shape("square")
left_pad.color("red")
left_pad.shapesize(stretch_len=1,stretch_wid=5)
left_pad.penup()
left_pad.speed(0)
left_pad.goto(-380,0)
left_pad.dx = 0
left_pad.dy = 0

#right_paddle
right_pad = turtle.Turtle()
right_pad.shape("square")
right_pad.color("blue")
right_pad.shapesize(stretch_len=1,stretch_wid=5)
right_pad.penup()
right_pad.speed(0)
right_pad.goto(375,0)

#ball_shape
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.speed(0)
ball.dx = 0.7
ball.dy = 0.7

# score
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0,260)
pen.write("Player A: 0     Player B: 0",align="center",font=("Ariel",25,"normal"))
pen.hideturtle()
scoreA =0
scoreB =0

#center show
center = turtle.Turtle()
center.penup()
center.speed(0)
center.color("White")
center.write("PONG     GAME",font=("Georgia",50,"bold"),align="center")
center.hideturtle()

#center line
line=turtle.Turtle()
line.penup()
line.clear()
line.speed(0)
line.shapesize(stretch_wid=100,stretch_len=0.01)
line.shape("square")
line.color("gray")

#Game over
game_ovr = turtle.Turtle()
game_ovr.penup()
game_ovr.clear()
game_ovr.speed(0)
game_ovr.color("Red")
game_ovr.hideturtle()
game_ovr.goto(10,-50)


#moving paddles
def left_moving_up():
    y = left_pad.ycor()
    y += 20
    if y < 260:
        left_pad.sety(y)

def left_moving_down():
    y = left_pad.ycor()
    y -= 20
    if y > -260:
        left_pad.sety(y)

def right_moving_up():
    y = right_pad.ycor()
    y+=20
    if y <260:
        right_pad.sety(y)
def right_moving_down():
    y = right_pad.ycor()
    y -=20
    if y > -260:
        right_pad.sety(y)
# def change_paddle_color(paddle):
#     original_color = paddle.color()
#     paddle.color("white")  # Change to the desired color
#     win.update()
#     turtle.ontimer(lambda: paddle.color(original_color), 200)  # Change back after 200 milliseconds


win.listen()
win.onkeypress(left_moving_up,"w")
win.onkeypress(left_moving_down,"s")
win.onkeypress(right_moving_up,"Up")
win.onkeypress(right_moving_down,"Down")


while True:
    win.update()

    #ball-movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #ball to wall collid
    #top wall
    if ball.ycor() > 290:
        ball.dy *= -1
    #bottom wall
    if ball.ycor() < -290:
        ball.dy *= -1
    #right wall
    if ball.xcor() > 390:
        ball.dx *= -1
        scoreA +=1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(scoreA,scoreB),align="center",font=("Ariel",25,"normal"))
    #left wall
    if ball.xcor() < -390:
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A:{}     Player B:{}".format(scoreA, scoreB), align="center", font=("Ariel", 25, "normal"))

    #ball to paddle collid
    if ball.xcor() > 365 and ball.ycor() < right_pad.ycor()+50 and ball.ycor() > right_pad.ycor()-50:
        ball.setx(345)
        ball.dx *= -1
        # change_paddle_color(right_pad)

    if (ball.xcor() < -370 and ball.ycor() < left_pad.ycor() + 50 and ball.ycor() > left_pad.ycor() - 50):
        ball.setx(-355)
        ball.dx *= -1
        # change_paddle_color(left_pad)

    #game over
    if scoreA == 5:
        left_pad.clear()
        left_pad.hideturtle()
        right_pad.clear()
        right_pad.hideturtle()
        ball.clear()
        ball.hideturtle()
        time.sleep(0.5)
        game_ovr.write("GAME OVER   Player A wins",font=("Georgia",30,"bold"),align="center")

    elif scoreB == 5:
        left_pad.clear()
        left_pad.hideturtle()
        right_pad.clear()
        right_pad.hideturtle()
        ball.clear()
        ball.hideturtle()
        time.sleep(0.5)
        game_ovr.write("GAME OVER   Player B wins",font=("Georgia",30,"bold"),align="center")

