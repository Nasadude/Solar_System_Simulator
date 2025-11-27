# create_bodies.py

from solar_system_ import SolarSystemBodies
from colors import YELLOW, GRAY, YELLOWISH_WHITE, BLUE, RED
from parameters import AU

def create_bodies():
    sun = SolarSystemBodies("Sun", YELLOW, 0, 0, 1.989e30, 30)
    sun.sun = True

    mercury = SolarSystemBodies("Mercury", GRAY, 0.39 * AU, 0, 0.33e24, 6)
    mercury.y_vel = -47.4e3

    venus = SolarSystemBodies("Venus", YELLOWISH_WHITE, 0.72 * AU, 0, 4.87e24, 14)
    venus.y_vel = -35e3

    earth = SolarSystemBodies("Earth", BLUE, AU, 0, 5.97e24, 15)
    earth.y_vel = -29.8e3

    mars = SolarSystemBodies("Mars", RED, 1.52 * AU, 0, 0.642e24, 8)
    mars.y_vel = -24.1e3

    return [sun, mercury, venus, earth, mars]
