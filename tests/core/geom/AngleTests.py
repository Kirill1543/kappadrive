import unittest
from math import pi
from kappa.core.geom import Angle


class AngleTests(unittest.TestCase):
    def test_creation_0(self):
        self.assertAlmostEqual(Angle(0).radians, 0)

    def test_creation_pi(self):
        self.assertAlmostEqual(Angle(pi).radians, pi)

    def test_creation_2pi(self):
        self.assertAlmostEqual(Angle(2 * pi).radians, 0)

    def test_creation_3pi(self):
        self.assertAlmostEqual(Angle(3 * pi).radians, pi)

    def test_creation_99pi(self):
        self.assertAlmostEqual(Angle(99 * pi).radians, pi)

    def test_creation_100pi(self):
        self.assertAlmostEqual(Angle(100 * pi).radians, 0)

    def test_creation_negative_pi(self):
        self.assertAlmostEqual(Angle(-pi).radians, pi)

    def test_negative_0(self):
        self.assertAlmostEqual((-Angle(0)).radians, 0)

    def test_negative_pi(self):
        self.assertAlmostEqual((-Angle(pi)).radians, pi)

    def test_negative_3(self):
        self.assertAlmostEqual((-Angle(3)).radians, 2 * pi - 3)

    def test_addition_pi_pi(self):
        self.assertAlmostEqual((Angle(pi) + Angle(pi)).radians, 0)

    def test_addition_2(self):
        self.assertAlmostEqual((Angle(1) + Angle(2)).radians, 3)

    def test_addition_3(self):
        self.assertAlmostEqual((Angle(4) + Angle(6)).radians, 10 - 2 * pi)

    def test_addition_symmetry(self):
        self.assertAlmostEqual((Angle(1) + Angle(2)).radians, (Angle(2) + Angle(1)).radians)

    def test_addition_transitivity(self):
        self.assertAlmostEqual(((Angle(1) + Angle(2)) + Angle(3)).radians, (Angle(1) + (Angle(2) + Angle(3))).radians)

    def test_subtraction_same(self):
        self.assertAlmostEqual((Angle(pi) - Angle(pi)).radians, 0)

    def test_subtraction(self):
        self.assertAlmostEqual((Angle(2) - Angle(1)).radians, 1)

    def test_subtraction_less_zero(self):
        self.assertAlmostEqual((Angle(1) - Angle(2)).radians, 2 * pi - 1)

    def test_subtraction_as_addition(self):
        self.assertAlmostEqual((Angle(2) - Angle(1)).radians, (Angle(2) + Angle(-1)).radians)

    def test_equals(self):
        self.assertTrue(Angle(1) == Angle(1))

    def test_equals_false(self):
        self.assertFalse(Angle(1) == Angle(2))

    def test_equals_with_2pi(self):
        self.assertTrue(Angle(1) == Angle(1 + 2 * pi))

    def test_equals_false_with_2pi(self):
        self.assertFalse(Angle(1) == Angle(2 + 2 * pi))

    def test_equals_addition(self):
        self.assertTrue(Angle(1) + Angle(2) == Angle(3))

    def test_not_equals(self):
        self.assertTrue(Angle(1) != Angle(2))

    def test_not_equals_false(self):
        self.assertFalse(Angle(1) != Angle(1))

    def test_not_equals_with_2pi(self):
        self.assertTrue(Angle(1) != Angle(2 + 2 * pi))

    def test_not_equals_false_with_2pi(self):
        self.assertFalse(Angle(1) != Angle(1 + 2 * pi))

    def test_not_equals_addition(self):
        self.assertTrue(Angle(1) + Angle(2) != Angle(4))

    def test_less(self):
        self.assertTrue(Angle(1) < Angle(2))
        self.assertTrue(Angle(1 + 2 * pi) < Angle(2))
        self.assertTrue(Angle(1 + 4 * pi) < Angle(2 + 2 * pi))

    def test_less_false(self):
        self.assertFalse(Angle(1) < Angle(1))
        self.assertFalse(Angle(2) < Angle(1))
        self.assertFalse(Angle(2) < Angle(1 + 2 * pi))

    def test_less_equals(self):
        self.assertTrue(Angle(1) <= Angle(1))
        self.assertTrue(Angle(1) <= Angle(2))
        self.assertTrue(Angle(1 + 2 * pi) <= Angle(2))

    def test_less_equals_false(self):
        self.assertFalse(Angle(2) <= Angle(1))
        self.assertFalse(Angle(2) <= Angle(1 + 2 * pi))

    def test_greater(self):
        self.assertTrue(Angle(2) > Angle(1))
        self.assertTrue(Angle(pi) > Angle(2 * pi))

    def test_greater_false(self):
        self.assertFalse(Angle(1) > Angle(1))
        self.assertFalse(Angle(1) > Angle(2))
        self.assertFalse(Angle(1 + 2 * pi) > Angle(2))

    def test_greater_equals(self):
        self.assertTrue(Angle(1) >= Angle(1))
        self.assertTrue(Angle(2) >= Angle(1))
        self.assertTrue(Angle(1) >= Angle(2 * pi))

    def test_greater_equals_false(self):
        self.assertFalse(Angle(1) >= Angle(2))
        self.assertFalse(Angle(2 * pi) >= Angle(1))

    def test_between(self):
        self.assertTrue(Angle(1).is_between(Angle(0), Angle(2)))
        self.assertTrue(Angle(1).is_between(Angle(1), Angle(2)))
        self.assertTrue(Angle(1).is_between(Angle(0), Angle(1)))
        self.assertTrue(Angle(1 + 2 * pi).is_between(Angle(0), Angle(2)))
        self.assertTrue(Angle(1).is_between(Angle(2 * pi), Angle(6)))
        self.assertTrue(Angle(0).is_between(Angle(pi), Angle(pi - 0.1)))
        self.assertTrue(Angle(2).is_between(Angle(2), Angle(2)))
        self.assertFalse(Angle(1).is_between(Angle(2), Angle(2)))
