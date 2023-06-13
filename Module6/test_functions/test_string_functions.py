import unittest
from more_functions import string_functions


class str_repetition(unittest.TestCase):
    def test_my_name_multiplied_7(self):
        result = string_functions.multiply_string("Bobby", 7)
        self.assertEqual(result, "BobbyBobbyBobbyBobbyBobbyBobbyBobby")
    def test_prof_name_multiplied_7(self):
        result = string_functions.multiply_string("Gilbertson", 3)
        self.assertEqual(result, "GilbertsonGilbertsonGilbertson")


if __name__ == '__main__':
    unittest.main()
