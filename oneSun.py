import solarSystem as drawingScript
import time
import turtle


# main
solar_sys_draw = drawingScript.solarSystem(1600, 1050)
draw_suns = (drawingScript.sun(solar_sys_draw, mass=10_000, position=(0, 0), velocity=(0, 0)))
draw_planets = (drawingScript.planet(solar_sys_draw, mass=5, position=(100, 0), velocity=(0, 9.5)),
                drawingScript.planet(solar_sys_draw, mass=15, position=(300, 0), velocity=(0, -6)),
                drawingScript.planet(solar_sys_draw, mass=20, position=(0, 450), velocity=(-4.8, 0)))
tick = 0
max_tick = 2_000
while tick < max_tick:
    tick += 1
    time.sleep(0.01)
    solar_sys_draw.interactions()
    solar_sys_draw.update_bodies()
turtle.done()
