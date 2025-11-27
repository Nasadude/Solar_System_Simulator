# simulation.py

def update_bodies(bodies, paused):
    if not paused:
        for body in bodies:
            body.update_position(bodies)
