import pygame as py
import random

py.init()

WIN_WIDTH, WIN_HEIGHT = 800, 600
WIN = py.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
py.display.set_caption("Game")

x, y = WIN_WIDTH/2, WIN_HEIGHT/2
WIN_COLOR = (200, 255, 223)
SNAKE_COLOR = (0, 0, 0)
EGG_COLOR = (223, 120, 35)
WIN.fill(WIN_COLOR)
FPS = 10
RECT_X = 400
RECT_Y = 300
SNAKE_BODY = [(x, y)]
MOVE_X, MOVE_Y = 0, 0
MOVE_DISTANCE = 10
EGG_X, EGG_Y = random.randrange(10, WIN_WIDTH)//MOVE_DISTANCE*MOVE_DISTANCE-5, random.randrange(10, WIN_HEIGHT)//MOVE_DISTANCE*MOVE_DISTANCE+5
score = 0
GAME_OVER = False

def checkCollision(rect, circle):
    if rect.colliderect(circle):
        return True
    return False

def drawGame():
    global RECT_X, RECT_Y, EGG_X, EGG_Y, x, y, score, GAME_OVER
    RECT_X = (RECT_X+MOVE_X)%WIN_WIDTH
    RECT_Y = (RECT_Y+MOVE_Y)%WIN_HEIGHT
    SNAKE_BODY.append((RECT_X, RECT_Y))
    WIN.fill(WIN_COLOR)
    py.draw.rect(WIN, SNAKE_COLOR, [RECT_X, RECT_Y, 10, 10])
    for (i, j) in SNAKE_BODY:
        snake_segment = py.draw.rect(WIN, SNAKE_COLOR, [i, j, 10, 10])

    egg = py.draw.circle(WIN, EGG_COLOR, (EGG_X, EGG_Y), 5)
    if checkCollision(snake_segment, egg):
        EGG_X, EGG_Y = random.randrange(0, WIN_WIDTH)//MOVE_DISTANCE*MOVE_DISTANCE, random.randrange(0, WIN_HEIGHT)//MOVE_DISTANCE*MOVE_DISTANCE
        score += 1
        print(score)
    else:
        del SNAKE_BODY[0]
    
    py.display.update()

def game():
    global MOVE_X, MOVE_Y, MOVE_DISTANCE, FPS
    frame = py.time.Clock()
    running = True
    ARROW_HOLD = False
    while running:
        frame.tick(FPS)
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                running = False
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    if (MOVE_X != MOVE_DISTANCE):
                        MOVE_X = -MOVE_DISTANCE
                    MOVE_Y = 0
                    ARROW_HOLD = True
                elif event.key == py.K_RIGHT:
                    if (MOVE_X != -MOVE_DISTANCE):
                        MOVE_X = MOVE_DISTANCE
                    MOVE_Y = 0
                    ARROW_HOLD = True
                elif event.key == py.K_UP:
                    MOVE_X = 0
                    ARROW_HOLD = True
                    if (MOVE_Y != MOVE_DISTANCE):
                        MOVE_Y = -MOVE_DISTANCE
                elif event.key == py.K_DOWN:
                    MOVE_X = 0
                    ARROW_HOLD = True
                    if (MOVE_Y != -MOVE_DISTANCE):
                        MOVE_Y = MOVE_DISTANCE
                else:
                    continue
                drawGame()
                py.display.update()

            elif event.type == py.KEYUP:
                if event.key == py.K_LEFT:
                    ARROW_HOLD = False
                elif event.key == py.K_RIGHT:
                    ARROW_HOLD = False
                elif event.key == py.K_UP:
                    ARROW_HOLD = False
                elif event.key == py.K_DOWN:
                    ARROW_HOLD = False
        if ARROW_HOLD:
            FPS+=2
        if not ARROW_HOLD:
            FPS = 20
        if not events:
            drawGame()
            py.display.flip()
    

if __name__ == "__main__":
    game()
