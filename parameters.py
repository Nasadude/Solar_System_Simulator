# parameters.py

import pygame as pg

pg.init()

# ---- Physics Constants ----
AU = 1.496e11
G = 6.6743e-11
TIME_STEP = 24 * 3600
SCALE = 250 / AU

# ---- Screen ----
screen_info = pg.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

# ---- Window ----
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Solar System Simulator")

# ---- Fonts ----
NAME_TEXT = pg.font.SysFont(name="TimesRoman", size=18, bold=True)
DIST_TEXT = pg.font.SysFont(name="Sans", size=18, bold=True)

# ---- FPS ----
FPS = 60
