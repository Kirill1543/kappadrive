import unittest
from .geom import suite_geom

__all__ = ["suite_core"]


def suite_core():
    loader: unittest.TestLoader = unittest.TestLoader()

    suite: unittest.TestSuite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(suite_geom()))

    return suite
