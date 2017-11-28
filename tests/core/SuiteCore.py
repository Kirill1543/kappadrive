import unittest

from .geom.SuiteGeom import SuiteGeom


class SuiteCore:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests(SuiteGeom().suite)
