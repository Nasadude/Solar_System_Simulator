# 🌌 Solar System Simulator (Pygame, Physics-Based)

A fully-interactive, physics-accurate 2D Solar System simulation built using **Python + Pygame**.
Bodies interact through **Newtonian gravity**, orbits are plotted over time, stars are rendered as a moving background, and the system architecture is fully modular.

This project implements real physics:

* **G = 6.6743e-11**
* **AU scaling**
* **Velocity-based orbital motion**
* **Distance-to-sun display (light minutes / light seconds)**

The codebase is cleanly divided into separate modules for maintainability.

---

# 📁 Project Structure

```
solar-system-simulator/
│
├── main.py
├── parameters.py
├── colors.py
├── stars.py
├── solar_system_.py
├── create_bodies.py
├── simulation.py
└── README.md
```
Other options
|-- RK4 - solar_system_RK4_NASA.py
---

# 📌 Module Breakdown

### **main.py**

Runs the simulator:

* Initializes Pygame
* Loads stars & planets
* Handles pause / quit events
* Calls simulation & render functions
* Main game loop

---

### **parameters.py**

Stores all global configuration:

* Window size
* FPS settings
* Astronomical Unit (AU)
* Gravitational constant
* Pygame font loaders
* Time-step settings
* Constants used across the project

---

### **colors.py**

Simple module defining RGB colors:

```python
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
YELLOWISH_WHITE = (255, 255, 246)
BLUE = (0, 0, 255)
RED = (188, 39, 50)

NAME_TEXT_COLOR = (111, 236, 123)
DIST_TEXT_COLOR = (56, 190, 255)

SUN_NAME_COLOR = (144, 128, 254)
SUN_TEXT_COLOR = (54, 32, 12)
```

---

### **solar_system_.py**

Contains the **SolarSystemBodies** class:

* Draw body & label
* Draw distance text
* Calculate gravitational force
* Update velocity & position
* Track orbit path
* Draw orbit path

Physics uses:

```
F = G * m1 * m2 / r²
v = v + a·dt
x = x + v·dt
```

---

### **stars.py**

Handles star field:

* Random generation of 400–500 stars
* Star colors randomized
* Efficient draw routine

---

### **create_bodies.py**

Creates actual solar system objects:

* Sun
* Mercury
* Venus
* Earth
* Mars
* (Optional) Moon
* Sets initial velocity for stable orbits

Example:

```python
earth = SolarSystemBodies("Earth", BLUE, 1 * AU, 0, 5.97e24, 15)
earth.y_vel = -29.8e3
```

---

### **simulation.py**

Provides:

* `update_bodies()`
* Pause logic helpers
* Wrapper around body.update_position()

---

# 🎮 Controls

| Key          | Action                                                       |
| ------------ | ------------------------------------------------------------ |
| **SPACE**    | Pause / Resume simulation                                    |
| **ESC**      | Quit                                                         |

---

# 🪐 Features

✔ Real gravitational physics
✔ True orbital speeds
✔ Adjustable time-step
✔ Orbit trails
✔ Light-minute / light-second distance display
✔ Stars background
✔ Smooth motion at 60 FPS
✔ Modular architecture
✔ Easy to extend (add Jupiter, Saturn, Moon, etc.)

---

# 🚀 Installation & Run

### 1. Install Python packages

```bash
pip install pygame
```

### 2. Run the simulator

```bash
python main.py
```

