"""
Program: search_and_sort_array.py
Author: Bobby Parsons

Contains two functions to search through and sort arrays (that mostly just wrap around default Python functions)
"""
import array as arr

def sort_array(input_array):
    new_list = input_array.tolist() #make this conversion just to use sort function
    new_list.sort()
    new_array = arr.array('i', new_list)
    return new_array
    # I chose to return a value because I felt that would be more intuitive than the original array being changed and the original order may be important

def search_array(input_array, value_to_find):
    try:
        index = input_array.index(value_to_find)
        return index
    except:
        return -1