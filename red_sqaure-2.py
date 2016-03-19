import turtle
import time


#---------------
#Create a Pen
#---------------
t = turtle.Pen()

#---------------
#Draw a red box
#---------------
t.reset()
t.color("red")
t.begin_fill()

t.forward(50)
t.left(90)

t.forward(50)
t.left(90)

t.forward(50)
t.left(90)

t.forward(50)
t.left(90)

t.end_fill()

t.penup()
t.sety(-50)
t.write ("Red Box", True, align="Center", font=("Helvetica",16,"normal"))
t.pendown()
time.sleep (1)


#-------------------------
# Same box with less steps
#-------------------------

t.reset()
t.color("red")
t.begin_fill()
for x in range (1,5):
    t.forward(50)
    t.left(90)
t.end_fill()

t.penup()
t.sety(-50)
t.write ("Red Box with Less Steps", True, align="Center", font=("Helvetica",16,"normal"))
t.pendown()
time.sleep (1)

#-------------------------
#Now Let's move the box
#-------------------------
t.reset()
t.penup()
t.sety(0)
t.setx (150)
t.pendown()
t.color("red")
t.begin_fill()
for x in range (1,5):
    t.forward(50)
    t.left(90)
t.end_fill()

t.penup()
t.sety(-50)
t.write ("Red Box Moved", True, align="Center", font=("Helvetica",16,"normal"))
t.pendown()
time.sleep (5)
