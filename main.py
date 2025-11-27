# main.py

# main.py

import pygame as pg
from parameters import WINDOW, FPS
from colors import BLACK       # <-- FIXED HERE
from stars import create_stars, draw_stars
from create_bodies import create_bodies
from simulation import update_bodies


def main():
    clock = pg.time.Clock()
    run = True
    paused = False

    bodies = create_bodies()
    stars_list = create_stars()

    while run:
        clock.tick(FPS)
        WINDOW.fill(BLACK)
        draw_stars(stars_list)

        # Handle input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                elif event.key == pg.K_SPACE:
                    paused = not paused

        # Update physics if not paused
        update_bodies(bodies, paused)

        # Draw always
        for body in bodies:
            body.draw(WINDOW, track=True)

        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()
