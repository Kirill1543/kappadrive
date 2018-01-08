import unittest
from kappa.core.geom import Vector


class VectorTests(unittest.TestCase):
    def test_creation_1(self):
        vector = Vector(0)
        self.assertAlmostEqual(vector.x, 0)

    def test_creation_2(self):
        vector = Vector(1.5, 1.1)
        self.assertAlmostEqual(vector.x, 1.5)
        self.assertAlmostEqual(vector.y, 1.1)

    def test_creation3(self):
        vector = Vector(1, -2.5, 4)
        self.assertAlmostEqual(vector.x, 1)
        self.assertAlmostEqual(vector.y, -2.5)
        self.assertAlmostEqual(vector.z, 4)

    def test_copy(self):
        vector = Vector(1, 2, 3)
        vector_copy = vector.copy()
        self.assertAlmostEqual(vector.x, vector_copy.x)
        self.assertAlmostEqual(vector.y, vector_copy.y)
        self.assertAlmostEqual(vector.z, vector_copy.z)
        self.assertIsNot(vector, vector_copy)

    def test_normalize1(self):
        vector = Vector(0, 1, 0)
        vector_norm = vector.normalize()
        self.assertAlmostEquals(vector_norm.x, 0)
        self.assertAlmostEquals(vector_norm.y, 1)
        self.assertAlmostEquals(vector_norm.z, 0)

    def test_normalize2(self):
        vector = Vector(3, 4)
        vector_norm = vector.normalize()
        self.assertAlmostEquals(vector_norm.x, 0.6)
        self.assertAlmostEquals(vector_norm.y, 0.8)
