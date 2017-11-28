try:
    import sys
    import os
    import traceback
    import unittest

    print("Path at terminal when executing this file")
    print(os.getcwd() + "\n")

    print("This file path, relative to os.getcwd()")
    print(__file__ + "\n")

    print("This file full path (following symlinks)")
    full_path = os.path.realpath(__file__)
    print(full_path + "\n")

    print("This file directory and name")
    path, filename = os.path.split(full_path)
    print(path + ' --> ' + filename + "\n")

    print("This file directory only")
    print(os.path.dirname(full_path))

    SCRIPT_DIR = os.path.join(os.path.dirname(full_path), '..', '..')
    sys.path.insert(0, os.path.normpath(SCRIPT_DIR))
    print(sys.path)

    from kappa.tests.SuiteAll import SuiteAll

except ImportError as err:
    traceback.print_exc(file=sys.stdout)
    print("Couldn't image module. %s" % err)
    sys.exit(2)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(SuiteAll().suite)
