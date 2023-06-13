"""
Program: my_definitions.py
Author: Bobby Parsons

Contains various functions
"""
def hello_world():
    print("Hello!")

def credits():
    print("Author: Bobby Parsons")

def print_dict(dict_to_print):
    for key in dict_to_print:
        print(str(key) + ": ", end="")
        print(str(dict_to_print[key]))

def print_set(set_to_print):
    for item in set_to_print:
        print(item)