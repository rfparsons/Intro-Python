import unittest
import array as arr
from unittest.mock import patch
from fun_with_lists import sort_and_search_array


class test_sorts(unittest.TestCase):
    def test_sort_array(self):
        array_to_sort = arr.array('i', [5, 3, 4, 1, 2])
        sorted_array = arr.array('i', [1, 2, 3, 4, 5])
        self.assertEqual(sort_and_search_array.sort_array(array_to_sort), sorted_array)

    def test_sort_long_array(self):
        array_to_sort = arr.array('i', [5, 3, 4, 1, 2, 10, 8, 7, 9, 6])
        sorted_array = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(sort_and_search_array.sort_array(array_to_sort), sorted_array)

class test_searches(unittest.TestCase):
    def test_find_2(self):
        array_to_search = arr.array('i', [5, 3, 4, 1, 2, 10, 8, 7, 9, 6])
        self.assertEqual(sort_and_search_array.search_array(array_to_search, 2), 4)

    def test_find_10(self):
        array_to_search = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0])
        self.assertEqual(sort_and_search_array.search_array(array_to_search, 10), 13)

    def test_dont_find_10(self):
        array_to_search = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(sort_and_search_array.search_array(array_to_search, 10), -1)

if __name__ == "__main__":
    unittest.main()