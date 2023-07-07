import solarSystem as drawingScript
import time
import turtle

# main
run = [13, -595.2292140814271, 105.91089043985997, -3.265722705, -2.224349783232]
solar_sys_draw = drawingScript.solarSystem(1600, 1000)
draw_suns = (drawingScript.sun(solar_sys_draw, mass=10_000, position=(-400, 0), velocity=(0, 2.5)),
             drawingScript.sun(solar_sys_draw, mass=10_000, position=(400, 0), velocity=(0, -2.5)))
draw_planets = (drawingScript.planet(solar_sys_draw, mass=run[0], position=(run[1], run[2]), velocity=(run[3], run[4])))
tick = 0
while tick < 2_000:
    tick += 1
    time.sleep(0.01)
    solar_sys_draw.interactions()
    solar_sys_draw.update_bodies()
turtle.done()
