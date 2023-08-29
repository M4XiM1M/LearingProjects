import turtle as t
import time

t.screensize(canvheight=400, canvwidth=400)
t.shape('triangle')
wn = t.Screen()
wn.tracer(0)
wn.bgcolor('#A4B5C6')

color = ['#6e7f80', '#536872', '#708090', '#536878', '#36454f']
t.color(color[4], color[2])
t.pensize(10)
t.speed(1000)
min = 300-50
sec = 300-20

def goto_origin(x):
    t.penup()
    t.goto(0,0)
    t.right(x)

#To draw circle
def circle(r):
    t.begin_fill()
    t.penup()
    t.goto(0, -300)
    t.pendown()
    t.circle(r)
    t.end_fill()
    goto_origin(90)

circle(300)

#For hrs
def dw_hrs():
    for i in range (12):
        t.forward(min)
        t.pendown()
        t.forward(50)
        goto_origin(360/12)
dw_hrs()

#For Seconds
def dw_sec():
    for i in range (60):
        t.forward(sec)
        t.pendown()
        t.forward(20)
        goto_origin(360/60)
dw_sec()

t.hideturtle()

# Drawing time

t1 = t.Turtle()
t1.speed(0)
t1.shape("circle")
t1.color('#DBEDFE')
t1.pensize(6)
t1.hideturtle()

t2 = t.Turtle()
t2.speed(0)
t2.shape("circle")
t2.color('#DBEDFE')
t2.pensize(4)
t2.hideturtle()


t3 = t.Turtle()
t3.speed(0)
t3.shape("circle")
t3.color('#DBEDFE')
t3.pensize(2)
t3.hideturtle()



def drawTime(h, m, s):
    #Drawing Hours
    t1.penup()
    t1.goto(0,0)
    t1.setheading(90)
    angle = (h / 12)*360
    t1.right(angle)
    t1.pendown()
    t1.fd(180)

    # Drawing Minutes
    t2.penup()
    t2.goto(0,0)
    t2.setheading(90)
    angle = (m / 60)*360
    t2.right(angle)
    t2.pendown()
    t2.fd(150)

    #Drawing Seconds
    t3.penup()
    t3.goto(0,0)
    t3.setheading(90)
    angle = (s / 60)*360
    t3.right(angle)
    t3.pendown()
    t3.forward(250)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    drawTime(h, m, s)
    wn.update()
    time.sleep(1)
    t1.clear()
    t2.clear()
    t3.clear()
    

t.done()
