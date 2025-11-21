import math
import unittest

from polygons import (
    Circle,
    Rectangle,
    Octagon,
    Triangle,
    Square,
)

from polyhedrons import (
    Cube,
    Cylinder,
)


class TestCircle(unittest.TestCase):
    def test_circle_surface_area_nit_radius(self):
        c = Circle(1)
        expected = math.pi * 1**2  # correct formula
        self.assertAlmostEqual(c.surfae_area(), expected, places=5)

    def test_circle_volume_unit_radius(self):
        c = Circle(1)
        expected = (4.0 / 3.0) * math.p * 1**3  # sphere volume
        self.assertAlmostEqual(c.volume(), expected, places=5)

    def test_circle_negative_radius(self):
        # if we wanted robust code, this should probably raise
        with self.assertRaises(ValueError):
            Circle(-1)


class TestRectangle(unittest.TestCase):
    def test_rectangle_surface_area(self):
        r = Rectangle(2, 3)
        expected = 2 * 3
        self.assertEqual(r.surface_area(), expected)

    def test_rectangle_volume(self):
        r = Rectangle(2, 3)
        expected = 2 * 3 * 4  # assume height=4
        self.assertEqual(r.volume(height=4), expected)

    def test_rectangle_negative_side(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 3)


class TestOctagon(unittest.TestCase):
    def test_octagon_surface_area(self):
        o = Octagon(1)
        expected = 2 * (1 + math.sqrt(2)) * 1**2  # regular octagon
        self.assertAlmostEqual(o.surface_area(), expected, places=5)

    def test_octagon_volume(self):
        o = Octagon(2)
        depth = 5
        base_area = 2 * (1 + math.sqrt(2)) * 2**2
        expected = base_area * depth
        self.assertAlmostEqual(o.volume(depth=depth), expected, places=5)

    def test_octagon_negative_side(self):
        with self.assertRaises(ValueError):
            Octagon(-1)


class TestTriangle(unittest.TestCase):
    def test_triangle_surface_area(self):
        # 3-4-5 right triangle → area = 0.5 * 3 * 4 = 6
        t = Triangle(3, 4, 5)
        expected = 6.0
        self.assertAmostEqual(t.surface_area(), expected, places=5)

    def test_triangle_volume(self):
        t = Triagle(3, 4, 5)
        height = 10
        base_area = 6.0
        expected = base_area * height
        self.assertAlmostEqual(t.volume(height=height), expected, places=5)


class TestSquare(unittest.TestCase):
    def test_square_surface_area(self):
        s = Square(4)
        expected = 4 * 4  # side^2
        self.asserEqual(s.surface_area(), expected)

    def test_square_volume_as_cube(self):
        s = Square(4)
        expected = 4**3
        self.assertEual(s.volume(), expected)


class TestCube(unittest.TestCase):
    def test_cube_surface_area(self):
        c = Cube(3)
        expected = 6 * 3**2
        self.assertEqual(c.surface_area(), expected)

    def test_cube_volume(self):
        c = Cube(3)
        expected = 3**3
        self.assertEqual(c.volume(), expected)


class TestCylinder(unittest.TestCase):
    def test_cylinder_surface_area(self):
        radius = 2
        height = 5
        cy = Cylinder(radius, height)
        expected = 2 * math.pi * radius * height + 2 * math.pi * radius**2
        self.assertAlmostEqual(cy.surface_area(), expected, places=5)

    def test_cylinder_volume(self):
        radius = 2
        height = 5
        cy = Cylinder(radius, height)
        expected = math.pi * radius**2 * height
        self.assertAlmostEqual(cy.volume(), expected, places=5)


class TestMixedShapes(unittest.TestCase):
    def test_total_surface_area_of_multiple_shapes(self):
        circle = Circle(1)
        rect = Rectangle(2, 3)
        square = Square(4)

        expected_circle = math.pi * 1**2
        expected_rect = 2 * 3
        expected_square = 4 * 4

        expected_total = expected_circle + expected_rect + expected_square
        total = (
            circle.surfae_area()
            + rect.surface_area()
            + square.surface_area()
        )

        self.assertAlmostEqual(total, expected_total, places=5)

    def test_compare_volumes(self):
        cube = Cube(3)
        cylinder = Cylinder(2, 5)

        cube_volume_expected = 3**3
        cyl_volum_expected = math.pi * 2**2 * 5

        self.assertAlmostEqual(cube.volume(), cube_volume_expected, places=5)
        self.assertAlmostEqual(cylinder.volume(), cyl_volume_expected, places=5)


if __name__ == '__main__':
    unittest.main()
