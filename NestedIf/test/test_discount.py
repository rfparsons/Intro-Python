import unittest
from nested_if import discount


class under_10(unittest.TestCase):
    def test_under_10_5_cash_10per(self):
        total = discount.calculate_order(8, 5, 10)
        self.assertEqual(total, 8.81)

    def test_under_10_5_cash_15per(self):
        total = discount.calculate_order(8, 5, 15)
        self.assertEqual(total, 8.65)

    def test_under_10_5_cash_20per(self):
        total = discount.calculate_order(8, 5, 20)
        self.assertEqual(total, 8.49)

    def test_under_10_10_cash_10per(self):
        total = discount.calculate_order(8, 10, 10)
        self.assertEqual(total, 4.04)


class between_10_30(unittest.TestCase):
    def test_between_10_30_5_cash_0per(self):
        total = discount.calculate_order(25, 5, 0)
        self.assertEqual(total, 29.15)

    def test_between_10_30_5_cash_10per(self):
        total = discount.calculate_order(25, 5, 10)
        self.assertEqual(total, 27.03)

class between_30_50(unittest.TestCase):
    def test_between_10_30_5_cash_0per(self):
        total = discount.calculate_order(45, 5, 0)
        self.assertEqual(total, 54.35)

    def test_between_10_30_5_cash_20per(self):
        total = discount.calculate_order(45, 10, 20)
        self.assertEqual(total, 37.63)

class over_50(unittest.TestCase):
    def test_over_50_5_cash_0per(self):
        total = discount.calculate_order(75, 5, 0)
        self.assertEqual(total, 74.2)

    def test_over_50_5_cash_10per(self):
        total = discount.calculate_order(75, 5, 10)
        self.assertEqual(total, 66.78)


if __name__ == '__main__':
    unittest.main()
