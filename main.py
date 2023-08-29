import turtle
import re

window = turtle.Screen()
WIN_WIDTH = 800
WIN_HEIGHT = 800
window.setup(width=WIN_WIDTH, height=WIN_HEIGHT)
AXIS_DRAW_1 = turtle.Turtle()
AXIS_DRAW_1.speed(0)
AXIS_DRAW_1.hideturtle()
AXIS_DRAW_2 = turtle.Turtle()
AXIS_DRAW_2.speed(0)
AXIS_DRAW_2.hideturtle()
POLY_DRAW_TURTLE_1 = turtle.Turtle()
POLY_DRAW_TURTLE_1.speed(0)
POLY_DRAW_TURTLE_1.color("BLUE")
POLY_DRAW_TURTLE_2 = turtle.Turtle()
POLY_DRAW_TURTLE_2.speed(0)
UNIT_DRAW = turtle.Turtle()
UNIT_DRAW.hideturtle()
ARROW_DRAW = turtle.Turtle()
ARROW_DRAW.hideturtle()
LIMIT_X = WIN_WIDTH*2
LIMIT_Y = WIN_HEIGHT*2
UNIT_S = 15
input = turtle.textinput("Enter an equation", "")
RANGE = float(5)
print(input)

def polynomial():
    coordinates = []
    step = 0.1
    i = -RANGE
    while(i <= RANGE):
        x = i
        X_VALUE = {'x':i}
        CONV_INPUT = input.replace('^', '**')
        CONV_INPUT = re.sub(r"(\d+)x", r"1*x", CONV_INPUT)
        Y_VALUE = eval(CONV_INPUT, X_VALUE)
        if Y_VALUE < LIMIT_X:
            coordinates.append((x * UNIT_S, Y_VALUE * UNIT_S))
            i += step
    return coordinates

cord = polynomial()
print (cord)

def drawPolyfun():
    POLY_DRAW_TURTLE_1.goto(cord[0])
    POLY_DRAW_TURTLE_1.clear()
    for x, y in cord:
        move_x = x + 1
        move_y = y + 1
        POLY_DRAW_TURTLE_1.goto(move_x, move_y)


def drawUnitsX(x):
    for i in range(x*UNIT_S, x*LIMIT_X, x*UNIT_S):
            UNIT_DRAW.penup()
            UNIT_DRAW.goto(i, 0)
            UNIT_DRAW.pendown()
            UNIT_DRAW.goto(i, 10)

def drawUnitsY(y):
    for i in range(y*UNIT_S, y*LIMIT_Y, y*UNIT_S):
            UNIT_DRAW.penup()
            UNIT_DRAW.goto(0, i)
            UNIT_DRAW.pendown()
            UNIT_DRAW.goto(-10, i)

def drawAxis_x():
    global WIN_WIDTH, WIN_HEIGHT, UNIT_S
    AXIS_DRAW_1.penup()
    AXIS_DRAW_1.goto(LIMIT_X, 0)
    AXIS_DRAW_1.pendown()
    AXIS_DRAW_1.goto(0, 0)
    AXIS_DRAW_1.goto(-LIMIT_Y, 0)
    drawUnitsX(1)
    drawUnitsX(-1)

def drawAxis_y():
    global WIN_HEIGHT, WIN_WIDTH, UNIT_S
    AXIS_DRAW_2.penup()
    AXIS_DRAW_2.goto(0, LIMIT_Y)
    AXIS_DRAW_2.pendown()
    AXIS_DRAW_2.goto(0, 0)
    AXIS_DRAW_2.goto(0, -LIMIT_X)
    drawUnitsY(1)
    drawUnitsY(-1)

drawAxis_x()
drawAxis_y()
drawPolyfun()

window.mainloop()
turtle.done()