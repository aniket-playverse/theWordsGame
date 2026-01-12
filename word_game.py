import turtle
import random
import time

#Screen
screen=turtle.Screen()
screen.title("Word Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

#words
words=["AMAZON","MESHO","AMAZING","CRYPTOGRAPHY"]
current_word=random.choice(words)
letter_index=0

#Score
score=0

pen=turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0,260)
pen.write(f"{current_word}", align="center", font=("Arial", 20, "bold"))

#Snake Head
head=turtle.Turtle()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction="stop"

segments=[]

#Characters
letter=turtle.Turtle()
letter.hideturtle()
letter.penup()
letter.color("red")

def draw_letter():
    letter.clear()
    x=random.randint(-280,280)
    y=random.randint(-280,280)
    letter.goto(x,y)
    letter.write(current_word[letter_index], align="center", font=("courier", 30, "bold"))
draw_letter()

#movement
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

#Keyboard
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

#Game loop
while True:
    screen.update()
    move()

    if head.distance(letter)<20:
        new_seg=turtle.Turtle()
        new_seg.shape("square")
        new_seg.color("yellow")
        new_seg.penup()
        new_seg.goto(head.xcor(),head.ycor())
        segments.append(new_seg)
        letter_index+=1

        #word chek
        if letter_index==len(current_word):
            score+=1
            current_word=random.choice(words)
            letter_index=0
            pen.clear()
            pen.write(f"Word: {current_word} Score :{score}",align="center", font=("courier", 20, "bold"))
        draw_letter()
    #Movement of body
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if segments:
        segments[0].goto(head.xcor(),head.ycor())

    #wall hitting
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
        print("Game Over")
        screen.bye()
        break

    #self collision
    for seg in segments[1:]:
        if seg.distance(head) < 20:
            print("Game Over")
            screen.bye()
            exit()

    time.sleep(0.1)