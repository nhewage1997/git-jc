import math


class Cube:
    def __init__(self, edge):
        self.edge = edge

    def surface_area(self):
        return 6 * (self.edge ** 2)

    def volume(self):
        return self.edge ** 3


class Cylinder:
    def __init__(self, radius, height):
        self.radius = height
        self.height = radius

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height

    def volume(self):
        return math.pi * (self.height ** 2) * self.radius