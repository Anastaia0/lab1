import unittest
import math
from circle import area
from circle import perimeter

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(9), math.pi * 9 * 9)

        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 2 * math.pi * 4)

        self.assertEqual(perimeter(0), 0)