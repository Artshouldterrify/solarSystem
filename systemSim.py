import math as mt


# each body in the solar system
class solar_body:
    min_size = 20
    scaling = 1.1

    def __init__(self, solar_sys, mass, position=(0, 0), velocity=(0, 0)):
        self.mass = mass
        self.pos = list(position)
        self.velocity = list(velocity)
        self.size = max(float(self.min_size), mt.log(self.mass, self.scaling))
        solar_sys.add_body(self)

    def move(self):
        self.pos[0] = self.pos[0] + self.velocity[0]
        self.pos[1] = self.pos[1] + self.velocity[1]


# sun deriving from body
class sun(solar_body):
    def __init__(self, solar_sys, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_sys, mass, position, velocity)


# planet deriving from body
class planet(solar_body):
    def __init__(self, solar_sys, mass, position=(0, 0), velocity=(0, 0)):
        super().__init__(solar_sys, mass, position, velocity)


# the solar system itself
class solar_system:
    def __init__(self):
        self.bodies = list()

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def move_bodies(self):
        for body in self.bodies:
            body.move()

    @staticmethod
    def gravity(first: solar_body, second: solar_body):
        dist = mt.sqrt((first.pos[0] - second.pos[0]) ** 2 + (first.pos[1] - second.pos[1]) ** 2)
        force = (first.mass * second.mass) / dist ** 2
        theta = mt.atan2((-first.pos[1] + second.pos[1]), (-first.pos[0] + second.pos[0])) * 180 / mt.pi
        reverse = 1
        for body in first, second:
            acc = force / body.mass
            acc_x = acc * mt.cos(mt.radians(theta))
            acc_y = acc * mt.sin(mt.radians(theta))
            body.velocity[0] = body.velocity[0] + (reverse * acc_x)
            body.velocity[1] = body.velocity[1] + (reverse * acc_y)
            reverse = -1

    @staticmethod
    def collision(first: solar_body, second: solar_body):
        dist = mt.sqrt((first.pos[0] - second.pos[0]) ** 2 + (first.pos[1] - second.pos[1]) ** 2)
        if dist < ((first.size / 2) + (second.size / 2)):
            return True
        return False

    def interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.gravity(first, second)
                if self.collision(first, second):
                    return True
        return False

    def simulate(self):
        ticks = 0
        while ticks < 2_000:
            val = self.interactions()
            if val:
                break
            self.move_bodies()
            planet_x, planet_y = self.bodies[2].pos[0], self.bodies[2].pos[1]
            if planet_x > 900 or planet_x < -900 or planet_y > 600 or planet_y < -600:
                break
            ticks += 1
        return ticks
