from colors import *
import pygame as pg


class Collectible:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True


    def draw(self, win, color):
        if self.visible:
            pg.draw.circle(
                win,
                color,
                (self.x, self.y),
                15
            )

    def is_overlapping(self, x1, y1, x2, y2):
        left_edge = self.x - 15
        right_edge = self.x + 15
        top_edge = self.y - 15
        bottom_edge = self.y + 15

        if self.visible and (x1 <= left_edge <= x2 or x1 <= right_edge <= x2):
            if y1 <= top_edge <= y2 or y1 <= bottom_edge <= y2:
                print(f"Collision {self.x}, {self.y}")
                self.visible = False
                return True
        return False


def save(x: int, file: str):
    with open(file, 'w') as f:
        f.write(str(x))
