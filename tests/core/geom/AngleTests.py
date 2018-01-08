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

    def test_negative_0(self):
        angle = Angle(0)
        self.assertAlmostEqual((-angle).radians, 0)

    def test_negative_pi(self):
        angle = Angle(pi)
        self.assertAlmostEqual((-angle).radians, pi)

    def test_negative_3(self):
        angle = Angle(3)
        self.assertAlmostEqual((-angle).radians, 2 * pi - 3)

    def test_addition_pi_pi(self):
        angle = Angle(pi)
        self.assertAlmostEqual((angle + angle).radians, 0)

    def test_addition_2(self):
        angle1 = Angle(1)
        angle2 = Angle(2)
        self.assertAlmostEqual((angle1 + angle2).radians, 3)

    def test_addition_3(self):
        angle1 = Angle(4)
        angle2 = Angle(6)
        self.assertAlmostEqual((angle1 + angle2).radians, 10 - 2 * pi)

    def test_addition_symmetry(self):
        angle1 = Angle(1)
        angle2 = Angle(2)
        self.assertAlmostEqual((angle1 + angle2).radians, (angle2 + angle1).radians)

    def test_addition_transitivity(self):
        angle1 = Angle(1)
        angle2 = Angle(2)
        angle3 = Angle(3)
        self.assertAlmostEqual(((angle1 + angle2) + angle3).radians, (angle1 + (angle2 + angle3)).radians)
