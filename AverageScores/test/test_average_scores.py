import unittest
import unittest.mock as mock
from format_output import average_scores

class standard_test(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert average_scores.average(3) == 90

class easy_average(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[90,90,90,90,90]):
            assert average_scores.average(5) == 90

class barely_passed(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[59,58,99]):
            assert average_scores.average(3) == 72

if __name__ == '__main__':
    unittest.main()