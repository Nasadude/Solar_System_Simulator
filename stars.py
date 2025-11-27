# stars.py

import pygame as pg
from random import randint
from parameters import WIDTH, HEIGHT, WINDOW

def create_stars(num=450):
    return [
        {
            'color': (randint(190, 255), randint(190, 255), randint(190, 255)),
            'center': (randint(5, WIDTH - 5), randint(5, HEIGHT - 5)),
            'radius': randint(1, 2)
        }
        for _ in range(num)
    ]

def draw_stars(stars_list):
    for star in stars_list:
        pg.draw.circle(WINDOW, star['color'], star['center'], star['radius'])
