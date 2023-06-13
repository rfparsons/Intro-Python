import unittest
from more_fun_with_collections import assign_average


class grade_tests(unittest.TestCase):
    def test_grade_caps_A(self):
        avg = assign_average.switch_average('A')
        self.assertEqual(avg, 90)

    def test_grade_lower_a(self):
        avg = assign_average.switch_average('a')
        self.assertEqual(avg, 90)

    def test_grade_B(self):
        avg = assign_average.switch_average('B')
        self.assertEqual(avg, 80)

    def test_grade_C(self):
        avg = assign_average.switch_average('C')
        self.assertEqual(avg, 70)

    def test_grade_D(self):
        avg = assign_average.switch_average('D')
        self.assertEqual(avg, 60)

    def test_grade_F(self):
        avg = assign_average.switch_average('F')
        self.assertEqual(avg, 0)

    def test_grade_nonexistant(self):
        avg = assign_average.switch_average('#')
        self.assertIsNone(avg)


if __name__ == '__main__':
    unittest.main()
