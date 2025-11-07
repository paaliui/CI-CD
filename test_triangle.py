import unittest
from geom2d.triangle import triangle_perimeter, triangle_area

class TriangleTests(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12.0)

    def test_area_heron(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.0, places=7)

    def test_invalid_sides(self):
        for sides in [(0,1,1), (-1,2,3), (1,2,3), (10,1,1)]:
            with self.assertRaises((ValueError,)):
                triangle_area(*sides)

        with self.assertRaises(TypeError):
            triangle_area(3, "4", 5)  # type: ignore

if __name__ == "__main__":
    unittest.main()
