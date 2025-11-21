from calculate import (
    calculate_area_of_circle,
    calculate_area_of_rectangle,
    calculate_area_of_octagon
)
import math
import unittest

class TestGeometricMethods(unittest.TestCase):

    def test_calculate_area_of_circle(self):
        self.assertEqual(calculate_area_of_circle(1), math.pi)
        self.assert_raises(ValueError, calculate_area_of_circle, -1)

    def test_calculate_area_of_rectangle(self):
        self.assertEqual(calculate_area_of_rectangle(2, 3), 6)
        self.assert_raises(ValueError, calculate_area_of_rectangle, -2, 3)
        self.assert_raises(ValueError, calculate_area_of_rectangle, 2, -3)

    def test_calculate_area_of_octagon(self):
        self.assertEqual(calculate_area_of_octagon(1), 2 * (1 + 2**0.5))
        self.assert_raises(ValueError, calculate_area_of_octagon, -1)


if __name__ == '__main__':
    unittest.main()
    