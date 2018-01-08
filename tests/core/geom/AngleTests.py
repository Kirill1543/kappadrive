import unittest
from math import pi
from kappa.core.geom import Angle


class AngleTests(unittest.TestCase):
    def test_creation_0(self):
        angle = Angle(0)
        self.assertAlmostEqual(angle.radians, 0)

    def test_creation_pi(self):
        angle = Angle(pi)
        self.assertAlmostEqual(angle.radians, pi)

    def test_creation_2pi(self):
        angle = Angle(2 * pi)
        self.assertAlmostEqual(angle.radians, 0)

    def test_creation_3pi(self):
        angle = Angle(3 * pi)
        self.assertAlmostEqual(angle.radians, pi)

    def test_creation_negative_pi(self):
        angle = Angle(-pi)
        self.assertAlmostEqual(angle.radians, pi)
