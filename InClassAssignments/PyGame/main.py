import pygame as pg
from random import randint
from InClassAssignments.PyGame.library import Collectible, save
from colors import *
from os.path import exists
pg.init()

if exists('highscore'):
    with open('highscore.txt', 'r') as file:
        highscore = file.read()






winlength = 1000
winheight = 800
win = pg.display.set_mode((winlength, winheight))


clock = pg.time.Clock()

# collectibles = [
#     Collectible(randint(30, winlength - 30), randint(100, winheight -30)),
#     Collectible(randint(30, winlength - 30), randint(100, winheight -30)),
#     Collectible(randint(30, winlength - 30), randint(100, winheight -30)),
#     Collectible(randint(30, winlength - 30), randint(100, winheight -30)),
#     Collectible(randint(30, winlength - 30), randint(100, winheight -30)),
# ]

collectibles = []
collectibles_needed = randint(5,10)

for i in range(collectibles_needed):
    collectibles.append(
        Collectible(randint(30, winlength - 30), randint(100, winheight - 30)))


run = True
cube_length = 50
cube_height = 50
x = 20
y = 20
collectibles_collected = 0
time_limit = 5 + 0.5*collectibles_needed # sec = num_of_frames / 60
num_of_frames = 0
collectibles_left = collectibles_needed - collectibles_collected
while run:
    if collectibles_left == 0:
        n = len(collectibles) + 1
        time_limit += 0.5*n

        collectibles = []

        for i in range(n):
            collectibles.append(
                Collectible(
                    randint(30, winlength - 30), randint(100, winheight - 30)))
        collectibles_left = n


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
    time_left = time_limit - int(num_of_frames / 60)
    if time_left <= 0:
        font = pg.font.SysFont("comicsans", 48, bold=True)
        game_over = font.render("GAME OVER", True, RED)
        start_over = font.render("Press Enter to play again", True, GREEN)
        score = font.render(f"Your score: {collectibles_collected} / {collectibles_needed}", True, WHITE)
        win.blit(game_over, (250, 250))
        win.blit(score, (200, 350))
        win.blit(start_over, (250, 450))
        if keys[pg.K_RETURN]:
            collectibles = []
            collectibles_needed = randint(5, 10)
            collectibles_collected = 0
            collectibles_left = collectibles_needed
            for i in range(collectibles_needed):
                collectibles.append(
                    Collectible(randint(30, winlength - 30), randint(100, winheight - 30)))
            num_of_frames = 0
            time_left = time_limit



    else:
        for collectible in collectibles:
            collectible.draw(win, MAGENTA)
            if collectible.is_overlapping(x, y, x  + cube_length, y + cube_height):
                collectibles_collected += 1
                collectibles_left -= 1



        cube = pg.draw.rect(
            win,
            LIME,
            (x,y,cube_length,cube_height),
            border_radius=5

        )

        font = pg.font.SysFont("comicsans", 30, bold = True)
        text_collectibles_collected = font.render(f"Collectibles collected: {collectibles_collected} / {collectibles_needed}", True, WHITE)
        win.blit(text_collectibles_collected, (550, 25))

        time_caption = font.render(f"Time left: {time_left}", True, WHITE)
        win.blit(time_caption, (550, 55))
        num_of_frames += 1

    clock.tick(60)
    pg.display.update()
highscore = 10
if not exists('highscore.txt'):
    save(highscore, "highscore.txt")
pg.quit()