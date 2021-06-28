import turtle
import time
import random

speed = 0.15

window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 100)
head.direction = 'stop'
head.shapesize(0.80, 0.80)

cherry = turtle.Turtle()
cherry.speed(0)
cherry.shape('circle')
cherry.color('red')
cherry.penup()
cherry.goto(0, 0)
cherry.shapesize(0.80, 0.80)

tails = []
score = 0

text = turtle.Turtle()
text.speed(0)
text.shape('square')
text.color('white')
text.penup()
text.goto(0, 260)
text.hideturtle()
text.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)


def goUp():
      if head.direction != 'down':
          head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'

window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')

while True:
    window.update()

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        for tail in tails:
            tail.goto(1000, 1000)

        tails = []
        score = 0
        text.clear()
        text.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))

        speed = 0.15

    if head.distance(cherry) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        cherry.goto(x, y)

        score = score + 10
        text.clear()
        text.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))

        speed = speed - 0.001

        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('white')
        newTail.shapesize(0.80, 0.80)
        newTail.penup()
        tails.append(newTail)

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i -1].xcor()
        y = tails[i -1].ycor()
        tails[i].goto(x, y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

    move()

    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            score = 0
            text.clear()
            text.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))
            speed = 0.15

    time.sleep(speed)

