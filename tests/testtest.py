import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, 1)


if __name__ == '__main__':
    unittest.main()
