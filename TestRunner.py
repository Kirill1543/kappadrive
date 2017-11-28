try:
    import sys
    import os
    import traceback
    import unittest

    SCRIPT_DIR = os.path.dirname(os.path.realpath(os.getcwd()))
    sys.path.insert(0, os.path.normpath(SCRIPT_DIR))

    from kappa.tests.SuiteAll import SuiteAll

except ImportError as err:
    traceback.print_exc(file=sys.stdout)
    print("Couldn't image module. %s" % err)
    sys.exit(2)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(SuiteAll().suite)
