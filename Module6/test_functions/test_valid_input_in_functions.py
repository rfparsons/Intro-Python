import unittest
from more_functions import validate_input_in_functions


class mandatory_argument(unittest.TestCase):
    def test_score_input_test_name(self):
        result = validate_input_in_functions.score_input("Test Test")
        self.assertEqual(result, "Test Test: 0")


class optional_score(unittest.TestCase):
    def test_score_input_test_10(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=10)
        self.assertEqual(result, "Test Test: 10")

    def test_score_input_test_20(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=20)
        self.assertEqual(result, "Test Test: 20")

    def test_score_input_test_30(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=30)
        self.assertEqual(result, "Test Test: 30")

    def test_score_input_test_40(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=40)
        self.assertEqual(result, "Test Test: 40")


class range_tests(unittest.TestCase):
    def test_score_input_test_score_above_range(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=101)
        self.assertEqual(result, 'Invalid test score, try again!')

    def test_score_input_test_score_below_range(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=-20)
        self.assertEqual(result, 'Invalid test score, try again!')

    def test_score_input_test_score_valid(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=50)
        self.assertEqual(result, "Test Test: 50")

class other_tests(unittest.TestCase):
    def test_score_input_non_numeric(self):
        with self.assertRaises(ValueError):
            validate_input_in_functions.score_input("Test Test", test_score="B+")

    def test_score_input_invalid_message(self):
        result = validate_input_in_functions.score_input("Test Test", test_score=-20, invalid_message="Score out of range!")
        self.assertEqual(result, "Score out of range!")

if __name__ == '__main__':
    unittest.main()

# Function score_input() has only the mandatory argument
# 1 unit test test_score_input_test_name
# Function score_input() has the mandatory argument and one optional argument for test_score
# 4 unit tests
# one good input test_score_input_ test_score_valid
# one below range test_score_input_ test_score_below_range
# one above range test_score_input_ test_score_above_range
# one non-numeric input (make sure you account for an exception) test_test_score_non_numeric
# Has all arguments
# 1 unit test test_score_input_invalid_message
