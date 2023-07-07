import turtle
import itertools as itr
import math as mt


class solarSystemBody(turtle.Turtle):
    min_display_size = 20
    scaling = 1.1

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = max(mt.log(self.mass, self.scaling), self.min_display_size)
        self.penup()
        self.hideturtle()
        self.tracer = turtle.Turtle()
        self.tracer.hideturtle()
        self.tracer.penup()
        self.tracer.setposition(position)
        self.tracer.pendown()
        solar_system.add_body(self)

    def draw(self):
        self.clear()
        self.dot((int(self.display_size)))

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])
        self.tracer.setx(self.xcor() + self.velocity[0])
        self.tracer.sety(self.ycor() + self.velocity[1])


class sun(solarSystemBody):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.tracer.pencolor("green")
        self.color("yellow")


class planet(solarSystemBody):
    colors = itr.cycle(["red", "green", "brown"])

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(planet.colors))
        self.tracer.pencolor("white")


class solarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        self.bodies = []

    def exit_program(self):
        self.solar_system.bye()

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        body.clear()
        self.bodies.remove(body)

    def update_bodies(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    @staticmethod
    def gravity(first: solarSystemBody, second: solarSystemBody):
        force = (first.mass * second.mass) / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acc = force / body.mass
            acc_x = acc * mt.cos(mt.radians(angle))
            acc_y = acc * mt.sin(mt.radians(angle))
            body.velocity = (body.velocity[0] + (reverse * acc_x), body.velocity[1] + (reverse * acc_y))
            reverse = -1

    def collision(self, first, second):
        if first.distance(second) < first.display_size / 2 + second.display_size / 2:
            for body in first, second:
                if isinstance(body, planet):
                    print("Collision.")
                    self.remove_body(body)

    def interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.gravity(first, second)
                self.collision(first, second)


