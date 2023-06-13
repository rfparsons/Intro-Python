"""
Program: cast_to_integer.py
Author: Bobby Parsons
Last date modified: 01/23/2020



The purpose of this program is to accept any input, 
convert to a integer type and output the integer. 
"""
str_to_cast = input("Please enter a number: ")
#print(str_to_cast)
result = int(float(str_to_cast))
print(result)

# Input   Expected Output  Actual Output
#    5           5               5
#   4.3          4               4
#  'somestr'     0?            Error        
