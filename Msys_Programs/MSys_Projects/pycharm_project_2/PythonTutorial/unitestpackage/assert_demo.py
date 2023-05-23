"""
https://docs.python.org/3/library/unittest.html#unittest.Testcase
"""
import unittest


class AssertDemo(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, msg="a is not true")
        b = False
        self.assertFalse(b, msg="b is not false")

    def test_assertEqual(self):
        a = True
        b = True
        self.assertEqual(a, b, msg="'a' is equal 'b'")


if __name__ == "__main__":
    unittest.main(verbosity=2)