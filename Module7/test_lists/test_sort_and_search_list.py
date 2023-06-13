import unittest
from unittest.mock import patch
from fun_with_lists import sort_and_search_list


class test_sorts(unittest.TestCase):
    def test_sort_list(self):
        list_to_sort = [5, 3, 4, 1, 2]
        sorted_list = [1, 2, 3, 4, 5]
        self.assertEqual(sort_and_search_list.sort_list(list_to_sort), sorted_list)

    def test_sort_long_list(self):
        list_to_sort = [5, 3, 4, 1, 2, 10, 8, 7, 9, 6]
        sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sort_and_search_list.sort_list(list_to_sort), sorted_list)

class test_searches(unittest.TestCase):
    def test_find_2(self):
        list_to_search = [5, 3, 4, 1, 2, 10, 8, 7, 9, 6]
        self.assertEqual(sort_and_search_list.search_list(list_to_search, 2), 4)

    def test_find_10(self):
        list_to_search = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0]
        self.assertEqual(sort_and_search_list.search_list(list_to_search, 10), 13)

if __name__ == "__main__":
    unittest.main()