import unittest

from .core.SuiteCore import SuiteCore


class SuiteAll:
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTests(SuiteCore().suite)
