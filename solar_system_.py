# solar_system.py

import math
import pygame as pg
from parameters import WIDTH, HEIGHT, AU, G, TIME_STEP, SCALE, NAME_TEXT, DIST_TEXT
from colors import NAME_TEXT_COLOR, DIST_TEXT_COLOR, SUN_NAME_COLOR

class SolarSystemBodies:

    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius

        self.x_vel = 0
        self.y_vel = 0
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

    # Draw body
    def draw_body(self, WINDOW):
        x = self.x * SCALE + WIDTH // 2
        y = self.y * SCALE + HEIGHT // 2

        pg.draw.circle(WINDOW, self.color, (x, y), self.radius)

        # Planet labels
        if not self.sun:
            name_text = NAME_TEXT.render(self.name, True, NAME_TEXT_COLOR)
            WINDOW.blit(name_text, (x - 40, y - 55))

            dist_text = DIST_TEXT.render(
                f"{round(self.distance_to_sun/(3e8*60), 3)} lt/min",
                True, DIST_TEXT_COLOR
            )
            WINDOW.blit(dist_text, (x - 40, y - 35))

        # Sun labels
        else:
            name_text = NAME_TEXT.render(self.name, True, SUN_NAME_COLOR)
            WINDOW.blit(name_text, (x - 40, y - 75))

            dist_text = DIST_TEXT.render(
                f"{round(self.x/3e8, 3)}, {round(self.x/3e8, 3)} lt-sec",
                True, DIST_TEXT_COLOR
            )
            WINDOW.blit(dist_text, (x - 40, y - 55))

    # Force between bodies
    def gravitational_force(self, other):
        x_diff = other.x - self.x
        y_diff = other.y - self.y

        distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(y_diff, x_diff)

        return force * math.cos(theta), force * math.sin(theta)

    # Update position
    def update_position(self, bodies):
        net_fx = net_fy = 0

        for other in bodies:
            if self != other:
                fx, fy = self.gravitational_force(other)
                net_fx += fx
                net_fy += fy

        self.x_vel += net_fx / self.mass * TIME_STEP
        self.y_vel += net_fy / self.mass * TIME_STEP

        self.x += self.x_vel * TIME_STEP
        self.y += self.y_vel * TIME_STEP

        self.orbit.append((self.x, self.y))

    # Track orbit line
    def track_orbit(self, WINDOW):
        if len(self.orbit) > 1:
            points = [
                (x * SCALE + WIDTH // 2, y * SCALE + HEIGHT // 2)
                for x, y in self.orbit
            ]
            pg.draw.lines(WINDOW, self.color, False, points, 2)

    # Combined draw method
    def draw(self, WINDOW, track=True):
        self.draw_body(WINDOW)
        if track:
            self.track_orbit(WINDOW)
