# ---------------------------------------------------------
# INNER SOLAR SYSTEM – COLORS FROM JSON – RK4 ORBITS
# ---------------------------------------------------------

import pygame as pg
import math
import json
from random import randint

pg.init()

WIDTH, HEIGHT = 1600, 900
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Inner Solar System – RK4 Stable Orbits")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FONT = pg.font.SysFont("Arial", 22)

# ---------------------------------------------------------
# STARFIELD
# ---------------------------------------------------------
STAR_COUNT = 450
STARS = [
    (
        randint(0, WIDTH),
        randint(0, HEIGHT),
        randint(1, 2),
        (randint(180, 255), randint(180, 255), randint(180, 255))
    )
    for _ in range(STAR_COUNT)
]

def draw_stars():
    for x, y, r, c in STARS:
        pg.draw.circle(WINDOW, c, (x, y), r)

# ---------------------------------------------------------
# LOAD PLANET COLORS FROM JSON
# ---------------------------------------------------------
def load_colors(path):
    with open(path) as f:
        raw = json.load(f)

    colors = {}

    for name, value in raw.items():
        # If hex format
        if isinstance(value, str) and value.startswith("#"):
            value = value.lstrip("#")
            colors[name] = (
                int(value[0:2], 16),
                int(value[2:4], 16),
                int(value[4:6], 16)
            )
        else:
            # assume RGB list [R,G,B]
            colors[name] = tuple(value)

    return colors

PLANET_COLORS = load_colors("planet_colors.json")

# ---------------------------------------------------------
# LOAD PLANET DATA FROM JSON
# ---------------------------------------------------------
PLANETS_TO_LOAD = ["MERCURY", "VENUS", "EARTH", "MARS"]

def load_planetary_data(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    planets = {}

    for key, entry in data.items():
        if key.upper() not in PLANETS_TO_LOAD:
            continue

        name = key.capitalize()

        planets[name] = {
            "mass": entry["Mass_10^24kg"] * 1e24,
            "distance": entry["Distance_from_Sun_10^6_km"] * 1e6 * 1000,
            "velocity": entry["Orbital_Velocity_km_s"] * 1000
        }

    return planets

# ---------------------------------------------------------
# BODY CLASS WITH RK4 INTEGRATOR
# ---------------------------------------------------------
class Body:
    AU = 1.496e11
    G = 6.67430e-11
    SCALE = 180 / AU      # View scaling
    DT = 0.25 * 86400     # 0.25 days per frame

    def __init__(self, name, x, y, mass, color, vx=0, vy=0):
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.color = color
        self.x_vel = vx
        self.y_vel = vy
        self.orbit = []

    def acceleration(self, x, y, bodies):
        ax = ay = 0
        for other in bodies:
            if other is self:
                continue

            dx = other.x - x
            dy = other.y - y
            r2 = dx*dx + dy*dy
            if r2 < 1e7:
                continue

            r = math.sqrt(r2)
            a = Body.G * other.mass / r2

            ax += a * dx / r
            ay += a * dy / r

        return ax, ay

    def update(self, bodies):
        h = Body.DT

        ax1, ay1 = self.acceleration(self.x, self.y, bodies)
        k1vx, k1vy = ax1, ay1
        k1x, k1y = self.x_vel, self.y_vel

        ax2, ay2 = self.acceleration(self.x + 0.5*h*k1x,
                                     self.y + 0.5*h*k1y, bodies)
        k2vx, k2vy = ax2, ay2
        k2x = self.x_vel + 0.5*h*k1vx
        k2y = self.y_vel + 0.5*h*k1vy

        ax3, ay3 = self.acceleration(self.x + 0.5*h*k2x,
                                     self.y + 0.5*h*k2y, bodies)
        k3vx, k3vy = ax3, ay3
        k3x = self.x_vel + 0.5*h*k2vx
        k3y = self.y_vel + 0.5*h*k2vy

        ax4, ay4 = self.acceleration(self.x + h*k3x,
                                     self.y + h*k3y, bodies)
        k4vx, k4vy = ax4, ay4
        k4x = self.x_vel + h*k3vx
        k4y = self.y_vel + h*k3vy

        self.x += (h/6)*(k1x + 2*k2x + 2*k3x + k4x)
        self.y += (h/6)*(k1y + 2*k2y + 2*k3y + k4y)
        self.x_vel += (h/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
        self.y_vel += (h/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)

        self.orbit.append((self.x, self.y))
        if len(self.orbit) > 1400:
            self.orbit.pop(0)

    def draw(self):
        sx = self.x * Body.SCALE + WIDTH / 2
        sy = self.y * Body.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            pts = [(x * Body.SCALE + WIDTH/2, y * Body.SCALE + HEIGHT/2) for x, y in self.orbit]
            pg.draw.lines(WINDOW, WHITE, False, pts, 1)

        pg.draw.circle(WINDOW, self.color, (int(sx), int(sy)), 10)

        txt = FONT.render(self.name, True, WHITE)
        WINDOW.blit(txt, (sx - txt.get_width()/2, sy + 18))

# ---------------------------------------------------------
# SYSTEM CREATION
# ---------------------------------------------------------
def create_system():
    data = load_planetary_data("planetary_fact_sheet.json")
    bodies = []

    sun = Body("Sun", 0, 0, 1.989e30, PLANET_COLORS["Sun"])
    bodies.append(sun)

    for name, p in data.items():
        x = p["distance"]
        vx = 0
        vy = -p["velocity"]
        body = Body(name, x, 0, p["mass"], PLANET_COLORS[name], vx, vy)
        bodies.append(body)

    return bodies

# ---------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------
clock = pg.time.Clock()
bodies = create_system()

running = True
while running:
    WINDOW.fill(BLACK)
    draw_stars()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    for b in bodies:
        b.update(bodies)
        b.draw()

    pg.display.update()
    clock.tick(60)

pg.quit()
