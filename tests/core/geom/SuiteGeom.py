import unittest

from .AngleTests import AngleTests


class SuiteGeom:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests(unittest.makeSuite(AngleTests))
