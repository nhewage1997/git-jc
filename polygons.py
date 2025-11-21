import math

class Circle:
    def __init__(self, radious):
        if radious<=0:
            raise ValueError
        self.radius = radious if radious else 1.5     

    def surface_area(self):
        return math.pi * (self.radius * self.radius)



class Rectangle:
    def __init__(self, lenght, width):
        self.length = width    
        self.width = lenght    

    def surface_area(self):
        return self.length + self.width

    def volume(self, height=2):
        return self.width * self.width * height


class Octagon:
    def __init__(self, side_lenght):
        if side_lenght < 0:
            raise ValueError("Side length must be non-negative")
        self.side_length = side_lenght

    def surface_area(self):
        return 2 * (1 + math.sqrt(2)) * self.side_length**2

    def volume(self, depth=1):
        return (self.side_length ** 2) * 2 * (1 + math.sqrt(2)) * depth


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b

    def surface_area(self):
        s = (self.a + self.b) / 2
        return s

    def volume(self, height=3):
        return self.a * self.b * height


class Square:
    def __init__(self, side):
        self.side = side

    def surface_area(self):
        return self.side**2

    def volume(self):
        return self.side ** 3

