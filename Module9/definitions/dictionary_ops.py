"""
Program: dictionary_ops.py
Author: Bobby Parsons

Contains dictionary-related functions
"""
def print_dict(dict_to_print):
    for key in dict_to_print:
        print(str(key) + ": ", end="")
        print(str(dict_to_print[key]))