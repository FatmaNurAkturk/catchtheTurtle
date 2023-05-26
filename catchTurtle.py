import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT= ("Arial",15,"normal")
score = 0
gameOver = False

turtleList = []

#score turtle
scoreTurtle = turtle.Turtle()

#countdown turtle
countdownTurtle = turtle.Turtle()

def setupScoreTurtle():
    scoreTurtle.hideturtle() # turtle gizlemek
    scoreTurtle.color("dark blue")
    scoreTurtle.penup() # çizmesini engelle

    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    scoreTurtle.setpos(0, y)
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)

gridSize = 10
def makeTurtle(x, y):
    t = turtle.Turtle()

    def handleClick(x, y):
        global score
        score +=1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
        #print(x, y)

    t.onclick(handleClick)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.setposition(x * gridSize, y * gridSize)
    turtleList.append(t)

xCoordinates = [-20,-10,0,10,20]
yCoordinates = [20,10,0,-10,-20]

def setupTurtles():
    for x in xCoordinates:
        for y in yCoordinates:
            makeTurtle(x,y)

def hideTurtles():
    for t in turtleList:
        t.hideturtle()

#recursive function
def showTurtleRandomly():
    if not gameOver:
        hideTurtles()
        random.choice(turtleList).showturtle()
        screen.ontimer(showTurtleRandomly, 500)

def countdown(time):
    global gameOver
    countdownTurtle.hideturtle()  # turtle gizlemek
    countdownTurtle.color("dark blue")
    countdownTurtle.penup()  # çizmesini engelle

    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    countdownTurtle.setpos(0, y - 30)
    countdownTurtle.clear()
    if time > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)
    else:
        gameOver = True
        countdownTurtle.clear()
        hideTurtles()
        countdownTurtle.write(arg="GAME OVER! ", move=False, align="center", font=FONT)

def startGameUp():
    turtle.tracer(0) # takip etmeyi bırak
    setupScoreTurtle()
    setupTurtles()
    hideTurtles()
    showTurtleRandomly()
    countdown(10)
    turtle.tracer(1) # takip etmeye başlat

startGameUp()
turtle.mainloop()