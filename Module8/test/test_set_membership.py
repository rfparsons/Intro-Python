import unittest
from more_fun_with_collections import set_membership


class set_tests(unittest.TestCase):
    def test_in_set_true(self):
        result = set_membership.in_set({1, 2, 3}, 2)
        self.assertTrue(result)
    def test_in_set_false(self):
        result = set_membership.in_set({1, 2, 3}, 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
