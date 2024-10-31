import pygame as pg
from colors import *
pg.init()

win = pg.display.set_mode((1000, 800))


clock = pg.time.Clock()


run = True

x = 0
y = 0


while run:
    win.fill(OCEAN)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                x += 5
            elif event.key == pg.K_a:
                x-= 5
            if event.key == pg.K_w:
                y -= 5
            elif event.key == pg.K_s:
                y += 5

    rect = pg.draw.rect(
        win,
        LIME,
        (x,y,50,50)
    )
    clock.tick(60)
    pg.display.update()

pg.quit()