import pygame

LIGHT_BROWN = (240, 220, 130)
DARK_BROWN = (138, 51, 36)
QUEEN_IMAGE = pygame.image.load("queen.png")


def is_even(num):
    return num % 2 == 0


class Tile(object):
    def __init__(self, coordinate, width, height):
        self.coordinate = coordinate
        self.pos = (int(coordinate // 8), int(coordinate % 8))
        self.is_empty = True
        self.width = width
        self.height = height

    def put_queen(self):
        if self.is_empty:
            self.is_empty = False

    def remove_queen(self):
        if not self.is_empty:
            self.is_empty = True

    def draw(self, win):
        row, col = self.pos
        if is_even(row):
            color = DARK_BROWN if not is_even(self.coordinate) else LIGHT_BROWN
        else:
            color = LIGHT_BROWN if not is_even(self.coordinate) else DARK_BROWN
        rect = (col*self.width/8, row*self.height/8, self.width/8, self.height/8)
        pygame.draw.rect(win, color, rect)
        if not self.is_empty:
            win.blit(QUEEN_IMAGE, (col*self.height/8+5, row*self.width/8+5))
