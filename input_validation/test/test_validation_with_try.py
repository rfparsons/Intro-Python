import unittest
from input_validation import validation_with_try


class test_average_negative_input(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(-90, 89, 78)

    def test_average_exception_2(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, -89, 78)

    def test_average_exception_3(self):
        with self.assertRaises(ValueError):
            validation_with_try.average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()
