##########
#  My turtle art
#  
#  Matthew Eng
#  Nov. 9, 2022
#  Objective: Create drawings using 'turtle' while following specific guidelines
#           - at least: 4 functions (2 non-fruitful), 3 loops (1 while), contain 'MAT6'

import turtle
import random

# Functions #
# Random Color Generators
def randomDogColor():
    bodyC = (230/255,random.randint(110,150)/255,random.randint(1,10)/255)
    limbC = (204/255,random.randint(100,130)/255,random.randint(1,10)/255)
    return bodyC, limbC

def randomGrassColor():
    clist = [[80,200,120],[95,133,117],[34,139,34],[76,187,23],[53,94,59]]
    cRan = []
    for elm in random.choice(clist):
        cRan.append(elm/255)

    return tuple(cRan)

# Background 
def setBackground(wScrn,hScrn):
    t.pensize(1)
    r = (255)/255
    g = (230)/255
    b = (140)/255
    for row in range((hScrn//2),(hScrn//2-int(hScrn/1.75)),-1):
        t.color(r,g,b)
        t.penup()
        t.goto(-wScrn//2,row)
        t.setheading(0)
        t.pendown()
        t.forward(wScrn)
        g-=(125/int(hScrn/1.75)/255)
        b-=(45/int(hScrn/1.75)/255)
    
    for row in range((hScrn//2-int(hScrn/1.75)),(-hScrn//2),-1):
        t.color(141/255,180/255,30/255)
        t.penup()
        t.goto(-wScrn//2,row)
        t.setheading(0)
        t.pendown()
        t.forward(wScrn)

# Animals and Grass
def dogFigure(tongueC,earC,eyeC,pupilC,noseC,noseDotC,locX,locY,scale=1):

    bodyC, limbC = randomDogColor()

    # Body
    t.color(bodyC)
    t.penup()
    t.goto((locX-122*scale),(locY-120*scale))
    t.setheading(-90)
    t.pendown()
    t.begin_fill()
    t.forward(20*scale)
    t.circle(75*scale,180)
    t.forward(20*scale)
    t.circle(75*scale,180)
    t.end_fill()

    # Head
    t.color(limbC)
    t.pensize(7*scale)
    t.penup()
    t.setheading(90)
    t.goto(locX,locY)
    t.pendown()
    t.begin_fill()
    t.circle(45*scale,180)
    t.right(90)
    t.goto((locX-75*scale),locY)
    t.circle(35*scale,190)
    t.setheading(0)
    t.forward(55*scale)
    t.penup()
    t.setheading(0)
    t.pendown()
    t.circle(35*scale,170)
    t.penup()
    t.end_fill()

    # Tongue
    t.color(tongueC)
    t.setheading(270)
    t.goto((locX-45*scale),(locY-60*scale))
    t.right(60)
    t.pendown()
    t.begin_fill()
    t.forward(16*scale)
    t.left(60)
    t.forward(20*scale)
    t.circle(15*scale,180)
    t.forward(20*scale)
    t.left(60)
    t.forward(16*scale)
    t.end_fill()

    #Inner detail (Tongue)
    t.color("DeepPink")
    t.pensize(5*scale)
    t.penup()
    t.goto((locX-44*scale),(locY-62*scale))
    t.setheading(270)
    t.pendown()
    t.forward(25*scale)
    t.circle(5*scale,180)
    t.penup()
    t.left(90)
    t.goto((locX-44*scale),(locY-87*scale))
    t.setheading(270)
    t.left(180)
    t.pendown()
    t.circle(5*scale,-180)

    #Right ear
    t.penup()
    t.pensize(2*scale)
    t.goto((locX+11*scale),(locY-12*scale))
    t.color(earC)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.forward(10*scale)
    t.left(60)
    t.circle(35*scale,145)
    t.end_fill()

    #Left ear
    t.penup()
    t.goto((locX-101*scale),(locY-12*scale))
    t.pendown()
    t.setheading(180)
    t.begin_fill()
    t.forward(10*scale)
    t.left(-240)
    t.circle(35*scale,-145)
    t.end_fill()

    #Eyes
    t.penup()
    t.color(eyeC)
    t.goto((locX-30*scale),(locY-20*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(10*scale,180)
    t.forward(6*scale)
    t.circle(10*scale,180)
    t.forward(6*scale)
    t.end_fill()
    
    t.penup()
    t.color(eyeC)
    t.goto((locX-80*scale),(locY-20*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(10*scale,180)
    t.forward(6*scale)
    t.circle(10*scale,180)
    t.forward(6*scale)
    t.end_fill()
    t.penup()

    # Pupils
    t.color(pupilC)
    t.goto((locX-75*scale),(locY-18*scale))
    t.begin_fill()
    t.circle(7*scale)
    t.end_fill()

    t.color(pupilC)
    t.goto((locX-28*scale),(locY-18*scale))
    t.begin_fill()
    t.circle(7*scale)
    t.end_fill()

    #Nose 
    t.color(noseC)
    t.goto((locX-55*scale),(locY-40*scale))
    t.begin_fill()
    t.circle(11*scale)
    t.end_fill()

    #Nose dots
    t.goto((locX-50*scale),(locY-37*scale))
    t.color(noseDotC)
    t.begin_fill()
    t.circle(2*scale)
    t.end_fill()
    t.goto((locX-42*scale),(locY-37*scale))
    t.color("white")
    t.begin_fill()
    t.circle(2*scale)
    t.end_fill()
    t.goto((locX-46*scale),(locY-44*scale))
    t.color("white")
    t.begin_fill()
    t.circle(2*scale)
    t.end_fill()

    #Feet
    t.penup()
    t.color(limbC)
    t.goto((locX-30*scale),(locY-200*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(20*scale,180)
    t.forward(10*scale)
    t.circle(20*scale,180)
    t.forward(10*scale)
    t.end_fill()

    t.penup()
    t.color(limbC)
    t.goto((locX-100*scale),(locY-200*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(20*scale,180)
    t.forward(10*scale)
    t.circle(20*scale,180)
    t.forward(10*scale)
    t.end_fill()
    
    #Hand
    t.penup()
    t.color(limbC)
    t.goto((locX-15*scale),(locY-125*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(16*scale,180)
    t.forward(8*scale)
    t.circle(16*scale,180)
    t.forward(8*scale)
    t.end_fill()

    t.penup()
    t.color(limbC)
    t.goto((locX-110*scale),(locY-125*scale))
    t.setheading(270)
    t.pendown()
    t.begin_fill()
    t.circle(16*scale,180)
    t.forward(8*scale)
    t.circle(16*scale,180)
    t.forward(8*scale)
    t.end_fill()
    t.penup()

def drawBirds(wScrn,hScrn):
    numBirds = 0
    numScrt = random.randint(3,20)

    while (numBirds<numScrt):
        t.pensize(3)
        t.color("black")
        t.penup()
        absWidth = int(wScrn/2.15)
        uBoundH = int(hScrn/2.15)
        lBoundH = hScrn//2-int(hScrn/1.75)
        t.goto(random.randrange(-absWidth,absWidth,1),random.randrange(lBoundH,uBoundH,1))
        t.setheading(90)
        t.pendown()
        t.circle(10,180)
        t.setheading(90)
        t.circle(10,180)
        numBirds+=1
    
    return numBirds

def drawGrass(wScrn,hScrn):
    numGrassBunch = 0
    numScrt = random.randint(5,12)

    while (numGrassBunch<numScrt):
        t.pensize(3)
        x=random.randint(-int(wScrn/2.15),int(wScrn/2.15))
        y=random.randint((-hScrn//2),(hScrn//2-int(hScrn/1.75)))
        for _ in range(0,random.randint(10,15)):
            t.pencolor(randomGrassColor())
            t.penup()
            t.goto(x,y)
            t.setheading(random.randint(60,140))
            t.pendown()
            t.circle(random.randint(-50,50),random.randint(80,120))
        numGrassBunch+=1

def drawDog():
    numScrt = random.randint(3,5)
    numDogs = 0

    while (numDogs<numScrt):
        scale = random.randint(50,100)/100
        x=random.randint(-int(wScrn/2),int(wScrn/2.15))
        y=random.randint((-hScrn//2),(-hScrn//2+int(hScrn/2)))
        dogFigure("pink","brown","black","white","black","white",x,y,scale)
        numDogs+=1
    return numDogs

# Text signature 
def drawText(wScrn,hScrn):
    # M
    t.penup()
    t.pensize(4)
    t.pencolor("black")
    t.goto(wScrn//2-120,-hScrn//2+20)
    t.setheading(90)
    t.pendown()
    t.forward(25)
    t.right(135)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.left(-135)
    t.forward(25)

    # A
    t.penup()
    t.setheading(0)
    t.forward(7)
    t.setheading(70)
    t.pendown()
    t.forward(15)

    # Cross of A
    t.setheading(0)
    t.forward(9)
    t.setheading(180)
    t.forward(9)

    t.setheading(70)
    t.forward(13)
    t.setheading(-70)
    t.forward(28)

    # T 
    t.penup()
    t.setheading(0)
    t.forward(10)
    t.left(90)
    t.pendown()
    t.forward(25)
    t.left(90)
    t.forward(9)
    t.right(180)
    t.forward(18)

    # 6
    t.penup()
    t.setheading(0)
    t.forward(20)
    t.pendown()
    t.setheading(170)
    t.circle(14,150)
    t.circle(7,310)
# End of Functions #

# Start of Program #
t = turtle.Turtle()
scrn = t.getscreen()

wScrn = scrn.window_width()
hScrn = scrn.window_height()

t.hideturtle()
t.speed(0)
turtle.tracer(False)

setBackground(wScrn=wScrn,hScrn=hScrn)
birds = drawBirds(wScrn=wScrn,hScrn=hScrn)
drawGrass(wScrn=wScrn,hScrn=hScrn)
dogs = drawDog()

turtle.tracer(True)
drawText(wScrn=wScrn,hScrn=hScrn)

print("Let's play a game, find the following: \n{} Dogs \n{} Birds".format(dogs,birds))

print("\nCode Summary")
print("Longest line: 91 Characters")
print("Number of loops: 6 (3 'while' & 3 'for')")
print("Number of functions: 8 (4 'fruitful' & 4 'non-fruitful')")
turtle.done()

# End of Program