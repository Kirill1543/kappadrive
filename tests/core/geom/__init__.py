import unittest
from .AngleTests import AngleTests

__all__ = ["suite_geom"]


def suite_geom():
    loader: unittest.TestLoader = unittest.TestLoader()

    suite: unittest.TestSuite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(AngleTests))

    return suite
