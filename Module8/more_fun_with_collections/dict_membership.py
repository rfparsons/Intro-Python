"""
Program: dict_membership.py
Author: Bobby Parsons

Contains a function to test if a value is in a dictionary
"""

def in_dict(my_dict, value_to_find):
    found = False
    dict_list = list(my_dict)

    for key in dict_list:
        if my_dict[key] == value_to_find:
            found = True
    
    return found

if __name__ == "__main__":
    test_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
    print(in_dict(test_dict, 90))
    print(in_dict(test_dict, 95))