"""
Program: set_membership.py
Author: Bobby Parsons

Contains a function to test if a value is in a set
"""

def in_set(my_set, value_to_find):
    found = False

    for num in my_set:
        if num == value_to_find:
            found = True
    
    return found

if __name__ == "__main__":
    print(in_set({1, 2, 3}, 2))
    print(in_set({1, 2, 3}, 5))