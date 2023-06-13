"""
Program: search_and_sort_list.py
Author: Bobby Parsons

Contains two functions to search through and sort lists (that mostly just wrap around default Python functions)
"""

def sort_list(input_list):
    new_list = input_list # buffer list to not mess with input_list
    new_list.sort()
    return new_list #returns a list sorted using Python's default method
    # I chose to return a value because I felt that would be more intuitive than the original list being changed

def search_list(input_list, value_to_find):
    return input_list.index(value_to_find)