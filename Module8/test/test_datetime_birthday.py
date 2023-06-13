import unittest
from more_fun_with_collections import datetime_birthday
from datetime import datetime

class birthday_tests(unittest.TestCase): #🥳
    def test_half_birthday(self):
        birthday = datetime(2019, 12, 3)
        half_birthday = datetime(2020, 6, 3)
        result = datetime_birthday.half_birthday(birthday)

        self.assertEqual(half_birthday, result)