import pygame as pg
from random import randint
from InClassAssignments.PyGame.library import Collectible
from colors import *
pg.init()


winlength = 1000
winheight = 800
win = pg.display.set_mode((winlength, winheight))


clock = pg.time.Clock()

collectibles = [
    Collectible(100, randint(300,500)),
    Collectible(300, randint(300, 700)),
    Collectible(500, randint(100, 300)),
    Collectible(700,randint(100, 700)),
    Collectible(450,randint(600, 800)),
]

run = True
rect_length = 50
rect_height = 50
x = 20
y = 20
collectibles_collected = 0

while run:
    win.fill(OCEAN)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    keys = pg.key.get_pressed()

    if keys[pg.K_d]:
        if x <= winlength -55:
            x += 5

    elif keys[pg.K_a]:
        if x >= 5:

            x-= 5


    if keys[pg.K_w]:
        if y >= 5:
            y -= 5
    elif keys[pg.K_s]:
        if y <= winheight - 55:

            y += 5

    for collectible in collectibles:
        collectible.draw(win, MAGENTA)
        collectible.is_overlapping(x, y, x  + rect_length, y + rect_height)




    rect = pg.draw.rect(
        win,
        LIME,
        (x,y,rect_length,rect_height)
    )
    clock.tick(60)
    pg.display.update()
print("Collectibles collected: ", collectibles_collected)
pg.quit()