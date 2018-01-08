import unittest

from .VectorTests import VectorTests
from .AngleTests import AngleTests


class SuiteGeom:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests(unittest.makeSuite(AngleTests))
        self.suite.addTests(unittest.makeSuite(VectorTests))
