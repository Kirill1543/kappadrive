import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_testing_bitbucket(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()
