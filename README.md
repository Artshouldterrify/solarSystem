# A 2-D simulation of a Solar System.
***

This repository showcases a 2-D sim of a solar system using the `turtle` library 
to visually present this simulation. This simulation structure is further used to find stable 
orbits for an arbitrary binary Solar System using the **genetic algorithm**.

### 1. `solarSystem` and `solarSystemBody`
This module is used for the visual simulation of the Solar System. It consists of two classes: 
`solarSystemBody` and `solarSystem`. Definitions for both of these classes and related child classes
are contained in `solarSystem.py`.

The `solarSystem` class represents the screen on which the simulation takes place.
It can be initialized as `solarSystem(width, height)`, with the width and height parameters
denoting the same properties of the simulation screen.

```python
import solarSystem as drawingScript
import time
import turtle


# main
solar_sys_draw = drawingScript.solarSystem(1600, 1000)
```

All bodies within the system (objects of the `solarSystemBody` class) are contained within the 
object instance's `inst.bodies` attribute. The method `inst.add_body(body)` can be used to add
an object `body` of the `solarSystemBody` class to the current system, while the method `inst.remove_body(body)`
similarly removes the object `body` from the current system. We can use the `inst.update_bodies()`
method to update the current positions and velocities of each body to the screen and the `inst.interactions()` method
to calculate positions and velocities for the next discrete interval of time.

The `solarSystemBody` class is used to represent each body within the system i.e. Suns, Planets or Asteroids.
Each of these objects is a `Turtle` from the `turtle` library and traces its path across the screen.

An object of this class is initialized as `solarSystemBody(solar_system, mass, position=(0, 0), velocity=(0, 0))`,
where `solar_system` is an object of the `solarSystem` class and `mass`, `position` and 
`velocity` are the same-named properties of our created body. 

To specifically generate Suns and Planets respectively, we can use child classes of `solarSystemBody`, 
`sun` and `planet`. Both are initialized in exactly the same way, and only differ in the colour and size scaling of
the created object.

```python
draw_suns = (drawingScript.sun(solar_sys_draw, mass=10_000, position=(0, 0), velocity=(0, 0)))
draw_planets = (drawingScript.planet(solar_sys_draw, mass=5, position=(100, 0), velocity=(0, 9.5)),
                drawingScript.planet(solar_sys_draw, mass=15, position=(300, 0), velocity=(0, -6)),
                drawingScript.planet(solar_sys_draw, mass=20, position=(0, 450), velocity=(-4.8, 0)))
```

We run the simulation by defining the variable `max_tick` denoting the number of ticks for which
the simulation will run. For each tick, the variable `tick` is incremented until it reaches `max_tick` while calculating
the positions of the bodies for the next tick using `inst.interactions` and the screen in updated using 
`inst.update_bodies`.

(**Note:** We use `time.sleep(0.01)` to slightly slow down the animation to make it more visible.)
```python
tick = 0
max_tick = 2_000
while tick < max_tick:
    tick += 1
    time.sleep(0.01)
    solar_sys_draw.interactions()
    solar_sys_draw.update_bodies()
turtle.done()
```
![sim]()
***

### 2. `solar_body` and `solar_system` classes.

Both of these classes are conceptually identical to `solarSystemBody` and `solarSystem`, except 
that they do not _actually_ simulate the system on the screen but only mathematically simulate
the positions and velocities of the system as it evolves.

Objects of both classes are initialized similar to `solarSystemBody` and `solarSystem`.

`inst.add_body(body)`, `inst.remove_body(body)`, `inst.interactions()`, `inst.update_bodies` all work
in an identical manner, except `body` is now an object of the `solar_body` class.

The only addition is the `inst.simulate()` method, which mathematically simulates the system and is
used in [finding stable orbits via the genetic algorithm](). This method returns the number of ticks for 
which the system existed without collision.