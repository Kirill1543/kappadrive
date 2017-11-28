import unittest
from math import pi
from ....core.geom import Angle


class AngleTests(unittest.TestCase):
    def test_creation_0(self):
        angle: Angle = Angle(0)
        self.assertAlmostEqual(angle.radians, 0)

    def test_creation_2pi(self):
        angle: Angle = Angle(2 * pi)
        self.assertAlmostEqual(angle.radians, 0)
