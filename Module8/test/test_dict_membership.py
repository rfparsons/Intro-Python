import unittest
from more_fun_with_collections import dict_membership


class set_tests(unittest.TestCase):
    def test_in_set_true(self):
        test_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
        result = dict_membership.in_dict(test_dict, 90)
        self.assertTrue(result)
    def test_in_set_false(self):
        test_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
        result = dict_membership.in_dict(test_dict, 89)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
