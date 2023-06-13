"""
Program: assign_average.py
Author: Bobby Parsons

Contains a function that uses a dictionary to return a value given a key, 
in a similar way to a switch-case statement
"""
def switch_average(letter):
    grades_dict = {'A':90, 'B':80, 'C':70, 'D': 60, 'F':0}
    upper_letter = letter.upper()

    return grades_dict.get(upper_letter, None)