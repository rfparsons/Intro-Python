import unittest
from main import camper_age_input

class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        months = camper_age_input.convert_to_months(1)
        self.assertEqual(months, 12)

if __name__ == "__main__":
    unittest.main()