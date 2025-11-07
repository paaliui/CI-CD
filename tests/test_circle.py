import unittest
import math
from geom2d.circle import circle_area, circle_circumference

class CircleTests(unittest.TestCase):
    def test_area_basic(self):
        self.assertAlmostEqual(circle_area(1.0), math.pi, places=7)
        self.assertAlmostEqual(circle_area(3.0), math.pi * 9.0, places=7)

    def test_circumference_basic(self):
        self.assertAlmostEqual(circle_circumference(0.0), 0.0, places=7)
        self.assertAlmostEqual(circle_circumference(2.5), 2 * math.pi * 2.5, places=7)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(TypeError):
            circle_area("5")  # type: ignore

if __name__ == "__main__":
    unittest.main()
