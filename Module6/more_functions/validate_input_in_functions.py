"""
Program: validate_input_in_functions.py
Author: Bobby Parsons

Contains a function to output a test name and a score
"""

def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
     Takes in a score and a test name and outputs both

     :param test_name: The name of the test
     :param test_score: The score recieved on the test
     :param invalid_message: The message returned when the value is out of range
     :returns: The name of the test and the score
     :raises ValueError: raises an exception when the value is out of range
    """
    if  type(test_score) is not int:
        raise ValueError
    if test_score < 0 or test_score > 100:
        return invalid_message
    else:
        return test_name + ": " + str(test_score)